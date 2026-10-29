"""Namaste Incense Shop (namasteincenseshop.com): the ritual and smudge apothecary. Copy written for this site only."""
import re
E = __import__('html').escape

AISLES = {
 'smudge':  ('Sage & Smudge Bundles', 'Sage', 'sage-smudge', 'White sage, blue sage, cedar, yerba santa, sweetgrass and mixed herb bundles, tied and ready to light.', '#6f7d4f'),
 'palo':    ('Palo Santo', 'Palo Santo', 'palo-santo', 'Palo santo sticks, chips and cones: sweet, woody smoke for clearing and calm.', '#a7744a'),
 'resins':  ('Resins & Tree Saps', 'Resins', 'resins', "Frankincense, myrrh, copal, benzoin, dragon's blood and other tears and saps for the coal.", '#9c6b1f'),
 'incense': ('Temple & Ritual Incense', 'Ritual Incense', 'ritual-incense', 'Sage, palo santo, copal, frankincense and myrrh in stick and cone form, plus resin-on-a-stick from New Mexico.', '#7a1f1f'),
 'charcoal':('Charcoal & Tools', 'Charcoal', 'charcoal-tools', 'Quick-light charcoal tablets, tongs and the small tools that make resin easy.', '#3d3a36'),
 'burners': ('Censers & Smudge Bowls', 'Censers', 'censers-bowls', 'Brass censers, cauldrons, abalone and ceramic smudge bowls to hold the heat.', '#5b4a6b'),
 'candles': ('Ritual & Reiki Candles', 'Candles', 'ritual-reiki-candles', 'Herbal, smudge, chakra, intention and Reiki-charged candles for altar and practice.', '#b5532a'),
 'kits':    ('Ritual & Smudge Kits', 'Kits', 'ritual-kits', 'Ready-made cleansing and intention kits that put the herbs, tools and instructions in one box.', '#4f6d6a'),
}
KIT = re.compile(r'\bkit\b|bundle set|ritual set|smudge set|cleansing set', re.I)
CHAR = re.compile(r'charcoal|swift.?lite|tongs|briquet|tablet', re.I)
RITUAL_STICK = re.compile(r'sage|palo santo|copal|frankincense|myrrh|benzoin|dragon.?s ?blood|cedar|sweet ?grass|church|temple|resin|pinon|piñon|juniper|smudge|cleansing|protection|archangel|chakra|ritual', re.I)
def assign(x):
    t = x['title']; b = x['base']
    if b in ('smudge', 'candles') and KIT.search(t): return 'kits'
    if re.search(r'palo santo', t, re.I) and not re.search(r'sage', t, re.I) and b in ('smudge', 'sticks', 'cones') and (b == 'smudge' or re.search(r'palo santo (sticks|cones \(12|chips|wood)|made in peru|^palo santo incense sticks pack', t, re.I)): return 'palo'
    if b == 'smudge': return 'smudge'
    if b == 'resins': return 'resins'
    if b == 'burners': return 'charcoal' if CHAR.search(t) else ('burners' if not re.search(r'backflow|waterfall', t, re.I) else '')
    if b == 'candles': return 'candles'
    if b in ('sticks', 'cones') and (RITUAL_STICK.search(t) or x['brand'] in ('fred-soll', 'wolf-spirit', 'archangel-incense', 'soul-sticks')): return 'incense'
    return ''

VISIT_EYEBROW = 'The apothecary counter'
def STORE_DESC(S): return f'Ritual and smudge apothecary on West 14th Street near Union Square: white sage, palo santo, frankincense, myrrh, copal, charcoal, censers and ritual candles, about {S.ABOUT_N:,} items.'
REVIEW_TITLE = 'Found your sage here?'
REVIEW_TEXT = 'A few words on Google tell the next person looking for sage, palo santo or resin near Union Square where to go. Thank you for taking a moment.'
LOGO_SVG = '<svg viewBox="0 0 40 40"><path d="M12 30h16l-2 5H14z" fill="#c9a227"/><path d="M20 28c-5-5 4-8-1-14s3-7 1-11" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><path d="M16 22l8-8" stroke="#c0504d" stroke-width="2.4" stroke-linecap="round"/></svg>'
WORDMARK = 'Namaste Incense <b>Shop</b>'
BAR_TEXT = 'Sage, palo santo & resin on West 14th St'
SEARCH_PLACEHOLDER = 'Search sage, palo santo, copal, charcoal'

QUIZ = {
 'slug': 'ritual-finder', 'nav': 'Ritual finder', 'cta': 'Start the ritual finder',
 'title': 'Ritual Finder: Sage, Resin or Candle?', 'desc': 'Tell us what the ritual is for and get matching sage, palo santo, resin or candles from current stock near Union Square.',
 'h1': 'Ritual finder', 'lead': 'Pick what you are working on and how you like to burn, and we will pull matching pieces from the apothecary shelves. It all runs on this page; nothing you choose is stored.',
 'submit': 'Find my ritual supplies',
 'questions': [
  {'q': 'What is the ritual for?', 'options': [
    {'label': 'Clearing a home or new space', 'filter': {'aisle': ['smudge', 'palo', 'kits']}},
    {'label': 'Setting an intention', 'filter': {'aisle': ['candles', 'kits']}},
    {'label': 'Prayer or meditation', 'filter': {'aisle': ['resins', 'incense']}},
    {'label': 'A gift for someone starting out', 'filter': {'aisle': ['kits', 'smudge', 'palo']}}]},
  {'q': 'Which smoke draws you in?', 'options': [
    {'label': 'Green and herbal, like sage', 'filter': {'fam': ['herbal']}},
    {'label': 'Woody and sweet, like palo santo', 'filter': {'fam': ['woods']}},
    {'label': 'Church and temple resins', 'filter': {'fam': ['resinous']}},
    {'label': 'Surprise me', 'filter': {}}]},
  {'q': 'Your budget?', 'options': [
    {'label': 'Under $10', 'filter': {'maxp': 10}}, {'label': 'Under $25', 'filter': {'maxp': 25}}, {'label': 'No limit', 'filter': {}}]},
 ]}

def FOOTER_EXPLORE(S):
    return [('Ritual finder', '/ritual-finder/'), ('How to smudge a room', '/guide/how-to-smudge-a-room/'), ('Palo santo basics', '/guide/palo-santo-basics/'),
            ('Charcoal & resin, step by step', '/guide/charcoal-and-resin/'), ('Smudge supplies near Union Square', '/smudge-supplies-near-union-square/'), ('White sage', '/white-sage/'), ('Frankincense & myrrh', '/frankincense-myrrh/')]
FOOT_BLURB = 'An apothecary for ritual smoke: herbs, saps, coals and the vessels to hold them, sold from the counter at 2 West 14th Street.'
HERO_BASES = ('smudge', 'resins', 'candles')
def HERO(S):
    return {'eyebrow': 'Ritual &amp; smudge apothecary, West 14th Street',
            'h1': 'Sage, palo santo and temple resins, <em>counted out for ritual.</em>',
            'lede': f'{S.cat_count["smudge"] + S.cat_count["palo"]} bundles and sticks of sage and palo santo, {S.cat_count["resins"]} resins, plus charcoal, censers, smudge kits and ritual candles. Pick them up a few doors west of Union Square, open every day from 11.',
            'shop_cta': 'Browse the apothecary'}

def _shelves(S):
    rows = ''.join(f'<li><a href="/shop/{AISLES[k][2]}/"><b>{E(AISLES[k][0])}</b></a> <span class="small">{S.cat_count[k]}</span><br><span>{E(AISLES[k][3])}</span></li>' for k in S.AISLE_KEYS)
    return f'<section class="wrap"><div class="sechead"><h2>The apothecary shelves</h2><a href="/shop/">Everything &rarr;</a></div><ul class="whys">{rows}</ul></section>'
def _starter(S): return S.by_rank([x for x in S.leaders if x['aisle'] in ('smudge', 'palo', 'kits') and x['price'] < 15])[:8]
def _resins(S): return S.by_rank([x for x in S.leaders if x['aisle'] in ('resins', 'charcoal')])[:8]
def _candles(S): return S.by_rank([x for x in S.leaders if x['aisle'] == 'candles'])[:8]
def _new(S): return [x for x in S.leaders][:8]
def _whys(S):
    return [('Every herb has a listing', 'Each bundle, stick and resin has its own photo and price online, so you know what is on the shelf before you walk over.'),
            ('Coal, vessel and resin together', 'Charcoal tablets, tongs, censers and resins sit side by side, so you leave with everything a first resin burn needs.'),
            (('Reserve and collect', f'Order online, pick Pickup at checkout, then stop by West 14th Street. Orders are {S.READY.lower()}.') if S.PICKUP_ON else ('', '')),
            ('Clear how-to guides', 'Plain step-by-step guides for smudging, palo santo and resin, written with safety first.')]
HOME_SECTIONS = [
 {'type': 'html', 'html': _shelves},
 {'type': 'grid', 'title': 'Start here: sage, palo santo and kits', 'select': _starter, 'href': '/shop/sage-smudge/', 'link': 'All sage', 'intro': 'The pieces people reach for most when clearing a space for the first time, ranked by what sells at namastebookshop.com.'},
 {'type': 'collections', 'title': 'Ritual collections', 'items': [
   {'title': 'White sage', 'blurb': 'Bundles, loose leaf and sticks.', 'href': '/white-sage/', 'filter': {'q': 'white sage'}},
   {'title': 'Palo santo', 'blurb': 'Sticks, chips and cones.', 'href': '/shop/palo-santo/', 'filter': {'aisle': ['palo']}},
   {'title': 'Frankincense & myrrh', 'blurb': 'The temple pair, as tears and sticks.', 'href': '/frankincense-myrrh/', 'filter': {'q': 'frankincense|myrrh'}},
   {'title': 'Copal', 'blurb': 'Bright, piney resin from the Americas.', 'href': '/copal/', 'filter': {'q': 'copal'}},
   {'title': 'Smudge & ritual kits', 'blurb': 'Everything in one box.', 'href': '/shop/ritual-kits/', 'filter': {'aisle': ['kits']}},
   {'title': 'Chakra candles', 'blurb': 'Seven colors for seven centers.', 'href': '/chakra-candles/', 'filter': {'q': 'chakra'}}]},
 {'type': 'visit'},
 {'type': 'grid', 'title': 'For the coal: resins and charcoal', 'select': _resins, 'href': '/shop/resins/', 'link': 'All resins', 'intro': 'New to resin? Read <a href="/guide/charcoal-and-resin/">charcoal and resin, step by step</a>.'},
 {'type': 'quiz', 'title': 'Not sure where to begin?', 'text': 'The ritual finder matches what you are working on to sage, resin or candles we have today.'},
 {'type': 'grid', 'title': 'Ritual and Reiki candles', 'select': _candles, 'href': '/shop/ritual-reiki-candles/', 'link': 'All candles'},
 {'type': 'whys', 'title': 'Why shop the apothecary', 'items': _whys},
 {'type': 'grid', 'title': 'Just in', 'select': _new, 'href': '/shop/?sort=new', 'link': 'Newest first'},
 {'type': 'brands', 'title': 'Makers on our shelves', 'n': 12},
 {'type': 'review'},
 {'type': 'band', 'title': 'Order tonight, collect tomorrow', 'text': lambda S: 'Prices and stock on every listing come straight from the store. Reserve online and collect at the counter, or have it posted from New York City.',
  'steps': lambda S: [('Choose your herbs and tools', 'Browse by shelf, scent, maker or price.'), ('Select Pickup at checkout', 'Payment runs on Shopify through namastebookshop.com.'), ('Collect on West 14th', f'{S.STORE_ADDR}, just west of Fifth Avenue.')]},
]
def HOME_TITLE(S): return 'Namaste Incense Shop | Sage, Palo Santo & Resin near Union Square, NYC'
def HOME_DESC(S): return f'Ritual and smudge apothecary at {S.STORE_ADDR}: white sage, palo santo, frankincense, myrrh, copal, charcoal, censers, smudge kits and Reiki candles. Reserve online, collect near Union Square.'
def SHOP_TITLE(S): return 'Shop Sage, Palo Santo, Resin & Ritual Supplies | Namaste Incense Shop'
def SHOP_DESC(S): return f'{S.N:,} ritual supplies in stock: sage bundles, palo santo, resins, charcoal, censers, smudge kits and ritual candles. Collect at 2 West 14th Street or ship from NYC.'
SHOP_H1 = 'The whole apothecary'
def SHOP_SUB(S): return f'{S.N:,} herbs, resins, tools and candles on {len(S.AISLE_KEYS)} shelves. Filter by shelf, scent, maker or price.'
def AISLE_TITLE(S, k): return f'{AISLES[k][0]} near Union Square, NYC | Namaste Incense Shop'
def AISLE_DESC(S, k): return f'{S.cat_count[k]} {AISLES[k][0].lower()} at the Namaste Incense Shop apothecary, 2 West 14th Street. {AISLES[k][3]}'

def LANDINGS(S):
    return [
     {'path': '/white-sage/', 'title': 'White Sage Bundles & Smudge Sticks in NYC | Namaste Incense Shop', 'desc': 'White sage bundles, loose sage and sage incense near Union Square. Reserve online and collect at 2 West 14th Street.',
      'h1': 'White sage', 'sub': 'Bundles, sticks and loose leaf for clearing a room.', 'filter': {'q': 'white sage'},
      'intro': '<p class="intro">White sage is the bundle most people picture for smudging. Small bundles suit a single room; larger wands last for many sessions. See <a href="/guide/how-to-smudge-a-room/">how to smudge a room</a>.</p>'},
     {'path': '/frankincense-myrrh/', 'title': 'Frankincense & Myrrh Resin and Incense in NYC | Namaste Incense Shop', 'desc': 'Frankincense and myrrh as resin tears, sticks and cones, with charcoal and censers, near Union Square.',
      'h1': 'Frankincense & myrrh', 'sub': 'The two oldest temple resins, as raw tears and as incense.', 'filter': {'q': 'frankincense|myrrh'},
      'intro': '<p class="intro">Raw tears need a lit charcoal tablet and a censer; sticks and cones light on their own. If you are buying tears for the first time, add <a href="/shop/charcoal-tools/">charcoal</a>.</p>'},
     {'path': '/copal/', 'title': 'Copal Resin & Copal Incense in NYC | Namaste Incense Shop', 'desc': 'Copal resin, copal sticks and cones near Union Square in Manhattan.', 'h1': 'Copal', 'sub': 'Bright, piney resin, as raw pieces and as incense.', 'filter': {'q': 'copal'}},
     {'path': '/chakra-candles/', 'title': 'Chakra Candles in NYC | Namaste Incense Shop', 'desc': 'Chakra candles and seven-color candle sets near Union Square, from makers such as Aloha Bay.', 'h1': 'Chakra candles', 'sub': 'Single colors and full sets of seven.', 'filter': {'q': 'chakra', 'aisle': ['candles', 'kits']}},
     {'path': '/reiki-candles/', 'title': 'Reiki & Herbal Ritual Candles in NYC | Namaste Incense Shop', 'desc': "Reiki-charged and herbal ritual candles, including Jen's Reiki Candles, near Union Square.", 'h1': 'Reiki & herbal candles', 'sub': 'Herb-dressed and Reiki-charged candles for the altar.', 'filter': {'q': r"reiki|herbal|jen'?s"}},
     {'path': '/smudge-kits/', 'title': 'Smudge Kits & Cleansing Kits in NYC | Namaste Incense Shop', 'desc': 'Ready-made smudge and cleansing kits with sage, palo santo and shells, near Union Square.', 'h1': 'Smudge kits', 'sub': 'Herbs, tools and instructions in one box.', 'filter': {'aisle': ['kits']}},
    ]

BRAND_TEXT = {
 'escential-essences': 'Hand-dipped sticks and one-inch cones made in the USA with cosmetic-grade oils, from the Escential Essences line represented by Matchless Gifts. The temple and frankincense blends suit the altar.',
 'wolf-spirit': 'An American sage house with harvesters in California and on the High Plains. Its range runs from bundled sage to natural resin incense, smudge sticks and smoke-free sprays.',
 'fred-soll': 'Hand-dipped in pinon and other resins in Tijeras, New Mexico, just east of Albuquerque. Lay each Resin on a Stick flat in a tray; one stick smolders for one to two and a half hours.',
 'swift-lite': 'The charcoal most resin burners reach for. Swift-Lite International in Ashford, Kent, has made it since 1957, originally for church incense, and the tablets catch within seconds.',
 'little-smudgies': 'Tiny soy smudge candles by Soul Sticks, sold by the dozen. Each one is set with herbs and a crystal on a lead-free wick and burns roughly four hours, right for a single short ritual.',
 'soul-sticks': 'Makers of masala and plant-based incense who also assemble smudge kits and intention kits.',
 'coventry-creations': 'A family- and woman-owned candle maker in Ferndale, Michigan (today Coventry Products), loved for its Blessed Herbal intention candles.',
 'good-karma': 'Intention candles from Zensual in Southern California: a soy blend, poured by hand in the USA into tins you can recycle.',
 'aloha-bay': 'Chakra candle makers in Lower Lake, California, pouring since 1993. They use RSPO certified palm wax and belong to the World Fair Trade Organization.',
 'jens': "Reiki candles listed under the Jen's Candles name. We share only what the listings show: browse the current candles, their prices and photos below.",
 'archangel-incense': 'Hand-dipped natural sticks from Jabou in Canada, twenty per pack, each blended for one archangel.',
 'prabhujis': "Incense rolled by hand in India's cottage industry and sold by Prabhuji's Gifts, a Green America certified business that packs in recycled cardboard.",
 'suns-eye': "A Central Florida maker of incense, oils and sprays.",
 'hem': 'Sage, copal and other cleansing blends from HEM Corporation of India, founded in 1983 by three Shah brothers.',
 'satya': 'From Shrinivas Sugandhalaya in Bangalore, the maker of the original Sai Baba Nag Champa. Here you will find its cleansing and protection-minded blends.',
 'sonavi': 'Sticks, bakhoor chips and beeswax candles from New Age Imports of Placentia, California.',
 'herb-earth': "Nippon Kodo's low-smoke bamboo-stick line in botanical scents, white sage and frankincense among them.",
 'morning-star': 'Nippon Kodo\'s thin Japanese sticks, gentle enough for a small altar room.',
 'auroshikha': 'Hand-rolled at an incense unit of the Sri Aurobindo Ashram in Pondicherry, working since 1973 and following IFRA fragrance guidelines.',
 'kamini': 'Natural masala sticks and cones from Kamini Aromatics in Bangalore.',
 'song-of-india': 'Run by R. Expo between India and Auburn, Washington, with a family perfumery history going back to Delhi in 1932.',
}
def brand_intro(S, k, st):
    name = S.BRAND_NAME[k]
    t = BRAND_TEXT.get(k) or f'The apothecary holds {st["n"]} piece{"s" if st["n"] != 1 else ""} from {name} right now; each is listed below with its live price.'
    shelves = ' and '.join(S.AISLES[a][0].lower() for a, _ in st['aisles'].most_common(2))
    return f'<p>{E(t)}</p><p>You will find {name} on our {E(shelves)} shelves, starting at {S.money(st["min"])}.' + (' Reserve online, then collect it at the counter on West 14th Street.' if st['pickup'] else ' Phone before you visit to make sure it is on the shelf.') + '</p>'
def brand_faq(S, k, st):
    name = S.BRAND_NAME[k]
    q = [(f'Is {name} sold near Union Square?', f'Yes. The Namaste Incense Shop apothecary at 2 West 14th Street has {st["n"]} {name} pieces in stock today.'),
         (f'What is the price range for {name}?', (f'Between {S.money(st["min"])} and {S.money(st["max"])} at the moment' if st['max'] > st['min'] else f'{S.money(st["min"])} apiece at the moment') + '; this page refreshes daily.')]
    if st['pickup']: q.append(('Can I collect it in person?', 'Choose Pickup when you check out and come by the counter at 2 West 14th Street during opening hours.'))
    return q
def BRAND_H1(S, k): return f'{S.BRAND_NAME[k]} at the apothecary'
def BRAND_TITLE(S, k, st): return f'{S.BRAND_NAME[k]} Ritual Supplies near Union Square | Namaste Incense Shop'
def BRAND_DESC(S, k, st): return f'{st["n"]} {S.BRAND_NAME[k]} piece{"s" if st["n"] != 1 else ""} from {S.money(st["min"])} at the Namaste Incense Shop apothecary, West 14th Street, NYC. Reserve and collect.'
def BRANDS_TITLE(S): return 'Ritual & Smudge Makers A to Z | Namaste Incense Shop'
def BRANDS_DESC(S): return 'Every sage, resin, charcoal and ritual candle maker stocked at the Namaste Incense Shop apothecary on West 14th Street.'
BRANDS_H1 = 'Makers A to Z'
def BRANDS_LEAD(S, n): return f'The apothecary currently stocks {n} named makers. Pick one to see each piece we hold and what it costs today.'

PAIR = {'smudge': ['burners', 'kits'], 'palo': ['burners'], 'resins': ['charcoal', 'burners'], 'incense': ['burners'], 'charcoal': ['resins'], 'burners': ['charcoal', 'smudge'], 'candles': ['smudge', 'palo'], 'kits': ['candles']}
PAIR_AISLE = True
REL_BRAND = 'Also by {brand}'
REL_SCENT = 'Similar {scent} pieces'
REL_PAIR = 'Complete the ritual'
REL_MORE = 'Elsewhere on the {aisle} shelf'
def describe(S, x):
    a = x['aisle']; t = E(x['title']); by = f' by {S.BRAND_NAME[x["brand"]]}' if x['brand'] else ''
    if a in ('smudge', 'palo'):
        s = [f'{t}{by} comes from our {AISLES[a][0].lower()} shelf.', 'To use it, hold the tip to a flame for a moment, blow it out, and let the smoke drift as you walk the room, catching embers in a shell or bowl. Snuff it in sand when you finish, and never leave it smoldering.']
    elif a == 'resins':
        s = [f'{t}{by} is a resin to melt over a lit charcoal tablet.', 'Bed a censer with sand, light the coal with tongs, wait for a gray skin of ash, then add resin a few grains at a time. Our <a href="/guide/charcoal-and-resin/">charcoal and resin guide</a> covers it in detail.']
    elif a == 'incense':
        s = [f'{t}{by} is ritual incense that lights directly, no coal needed.', 'Light the end, wait for a steady glow, and set it in a holder or tray of sand on a heat-proof surface. Stay with it while it burns.']
    elif a == 'charcoal':
        s = [f'{t}{by} belongs with the coals and tools.', 'Charcoal gets extremely hot. Hold it with tongs, rest it on sand or ash in a heat-proof vessel, and let it burn out completely before disposal.']
    elif a == 'burners':
        s = [f'{t}{by} is a vessel for smoldering herbs, resin or coal.', 'Fill it partly with sand or salt to buffer the heat and set it on a protected surface. Metal and ceramic vessels become hot to the touch.']
    elif a == 'kits':
        s = [f'{t}{by} gathers a ritual into one kit.', 'Read the included card or label first, light only what the ritual calls for, and keep a fire-safe dish close by.']
    else:
        s = [f'{t}{by} is an altar or ritual candle.', 'Trim the wick, set it on a fire-safe plate away from drafts, and keep it in sight while lit.']
    s.append('Collect it at 2 West 14th Street near Union Square or have it shipped from New York City; checkout is handled by Shopify on namastebookshop.com.')
    return s
def PRODUCT_DESC(S, x, v0): return f"{x['title']}, {S.money(v0['price'])}, at the Namaste Incense Shop apothecary on West 14th Street near Union Square. " + ('Reserve online and collect, or ship.' if x['pickup'] else 'Ships from NYC.')

def ABOUT_DESC(S): return 'About Namaste Incense Shop, the ritual and smudge apothecary at 2 West 14th Street near Union Square. A brand of Wealth Edge Ventures Inc.'
ABOUT_H1 = 'About the apothecary'
def ABOUT(S):
    return f'''<p class="lead">Namaste Incense Shop is the ritual side of our 14th Street counter: herbs for smudging, resins and the coals to burn them, censers, kits and candles for the altar.</p>
<p>We keep the focus narrow on purpose. If it is used to clear a space, mark an intention or scent a prayer, it belongs here; everyday stick incense lives at our sister site, <a href="https://namasteincense.com/">Namaste Incense</a>, and value packs at <a href="https://namasteincensestore.com/">Namaste Incense Store</a>.</p>
<h2>Where to find us</h2><p>{S.STORE_ADDR}, just west of Fifth Avenue. Phone <a href="tel:{S.TEL}">{S.PHONE}</a>.</p>{S.hours_html()}{S.visit_buttons()}
<h2>How ordering works</h2><p>{S.LEGAL} Payment, shipping and in-store pickup are handled by our Shopify store, <a href="{S.SHOP}" rel="noopener">namastebookshop.com</a>. Prices and stock on this site refresh every day from that store.</p>
<h2>Our shelves</h2><ul>{''.join(f'<li><a href="/shop/{AISLES[k][2]}/">{E(AISLES[k][0])}</a>: {E(AISLES[k][3])}</li>' for k in S.AISLE_KEYS)}</ul>
<h2>A note on safety and claims</h2><p>Smoke and flame need attention: use heat-proof vessels, ventilate the room and never walk away from something burning. Descriptions of traditional or spiritual uses are cultural information, not health advice.</p>'''
VISIT_TITLE = 'Visit the Smudge & Ritual Apothecary near Union Square'
def VISIT_DESC(S): return f'Hours, subway directions and pickup for Namaste Incense Shop at {S.STORE_ADDR}, a short walk west of Union Square.'
def VISIT_LEAD(S): return 'Come to the counter on West 14th Street to smell the sage and resin before you buy, or collect an order you reserved online.'
def FAQ_DESC(S): return 'Questions about smudging, palo santo, resin and charcoal, plus hours and pickup at the Namaste Incense Shop apothecary near Union Square.'
FAQ_H1 = 'Apothecary questions'
def FAQ(S):
    return [('Where is the apothecary?', f'Inside our shop at {S.STORE_ADDR}, on the south side of 14th Street just west of Fifth Avenue.'),
            ('When can I come in?', '11 AM to 8 PM Monday through Thursday, 11 AM to 9 PM Friday and Saturday, 11 AM to 7 PM Sunday. Call before holidays.'),
            ('How do I smudge a room?', 'Light the tip of a bundle, blow out the flame, and let the smoke move through the room while you catch embers in a bowl. The full method is in <a href="/guide/how-to-smudge-a-room/">how to smudge a room</a>.'),
            ('What do I need to burn frankincense or copal?', 'Resin tears, a charcoal tablet, tongs and a censer half-filled with sand. See <a href="/guide/charcoal-and-resin/">charcoal and resin, step by step</a>.'),
            ('How long does a palo santo stick last?', 'One stick can be relit many times; each lighting smolders for a short while before going out on its own. See <a href="/guide/palo-santo-basics/">palo santo basics</a>.'),
            ('Can I reserve online?', 'Yes. Pick Pickup at checkout and collect at the counter.' + (f' Orders are {S.READY.lower()}.' if S.READY else '')),
            ('Do you ship?', 'Yes, from New York City. Rates appear at checkout before you pay.'),
            ('Are spiritual uses guaranteed?', 'No. We describe traditional and spiritual uses as cultural information only; they are not promises or medical advice.')]

def GUIDES(S):
    return [
     {'path': '/guide/how-to-smudge-a-room/', 'title': 'How to Smudge a Room with Sage, Safely', 'desc': 'A calm, safety-first walkthrough for smudging a room or apartment with white sage or a herb bundle, from the apothecary near Union Square.', 'h1': 'How to smudge a room',
      'html': '''<p class="lead">Smudging means burning a bundle of dried herbs, most often sage, and letting the smoke move through a space. Here is a simple, careful way to do it in a city apartment.</p>
<h2>Gather</h2><ul><li>A bundle of <a href="/white-sage/">white sage</a> or another <a href="/shop/sage-smudge/">smudge herb</a>.</li><li>A fire-safe dish, shell or <a href="/shop/censers-bowls/">smudge bowl</a> with a little sand.</li><li>A lighter or candle, and an open window.</li></ul>
<h2>Steps</h2><ol><li>Crack a window so smoke has somewhere to go, and check smoke alarms will not be triggered by a short burst.</li><li>Hold the bundle at an angle and light the tip until it catches, then gently blow out the flame so the leaves smolder.</li><li>Carry the bowl under the bundle and move slowly from room to room, letting the smoke drift into corners.</li><li>Finish by pressing the lit end into sand or the bowl until no ember remains.</li></ol>
<h2>Care</h2><ul><li>Keep it away from curtains, pets and children, and never leave a smoldering bundle.</li><li>A little smoke goes a long way in a small room.</li></ul><p><a class="btn" href="/shop/sage-smudge/">Shop sage & smudge</a></p>'''},
     {'path': '/guide/palo-santo-basics/', 'title': 'Palo Santo Basics: How to Light and Store It', 'desc': 'How to light, use, put out and store palo santo sticks, with tips from the ritual apothecary on West 14th Street.', 'h1': 'Palo santo basics',
      'html': '''<p class="lead">Palo santo is a fragrant wood, usually sold as short sticks. Unlike a sage bundle, a stick goes out on its own after a short smolder, so it is easy to use in small doses.</p>
<h2>Lighting</h2><ol><li>Hold the stick at a 45-degree angle over a flame for 30 seconds or so.</li><li>Let it burn briefly, then blow it out; a thin ribbon of sweet smoke follows.</li><li>Wave it gently or rest it in a fire-safe bowl.</li></ol>
<h2>Putting it out and relighting</h2><p>It usually stops by itself within a minute or two. If not, press the tip into sand. Relight the same end next time.</p>
<h2>Storing</h2><p>Keep sticks in a dry, closed box away from sunlight so the wood keeps its scent.</p><p><a class="btn" href="/shop/palo-santo/">Shop palo santo</a></p>'''},
     {'path': '/guide/charcoal-and-resin/', 'title': 'Charcoal and Resin, Step by Step', 'desc': 'How to light incense charcoal and burn frankincense, myrrh, copal and other resins in a censer, explained by the ritual apothecary near Union Square.', 'h1': 'Charcoal and resin, step by step',
      'html': '''<p class="lead">Resin needs a coal. Once you have done it twice it takes under five minutes, and the room fills with the oldest incense there is.</p>
<h2>Your kit</h2><ul><li><a href="/shop/charcoal-tools/">Quick-light charcoal</a> and tongs.</li><li>A <a href="/shop/censers-bowls/">censer or bowl</a> half full of sand or salt.</li><li><a href="/shop/resins/">Resin</a>: frankincense, myrrh, copal or a blend.</li></ul>
<h2>Method</h2><ol><li>Grip one tablet with tongs and hold a flame to its edge until sparks run across it.</li><li>Lay it on the sand. Give it a few minutes to turn gray all over.</li><li>Drop on two or three grains of resin. When they melt away, add a few more.</li><li>Leave the coal to burn out completely in the censer; it stays hot long after the smoke stops.</li></ol>
<h2>Safety</h2><p>Work on a heat-proof surface with the window open, keep water away from hot ceramic, and never leave a lit coal.</p><p><a class="btn" href="/shop/resins/">Shop resins</a></p>'''},
     {'path': '/smudge-supplies-near-union-square/', 'title': 'Where to Find Smudge Supplies near Union Square & the East Village', 'store_ld': True,
      'desc': f'Sage, palo santo, resin and charcoal on West 14th Street, a short walk from Union Square, the East Village and Chelsea. Reserve online and collect.',
      'h1': 'Smudge and ritual supplies near Union Square', 'html': f'''<p class="lead">If you are hunting for sage, palo santo or frankincense in lower Manhattan, our apothecary counter is on 14th Street just west of Fifth Avenue.</p>
<h2>What is on the shelves</h2><ul><li>{S.cat_count["smudge"]} sage and smudge bundles and {S.cat_count["palo"]} palo santo pieces.</li><li>{S.cat_count["resins"]} resins and saps, with charcoal and tongs beside them.</li><li>Censers, smudge bowls, ritual kits and candles.</li></ul>
<h2>Coming from nearby</h2><ul><li><b>East Village:</b> the L train west to 14 St&ndash;Union Square, or the M14A/M14D along 14th Street.</li><li><b>Union Square:</b> a short walk west along the south side of 14th Street.</li><li><b>Chelsea and the West Village:</b> the 1, 2, 3, F or M to 14th Street, then walk east.</li><li><b>Midtown:</b> the N, Q, R or W south to Union Square.</li></ul>
{S.visit_block()}'''},
    ]
NOT_FOUND = 'This shelf is empty'
