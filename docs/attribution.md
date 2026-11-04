# Visitor and order attribution

This static storefront uses the GA4 measurement ID in `site/config.json`. The
shared page template loads the Google tag once. Preview builds omit the tag.
Do not add a second tag or Tag Manager container for the same property.

The existing events are:

- `view_item`: a product page is viewed.
- `add_to_cart`: the quantity actually added by an Add button, after the local
  cart limit. Clicking an item already at its limit emits no additional event.
- `begin_checkout`: the customer clicks the Shopify checkout handoff. This is
  an intent event; it does not confirm that checkout loaded or payment succeeded.
- `generate_lead`: an existing phone, directions, email, or booking link is clicked.

The cart's quantity controls are not separately instrumented. A cart's final
quantity can therefore differ from the sum of Add button events. Live price and
stock checks can also change the cart after an addition. GA4 reports only events
that reach Google; blocked scripts and visitor privacy choices affect coverage.

## Links to Namaste Bookshop

The shared footer links directly to `https://namastebookshop.com/`. Checkout
continues to use Shopify's multi-item `/cart/VARIANT:QUANTITY,...` permalink and
keeps the existing order markers:

- `attributes[Storefront]=Namaste Incense Shop`
- `attributes[Site]=namasteincenseshop.com`
- `note=Ordered on Namaste Incense Shop (namasteincenseshop.com)`
- `ref=namasteincenseshop`

Both the footer link and checkout link also carry fixed campaign labels:

| Parameter | Value |
| --- | --- |
| `utm_source` | `namasteincenseshop.com` |
| `utm_medium` | `referral` |
| `utm_campaign` | `storefront` |
| `utm_content` | `bookshop_footer` or `checkout` |

These labels describe the immediate referring storefront. They do not copy
incoming query strings, customer details, visitor identifiers, or advertising
click IDs. They do not preserve an earlier marketing touchpoint or establish a
shared session across domains. No new analytics service or browser storage is
introduced by these link labels.

## Evidence required for sales reporting

Use Shopify's completed order records to verify the Storefront/Site attributes
or referral code, and distinguish paid, cancelled, refunded, and test orders as
appropriate for the report. Missing markers are unattributed, not proof that a
customer never used this site. Campaign labels alone do not prove that an order
was placed.

This repository does not emit `purchase`. Purchase reporting must come from
verified Shopify checkout/order integration. Do not turn a checkout click into a
purchase event or install another checkout pixel without auditing the existing
Bookshop integration. GA4 reporting access and any cross-domain configuration
must be checked in the merchant's account; the public measurement ID is not
reporting access.

References: [Shopify cart permalink parameters](https://shopify.dev/docs/apps/build/checkout/create-cart-permalinks),
[GA4 ecommerce events](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce).
