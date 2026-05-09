# AI is eating your traffic. Here's what to do about it — Prathik Roy (Springer Nature)

Video ID: `Mt1E4LTU37U`

## Summary
This episode of the Product Experience podcast features Pratik Roy, Product Director for Data and AI Solutions at Springer Nature, one of the world's largest academic publishing companies. The conversation explores how AI is fundamentally disrupting traditional content publishing business models — particularly in scientific publishing — by shifting value from direct content consumption to synthesized outputs. Pratik argues that publishers must rethink their metrics, monetization strategies, content structure, and IP management to survive and thrive in an AI-driven world. The episode is most relevant to product managers, editors, and business leaders working in content, publishing, media, or any IP-rich industry navigating the transition from SaaS to Data-as-a-Service (DaaS) models.

---

## Key Insights

- **The "ChatGPT moment" broke traditional publishing metrics.** For ~20 years, publishing value was measured by visible user behaviors: clicks, page views, PDF downloads, scroll depth, session time, unique visitors, and article downloads. AI has made these metrics increasingly unreliable because users no longer need to visit the source.

- **Value has shifted from full-text consumption to synthesized output.** A scientist using an AI research assistant can read 300 papers and get a synthesis without ever opening a single PDF from a publisher's site. Similarly, news consumers can get summaries from OpenAI or Google without visiting the New York Times or Washington Post.

- **Scientific content has unique characteristics that make it especially valuable to AI.** With ~8 million scientific users worldwide, the market is small but the content is extremely high quality — peer-reviewed, validated, and highly cited. AI developers (from large players like DeepMind to niche cancer research startups) are actively seeking this data to train models.

- **Citation count is the traditional value signal in scientific publishing,** but AI systems risk over-indexing on popular/sensationalist papers while ignoring foundational research that might win Nobel Prizes decades later — creating a new kind of bias risk.

- **Disintermediation is real.** Platforms like Open Evidence (a heavily VC-funded medical AI startup) use scientific content as their underlying evidence base, meaning users never interact with the original publisher's platform. This mirrors what OpenAI and Google are doing to news media.

- **The content monetization model is shifting from ads and subscriptions to Data-as-a-Service (DaaS).** Three emerging models are identified:
  - **Usage-based / token-based pricing:** Content delivered via APIs, MCP servers, and agentic protocols, charged by consumption.
  - **Outcome-based pricing:** Revenue tied to the value generated — e.g., if a publisher's data helps a pharma company save $10M and cut drug development from 10 years to 2, a bonus payment or revenue share is triggered.
  - **Licensing deals:** Like News Corp's reported ~$250M/5-year deal with an AI company; scientific publishing deals are expected to be even larger given the higher content value.

- **AI systems are restructuring what "good content" looks like.** AI developers are asking publishers to restructure articles with bullet points and Q&A formats so the content is easier to ingest — essentially asking authors to pre-summarize their own work before the AI summarizes it. Pratik found this both amusing and telling.

- **Content optimization for AI has two levels:**
  - **Article level:** Titles, SEO/GEO tags, metadata, altmetrics tracking, and now structural changes (bullet points, Q&A sections).
  - **Systems level:** Building pipelines that track how content flows into AI systems — RAG inference, fine-tuning, MCP servers — and measuring how often the content is used to generate outputs.

- **IP and rights management is now a core product management responsibility.** Pratik jokes he's gone from scientist to product manager to "half a lawyer." Key concepts:
  - **Rights In:** Understand what agreements you have with original content creators and what use cases are permitted.
  - **Rights Out:** Be explicit in user agreements about what licensees can and cannot do with the data. Example: music AI company Suno licensing from Universal/Sony but being restricted from distributing AI-generated music outside their platform.
  - The "prohibited section" of an agreement should be longer than the "permitted" section if you're doing it right.

- **The user interface itself is disappearing.** Publishers must now think about building for "humans consuming content via machines" rather than humans directly on their platforms. This requires an entirely new set of metrics and infrastructure.

- **New metrics framework for AI-age product managers:**
  - **Technical PMs:** Build pipelines to track content flow into AI systems; measure how often content is pinged during inference; track RAG usage.
  - **Product PMs:** Measure what percentage of AI-generated answers are derived from your content; track attribution clicks that bring users back to your platform; monitor session time on referred traffic.
  - **Growth/Monetization PMs:** Design token-based or outcome-based pricing; consider giving tokens back to users when outputs are unsatisfactory to maintain flywheel engagement.

- **Token-back pricing as a retention mechanic:** Pratik suggests that AI platforms should return a portion of tokens to users when outputs are poor (e.g., returning 5 tokens when a regenerated image still falls short), keeping users in the system rather than churning due to token depletion.

- **Scientific publishers were initially caught off guard by generative AI in 2023** and shifted to a more proactive stance in 2024–25, beginning to structure licensing deals with big tech and niche AI developers that share values around attribution and quality.

- **The tobacco industry example** is cited as a cautionary tale about how funding and incentives can corrupt scientific content — underscoring why trust, attribution, and source verification are non-negotiable in scientific AI applications.

- **High stakes of scientific AI errors:** Getting a restaurant recommendation wrong means bad pasta. Getting a drug dosage wrong due to a hallucinated or biased AI output could be catastrophic — making content quality and attribution critical.

---

## Use Cases

- **Product managers in publishing or media** who need to rethink their KPIs and business models in an AI-disintermediated world.
- **Technical product managers** building data pipelines and APIs to deliver content to AI systems and measure downstream usage.
- **Growth and monetization PMs** designing usage-based, token-based, or outcome-based pricing models for data products.
- **Content strategists and editors** who need to restructure article formats (bullet points, Q&A, structured metadata) to optimize for AI ingestion.
- **Legal/product teams** managing IP rights, licensing agreements, and data-as-a-service contracts — especially rights-in and rights-out frameworks.
- **Executives at IP-rich companies** (scientific publishers, news organizations, music labels, podcasts) exploring licensing deals with AI companies.
- **AI developers and LLM builders** seeking to understand how to partner with content owners for high-quality, validated training data.
- **Product leaders in healthcare or pharma tech** building clinical AI tools who need to ensure content attribution and accuracy to avoid dangerous errors.
- **Podcast producers and media companies** looking to extract and license value from their content archives.
- **Entrepreneurs building niche/small language models** (e.g., cancer research LLMs) who need to understand the content licensing landscape.

---

## Patterns & Frameworks

### 1. **SaaS → DaaS Mindset Shift**
- **What it is:** A fundamental reframing from Software-as-a-Service (where users interact with a platform) to Data-as-a-Service (where content is consumed by machines on behalf of humans).
- **How it works:** Instead of measuring page views and subscriptions, you measure API calls, token consumption, inference usage, and outcome-based value delivered. Pricing shifts from flat subscriptions to usage-based or outcome-based models.

### 2. **Rights In / Rights Out Framework**
- **What it is:** A two-sided IP management model for understanding and controlling how content flows through your product ecosystem.
- **How it works:** "Rights In" = audit what agreements you have with original content creators and what use cases are permitted under those agreements. "Rights Out" = define explicitly in your licensing agreements what downstream users (e.g., AI developers) can and cannot do with your data. The prohibited section should be longer than the permitted section.

### 3. **Three-Layer Metrics Framework for AI-Age PMs**
- **What it is:** A role-specific approach to measuring content value in AI-mediated environments.
- **How it works:**
  - *Technical PMs* → build infrastructure to track content flow (RAG, fine-tuning, MCP, agentic protocols) and ping frequency.
  - *Product PMs* → measure answer attribution rates, referral click-through back to source, and session engagement on attributed visits.
  - *Growth/Monetization PMs* → design token pricing, revenue share, and outcome-based bonus structures.

### 4. **Outcome-Based Pricing Model**
- **What it is:** A monetization structure where payment is tied to the measurable business value generated using your data.
- **How it works:** Establish a baseline guaranteed fee (e.g., $500K) plus a success bonus (e.g., $2M) if the licensee achieves a defined outcome (e.g., cutting drug development time from 10 years to 2 years using your content). Requires upfront agreement on how outcomes are measured and attributed.

### 5. **Token-Back Retention Mechanic**
- **What it is:** A product design pattern for AI platforms to reduce churn caused by token depletion.
- **How it works:** When a user regenerates a prompt and the output is still unsatisfactory, the platform refunds a portion of the tokens consumed (e.g., refunding 5 of 10 tokens). This keeps users in the system, maintains goodwill, and sustains the engagement flywheel.

### 6. **Content Structuring for AI Ingestion (Two Swim Lanes)**
- **What it is:** A dual-track approach to making content machine-readable.
- **How it works:**
  - *Metadata/SEO lane:* Optimize titles, abstracts, keywords, GEO tags, and structured metadata so AI crawlers can discover and prioritize content.
  - *Structural/format lane:* Reformat the body of content itself — replacing dense prose with bullet points and adding Q&A sections — so AI models can ingest and synthesize more efficiently without needing to parse complex academic prose.

### 7. **The "Garbage In, Garbage Out" Quality Gate (Schrödinger's Box Metaphor)**
- **What it is:** A mental model for understanding why content quality is the primary lever for AI output quality.
- **How it works:** The AI model is the "unknown box." If you can control and validate what goes in (peer-reviewed, attributed, unbiased content), you can trust what comes out. Poor or biased inputs produce unreliable or dangerous outputs — especially critical in medical or scientific AI applications.