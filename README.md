# namasteincenseshop.com

Static storefront built daily from the public namastebookshop.com catalog and deployed to GitHub Pages.
A brand of Wealth Edge Ventures Inc.

- `site/config.json`: site settings. Set `REVIEW_URL` (Google review link) to show the "Review us on Google" button and QR code; set `GOOGLE_SITE_VERIFICATION` to the Search Console HTML-tag value. Both stay hidden while empty.
- `site/sitecopy.py`: aisles, product mix and all copy for this site.
- `scripts/`: shared engine (fetch, pickup, best sellers, build).

Run the regression checks before publishing (also run by the daily deployment):

```sh
python3 -m unittest discover -s tests -p 'test_*.py'
node --test tests/cart.test.cjs
```

See [visitor and order attribution](docs/attribution.md) for the existing analytics,
the Bookshop handoff markers, and the evidence needed to confirm an order's source.
