# ProductTank Auckland - SaaS math with Shing

Video ID: `Vth0oVMwePQ`

## Summary
Paul Shingles (Shing), COO at Aura and operating partner at MOVAC, walks through the core financial metrics that define SaaS businesses, why they differ from brick-and-mortar measurement, and how product teams can directly influence them. The central argument is that SaaS businesses are counterintuitively measured by growth and efficiency metrics rather than profitability, because the subscription model generates compounding revenue that eventually eclipses traditional business models — but only if spend is efficient. The talk is most relevant to product managers, product leaders, and anyone working in or around a SaaS business who wants to understand how their work connects to business outcomes.

## Key insights
- **SaaS vs. brick-and-mortar financials are fundamentally different**: A widget sold for $100 upfront generates immediate revenue; the same widget sold as a $10/month subscription generates compounding revenue over time. A SaaS business acquiring 10 customers/month at 12× CAC looks terrible early on but eclipses the brick-and-mortar model over a long enough timeline — this is the core rationale for the entire SaaS model.
- **The J-curve / burn trough is intentional**: The faster you grow, the deeper the trough but the steeper the exit curve into profitability. Xero is cited as a prime example — massive early spend, dramatic acceleration into profitability. Measuring SaaS by EBITDA or traditional profit metrics during the burn phase is misleading and inappropriate.
- **Customer stock = inventory**: In SaaS, your customer base is the equivalent of a retailer's inventory — it represents future earning potential. Growing your customer base is growing the asset, not just growing revenue.
- **ARPO (Average Revenue Per Unit/Customer) is a critical product metric**: Calculated as recurring revenue ÷ number of recurring-revenue-generating customers. One-off fees, onboarding charges, and merch do not count. Product teams should think of ARPO as a direct measure of the value their features unlock — new features should move customers to higher-tier plans, lifting ARPO.
- **ARPO is extremely hard to move because of backbook drag**: Example given: 1,000 customers at $150/month = $150,000 MRR. Signing 10 new customers at $300/month moves the blended ARPO only to ~$151. Front-book vs. back-book distinction is critical — demonstrate ARPO gains on new customers separately if the overall number won't move meaningfully yet.
- **ARR/MRR is simple but critical**: MRR = customer count × ARPO. ARR = MRR × 12. Only include recurring revenue. Professional services, onboarding, and one-off sales pollute the metric and make the business look better than it structurally is.
- **ACMR (Annualized Committed Monthly Revenue)** is a useful variant when contracts are signed but revenue hasn't started flowing yet — accounts for timing gaps in implementation. Only use it if churn through the implementation phase is low. Pushpay example: when 45-day onboarding had 25% drop-off, they excluded pipeline customers; after cutting it to 2 days with 100% conversion, they included them.
- **Two types of churn — logo churn vs. revenue churn**: Logo churn = customers canceled ÷ opening customer count. Revenue churn = revenue lost from canceled customers ÷ opening revenue. Revenue churn is more informative because it reveals whether you're losing high-value or low-value customers. Losing small/legacy customers may be intentional; losing top accounts is a crisis even if logo churn looks fine.
- **Good churn benchmarks**: Consumer businesses will always churn higher than enterprise. Enterprise customers make platform decisions on 3–5 year cycles; consumers decide in 3–5 days. Sub-5% annual logo churn is generally good for B2B SaaS.
- **Negative churn is the holy grail**: When expansion revenue from retained customers exceeds lost revenue from churned customers, your backbook grows on its own. This means every new customer you acquire is additive on top of an already-growing base.
- **CAC (Customer Acquisition Cost)** = total sales + marketing + implementation costs ÷ new customers acquired. Consider spreading over 3–6 months for businesses with lumpy spend or long sales cycles. On its own, CAC is meaningless — "$1,000 CAC — is that good or bad?" requires context.
- **LTV (Lifetime Value)** = (ARPO × gross margin) ÷ logo churn rate. This is the proper formula — gross margin must be included, not just revenue. Dividing LTV by CAC gives the LTV:CAC ratio.
- **LTV:CAC ratio — the magic number is 3**: Above 3 = find more ways to invest, spend more, grow faster. Below 3 = improve efficiency before spending more. This is the primary efficiency gate for SaaS investment decisions.
- **CAC Months (payback period)**: CAC ÷ ARPO = how many months to recoup acquisition cost in raw revenue terms. Good = ≤12 months. CAC Payback (including gross margin) = CAC ÷ (ARPO × gross margin). Good = ≤15–18 months. Consumer businesses may need a tighter threshold (e.g., 4 months) due to higher churn.
- **Rough CAC allocation for inbound B2B SaaS**: Marketing ~5–6 months of CAC, Sales ~4–5 months, Implementation ~1–2 months. Enterprise businesses naturally skew heavier toward sales.
- **Sales conversion rates are contextual**: High conversion rate may mean the funnel is too narrow (not enough leads). Low conversion rate may mean poor ICP targeting or underperforming sales team. Cohort-based conversion analysis is recommended to account for multi-month sales cycles — track what % of a given month's leads convert over subsequent months.
- **Sales velocity formula**: (Number of opportunities × ARPO × win rate) ÷ length of sales cycle. The goal is to minimize sales cycle length while maintaining win rate.
- **Gross margin for SaaS should be 70–80%**: Direct costs include hosting, payment processing fees, support, DevOps (judgment call), and post-implementation customer success. Onboarding/implementation goes into CAC, not COGS. Payments businesses run 15–40% margin due to interchange costs. Pushpay blended example: payments (⅔ of revenue) at ~35% margin + SaaS (⅓ of revenue) at ~80% margin.
- **Gross margin directly impacts LTV, payback period, and free cash flow runway**: Higher margin = steeper acceleration curve = longer runway between raises.
- **Net Revenue Retention (NRR)**: (Opening MRR + expansions − churn − contractions) ÷ opening MRR. Target >100%. At 115% NRR, your existing customer base is generating 15% more revenue this month than last, meaning you need 15% fewer new customers just to hit the same growth target.
- **GRR (Gross Revenue Retention)** strips out expansion revenue entirely and only looks at downgrades and churn — used as an imperfect proxy for product-market fit. If customers are leaving or downgrading at high rates, the value-price equation is broken.
- **Discounting treatment**: Discounts lasting longer than one contract term should reduce reported ARPO. Short-term discounts (e.g., 3 months free) should be treated as cost of acquisition, with full contract revenue booked.
- **On AI and SaaS**: SaaS is not going away, but the definition of what makes a SaaS business must evolve. Teams must ship faster, be AI-forward, and deliver what customers would otherwise build internally. Teams that don't get on the AI product journey will become irrelevant.
- **On pricing**: Price testing is underused and less scary than it seems. For high-volume B2C, A/B test pricing directly. For low-volume enterprise, test in quotes — just raise by 10% and see what happens. Six months of formal research can be replaced by running real experiments.
- **Metrics ownership**: Ultimately sits with finance, but product leaders should be asking for these metrics proactively if they aren't being reported. Leading indicators for product teams: login rates, MAU/DAU, feature adoption, customer penetration (e.g., % of a retailer's stores actively using the platform).

## Use cases
- **Product managers building a business case for their roadmap**: Use ARPO movement and NRR to demonstrate ROI of feature investment.
- **Early-stage SaaS founders deciding what to measure**: The CAC/LTV/ARPO/NRR framework provides a complete picture of business health that revenue alone cannot.
- **Product leaders responding to "is engineering investment worth it?"**: Tie new features to tier upgrades, ARPO improvement, reduced churn, and shorter sales cycles.
- **SaaS businesses deciding whether to raise and spend more**: LTV:CAC >3 and CAC Months <12 are the green lights for accelerating spend.
- **Businesses experiencing growth that doesn't feel efficient**: Use the LTV:CAC and CAC payback period to diagnose whether the problem is acquisition cost, pricing, churn, or gross margin.
- **Companies with payments + subscription revenue** needing to understand blended gross margin and how to report it to investors.
- **Sales and marketing teams being asked to improve efficiency**: The breakdown of CAC into marketing / sales / implementation ratios gives a diagnostic starting point.
- **Businesses with long enterprise sales cycles**: Cohort-based conversion tracking resolves the temporal mismatch between when leads enter and when they close.
- **SaaS businesses considering annual vs. monthly subscription structures**: Annual contracts reduce churn signal but lock in customers; monthly contracts give faster product feedback.
- **Finance and data teams defining what counts as recurring revenue**: The talk provides clear rules (exclude onboarding, one-offs, merch; include payments if they behave like subscription revenue).

## Patterns & frameworks

**The SaaS J-Curve / Burn-to-Accelerate Model**
The foundational model of the talk. SaaS businesses intentionally spend more than they earn early (CAC > near-term revenue per customer) to build a compounding subscription base. The trough of the curve deepens with growth rate, but so does the steepness of the exit into profitability. The key insight: measure efficiency of spend, not profitability of the period.

**Backbook vs. Front Book**
A mental model for understanding pricing and metric impact. Backbook = all customers signed before today. Front book = all customers signed from tomorrow. Changes to pricing or product primarily affect the front book; the backbook creates inertia that makes metrics like ARPO slow to move. Used to set realistic expectations for how fast product investments will show up in blended numbers.

**LTV:CAC Ratio (the "3x rule")**
LTV = (ARPO × gross margin) ÷ churn rate. LTV ÷ CAC = efficiency ratio. Below 3: fix efficiency before spending more. Above 3: invest aggressively in growth. The primary decision gate for SaaS investment allocation.

**CAC Payback Period (CAC Months)**
Two variants: raw CAC ÷ ARPO (revenue payback, good ≤12 months) and CAC ÷ (ARPO × gross margin) (profit payback, good ≤15–18 months). A simpler, more intuitive companion to LTV:CAC that answers "how long until I get my money back?"

**CAC Component Ratio (inbound B2B benchmark)**
Marketing: 5–6 months of CAC. Sales: 4–5 months. Implementation: 1–2 months. Used to diagnose which part of acquisition spend is out of proportion.

**"Would you turn it off?" CAC inclusion rule**
Attributed to Rowan Simpson. When debating what counts as CAC: ask "if we stopped acquiring new customers today, would we turn off this spend?" If yes, it's CAC. Cuts through debates about building leases, Salesforce licenses, etc.

**Cohort-Based Conversion Tracking**
Instead of measuring conversion rate as deals closed this month ÷ leads this month (which is distorted by sales cycle length), track what % of a given month's lead cohort converts over subsequent months. Reveals true conversion rate and enables pipeline forecasting. Named-account view is used as an alternative for very-low-volume enterprise pipelines.

**NRR as a Growth Multiplier**
NRR > 100% means the existing customer base is self-growing — expansion revenue from upgrades and add-ons outpaces churn and contractions. This reduces the volume of new customers required to hit growth targets each month, compounding the efficiency of every new customer acquired.

**GRR as a Product-Market Fit Signal**
Gross Revenue Retention removes expansion revenue and only tracks losses (churn + downgrades). Used by investors as an imperfect but useful proxy for whether the core product is delivering enough value to justify the price — regardless of upsell performance.

**Leading vs. Lagging Indicator Split**
Lagging: ARR, MRR, ARPO, CAC, NRR — reflect what happened last month. Leading (product lens): MAU/DAU, feature adoption, customer penetration rate (% of potential users/sites active). Leading (sales lens): pipeline size, activity metrics, best-case and base-case close forecasts. Both are needed to manage the business proactively rather than reactively.