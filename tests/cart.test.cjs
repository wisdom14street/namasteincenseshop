const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const test = require('node:test');
const vm = require('node:vm');

const source = fs.readFileSync(path.join(__dirname, '../src/assets/cart.js'), 'utf8');
const item = {v:'12345', h:'test-incense', t:'Test incense', p:4.99, q:1, max:0, c:'incense'};

// Run the real cart against isolated browser adapters; no network or analytics is sent.
function cart(initial = [], analytics = true) {
  let saved = JSON.stringify(initial);
  const listeners = {}, events = [];
  const window = {
    NI_CART: {shop:'https://namastebookshop.com', attr:'?attributes%5BStorefront%5D=Namaste%20Incense%20Shop',
      brand:'Namaste Incense Shop', domain:'namasteincenseshop.com', ref:'namasteincenseshop'},
    addEventListener() {},
  };
  if (analytics) window.gtag = (...args) => events.push(args);
  const document = {querySelector:() => null, querySelectorAll:() => [],
    addEventListener:(name, fn) => { listeners[name] = fn; }};
  vm.runInNewContext(source, {window, document,
    localStorage:{getItem:() => saved, setItem:(_, value) => { saved = value; }},
    fetch:() => new Promise(() => {}), setTimeout() {}, URL, URLSearchParams});
  const click = (attributes, dataset = {}) => {
    const target = {dataset, disabled:false, textContent:'Add to cart', classList:{add(){}, remove(){}},
      closest:() => target, hasAttribute:key => key in attributes, getAttribute:key => attributes[key] ?? null};
    listeners.click({target, preventDefault(){}});
    return target;
  };
  return {window, events, click, items:() => JSON.parse(saved)};
}

test('add_to_cart records the actual increase at an existing item limit', () => {
  const c = cart([{...item, q:4, max:5}]);
  c.click({'data-atc':''}, {...item, q:'3'});
  assert.equal(c.items()[0].q, 5);
  assert.equal(c.events.length, 1);
  assert.equal(c.events[0][1], 'add_to_cart');
  assert.equal(c.events[0][2].items[0].quantity, 1);
  assert.equal(c.events[0][2].value, 4.99);
});

test('clicking a full cart item does not invent another add event', () => {
  const c = cart([{...item, q:5, max:5}]);
  c.click({'data-atc':''}, item);
  assert.equal(c.items()[0].q, 5);
  assert.equal(c.events.length, 0);
});

test('a new large quantity reports the hard cap, and bundles omit unchanged items', () => {
  const c = cart([{...item, q:2, max:2}]);
  c.click({'data-atc-items':JSON.stringify([item, {...item, v:'67890', q:200}])});
  assert.equal(c.items()[1].q, 99);
  assert.equal(c.events.length, 1);
  const event = c.events[0][2];
  assert.equal(event.items.length, 1);
  assert.equal(event.items[0].item_id, '67890');
  assert.equal(event.items[0].quantity, 99);
  assert.equal(event.value, 494.01);
});

test('checkout preserves the basket, notes and origin markers and adds static campaign tags', () => {
  const c = cart([{...item, q:2}, {...item, v:'67890', q:1}, {...item, v:'99999', q:3, out:true}]);
  const target = c.click({'data-checkout':''});
  const url = new URL(target.href);
  assert.equal(url.origin, 'https://namastebookshop.com');
  assert.equal(url.pathname, '/cart/12345:2,67890:1');
  assert.equal(url.searchParams.get('attributes[Storefront]'), 'Namaste Incense Shop');
  assert.equal(url.searchParams.get('attributes[Site]'), 'namasteincenseshop.com');
  assert.equal(url.searchParams.get('note'), 'Ordered on Namaste Incense Shop (namasteincenseshop.com)');
  assert.equal(url.searchParams.get('ref'), 'namasteincenseshop');
  assert.equal(url.searchParams.get('utm_source'), 'namasteincenseshop.com');
  assert.equal(url.searchParams.get('utm_medium'), 'referral');
  assert.equal(url.searchParams.get('utm_campaign'), 'storefront');
  assert.equal(url.searchParams.get('utm_content'), 'checkout');
  assert.equal(c.events.length, 1);
  assert.equal(c.events[0][1], 'begin_checkout');
  assert.equal(c.events[0][2].value, 14.97);
  assert.equal(c.events[0][2].items.length, 2);
  assert.ok(c.events.every(e => e[1] !== 'purchase'));
});

test('empty or sold-out carts have no checkout URL or checkout event', () => {
  for (const initial of [[], [{...item, out:true}]]) {
    const c = cart(initial);
    assert.equal(c.window.NI_CART_URL(), '');
    c.click({'data-checkout':''});
    assert.equal(c.events.length, 0);
  }
});

test('blocked or failing analytics cannot stop add or checkout', () => {
  for (const mode of ['absent', 'throws']) {
    const c = cart([], false);
    if (mode === 'throws') c.window.gtag = () => { throw new Error('blocked'); };
    c.click({'data-atc':''}, item);
    assert.equal(c.items()[0].q, 1);
    assert.equal(new URL(c.click({'data-checkout':''}).href).pathname, '/cart/12345:1');
  }
});
