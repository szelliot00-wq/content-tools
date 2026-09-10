# Scrape Literally Anything With Claude + SearchAPI

Video ID: `tIGEbk_4S6o`

## Summary
This video demonstrates how to use SearchAPI combined with an AI assistant (Claude) to scrape virtually any data from the web without building and maintaining custom scrapers. The presenter argues that DIY scraping at scale is a maintenance nightmare due to bot detection, JavaScript rendering, rate limits, and constantly changing website layouts. SearchAPI solves these problems by handling all the complex infrastructure under the hood, exposed via MCP (Model Context Protocol) so any AI agent can use it conversationally. The video culminates in a live build of a competitor ad intelligence dashboard for Gymshark that tracks Meta and Google ads across six competitors. Most relevant to marketers, growth operators, product managers, and founders who need competitive intelligence or web data without engineering resources.

---

## Key insights
- **DIY scraping breaks constantly**: Simple HTTP GET requests miss JavaScript-rendered content, and custom scrapers require ongoing maintenance every few days as sites update layouts, add CAPTCHAs, or change endpoints.
- **The seven core scraping problems SearchAPI solves**: JavaScript rendering, bot detection, CAPTCHA handling, rate limits, login-gated content, geo-blocks, and website versioning/A-B testing.
- **SearchAPI handles the full infrastructure stack**: Browser automation, CAPTCHA handling, session management, retries, storage, data parsing, monitoring, and proxy rotation — none of which you have to build or maintain yourself.
- **MCP integration makes it conversational**: By installing SearchAPI as a local MCP in Claude, you can scrape data using plain English prompts rather than writing any scraping code.
- **Fine-grained API key permissions**: SearchAPI lets you create integration tokens scoped to specific platforms (e.g., only Zillow + Airbnb, or only Meta Ads), which is useful for team environments where different services need different access levels.
- **Platform coverage is extremely broad**: Amazon, Google (Search, Ads, Flights, Hotels, Jobs), Meta Ads, YouTube, TikTok, Bing, DuckDuckGo, Airbnb, Zillow, eBay, TripAdvisor, GitHub, Gemini AI results, and many more.
- **Free tier available**: 100 free requests with no credit card required for new accounts.
- **Long-running ads signal profitability**: A heuristic from the presenter's ads agency background — brands only keep ads running for extended periods if they're profitable, so filtering for longest-running ads is a proxy for "what's working."
- **The dashboard built live tracked**: 243 active ads across 6 competitors (Lululemon, Nike, Under Armour, Young LA, Alphalete, Vuori), with 189 flagged as "likely winners" and 261 new creatives identified.
- **Dual interaction modes**: The dashboard provides a visual UI for browsing, but you can also query the scraped data conversationally inside Claude (e.g., "list Under Armour's top 3 longest-running active Meta ads").
- **Install MCP locally, not globally**: Scoping the MCP to a project folder keeps it from loading unnecessarily in unrelated Claude sessions, improving efficiency.

---

## Use cases
- **Paid media teams** monitoring competitor Google and Meta ad creative, copy, and longevity to inform their own campaign strategy without running every test themselves.
- **Growth marketers** at consumer brands who want to reverse-engineer what's working for competitors before spending budget.
- **E-commerce operators** tracking competitor pricing, stock availability, or product listings on Amazon or direct-to-consumer sites.
- **Travel or hospitality businesses** checking how they appear in AI-generated search overviews (e.g., Gemini's hotel recommendations) or scraping Google Hotels/Flights data.
- **Real estate professionals** pulling property listings (e.g., Miami homes listed 6+ months) from Zillow or Airbnb.
- **Researchers and analysts** who need recurring web data pulls without building and maintaining scrapers.
- **Recruiters or sales teams** using Google Jobs scraping to identify companies that are actively hiring in specific roles, then marketing to them.
- **Content or SEO teams** tracking what YouTube creators publish, how often, and what performs well.
- **Hotel/hospitality managers** checking which properties AI tools like Gemini recommend for their city.
- **Small teams or solo operators** who lack engineering bandwidth to build and maintain scraping infrastructure.

---

## Patterns & frameworks

**The "Scraping Maintenance Tax" argument**
The presenter's core mental model: DIY scraping has a hidden ongoing cost. It appears cheap on day one but generates compounding maintenance work (layout changes, new CAPTCHAs, endpoint shifts, full site rebuilds). The recommendation is to treat scraping infrastructure as a managed service cost rather than an engineering problem to solve yourself — the time and money saved outweigh the subscription cost.

**Work-backwards dashboard design**
When building a competitor intelligence dashboard, the presenter recommends starting from the business question, not the data: (1) Identify who your competitors are, (2) Determine how they acquire customers (ads, email, offers, etc.), (3) Define the specific signals worth tracking, (4) Then instruct the AI to use SearchAPI to gather exactly those signals. This prevents over-engineering and keeps the data collection purposeful.

**Long-running ad = likely winner heuristic**
A repeatable filter from agency practice: sort competitor ads by duration. Ads that have been running for weeks or months are almost certainly profitable — brands kill losing ads quickly. This turns ad longevity into a low-effort proxy metric for creative effectiveness, without needing access to the competitor's internal data.

**MCP as the AI-to-API bridge**
The technical pattern: install a service's MCP endpoint locally in your AI tool's project folder → authenticate with a scoped API token → interact with external APIs via natural language. This pattern is reusable across any MCP-compatible service and any MCP-compatible AI agent (Claude, ChatGPT, Grok, etc.), making it a general-purpose workflow for AI-augmented data gathering.