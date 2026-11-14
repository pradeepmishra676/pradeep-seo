# Schema module

1. Detect: list the JSON-LD types page_check found (also check microdata mentions if the user pasted HTML).
2. Match the type to the page: Article/BlogPosting for posts, Product (with offers) for products, LocalBusiness for a business page, FAQPage only if real visible FAQs exist, BreadcrumbList for hierarchical pages, Organization/WebSite on the home page.
3. Validate: required and recommended properties present, values match the visible content, correct formats (ISO dates, absolute URLs), valid JSON.
4. Generate: when asked, produce JSON-LD in a code block using only facts the user gave or the page shows. Leave clearly marked placeholders for anything unknown; never invent ratings, reviews, prices or addresses.
5. Tell the user to test the final markup in Google's Rich Results Test and Schema Markup Validator; do not claim a rich result is guaranteed.
