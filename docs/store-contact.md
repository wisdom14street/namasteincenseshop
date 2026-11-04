# Store contact source

The incense counter is inside Namaste Bookshop at 2 West 14th Street. Its
customer-facing phone is **212-645-0141** (`tel:+12126450141`).

Verified on 2026-11-04 against three first-party pages:

- [Bookshop contact page](https://namastebookshop.com/pages/contact)
- [Bookshop contact policy](https://namastebookshop.com/policies/contact-information)
- [Bookshop visit page](https://namastebookshop.com/pages/visit-namaste-bookshop-nyc)

A read-only Shopify location check also returned `+12126450141` for the active
Bookshop location at 2 West 14th Street. The previously used `646-876-1401`
belongs to the separate Crystalshop location in Shopify; its current call
routing was not tested.

The shared `PHONE` and `TEL` constants in `scripts/build.py` supply displayed
numbers, call links, store structured data, and `llms.txt`. Keep these aligned
with the Bookshop's published customer contact. This change does not alter
Shopify location settings or other storefront repositories.
