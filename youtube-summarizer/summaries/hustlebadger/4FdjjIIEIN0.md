# Intro to A/B testing

Video ID: `4FdjjIIEIN0`

## Summary
This video provides a detailed introduction to A/B testing for product managers, explaining its purpose, methodology, and limitations. Ed from HustleBadger outlines why companies like Booking.com use A/B tests to validate product changes and enable safe, rapid code deployment. He then presents a four-step framework for running an A/B test, covering metric selection, hypothesis formulation, experiment design, and result interpretation. The video also critically examines the downsides of A/B testing, such as cost and the risk of incremental thinking, and offers alternative quantitative and qualitative research methods, making it relevant for product managers across various company stages and contexts.

## Key insights
-   **Purpose of A/B testing**: Primarily used to validate that product changes (new features, streamlined experiences) have the expected behavioral and commercial impact. It also enables quick and safe deployment of new code by allowing features to be toggled on/off or traffic to be split rapidly.
-   **Definition of an A/B test**: It's a statistical method comparing a "control" (existing experience) with a "variant" (new feature) by splitting traffic (typically 50/50) and measuring success metrics (e.g., conversion rate) to determine if observed differences are statistically significant and not due to chance.
-   **Characteristics of a good success metric**: Metrics should be 1) **Intuitive** for easy understanding and communication, 2) **Measurable** with reliable and clean data, 3) **Actionable** enough to drive decisions (roll out or roll back), and 4) **Influenceable** by the team's actions, ensuring changes are attributable to the experiment.
-   **Experiment Design Variables**:
    -   **Confidence Level**: The probability a result is real (e.g., 95% means 1 in 20 results could be by chance).
    -   **Sample Size**: The number of users seeing the test, often thousands to millions; A/B testing is not suitable for low-traffic scenarios (tens or hundreds of users).
    -   **Runtime**: How long the test needs to run, typically 2-6 weeks, to collect sufficient data and account for weekly seasonality. Running too short (e.g., 2 days) can lead to skewed results, even if statistical significance is met.
    -   **Expected Result**: The anticipated difference between variant and control; smaller expected differences require larger samples and longer runtimes.
-   **Interpreting Results**: Outcomes can be **Positive** (statistically significant improvement, leading to rollout and doubling down on the hypothesis), **Inconclusive** (no significant difference, indicating the hypothesis was less important than thought), or **Negative** (statistically significant negative impact, leading to rollback and re-evaluation of assumptions).
-   **Downsides of A/B Testing**:
    -   **Costly**: Involves setting up testing platforms, building duplicate functionality, and clean-up.
    -   **Opportunity Cost**: Delays feature rollout, losing potential positive impact during the test period.
    -   **Incremental Thinking**: Can lead to optimizing for local maxima, hindering radical innovation that might initially perform poorly but lead to greater long-term gains (as highlighted by Brian Chesky of Airbnb).
    -   **False Confidence**: Multiple small A/B test wins often don't compound linearly due to "conservation of intent" (limited user intent to purchase) and "user sensitivity to change" (initial uplifts tail off over time as users adapt).

## Use cases
-   **Validating Product Changes**: When you want to ensure a new feature or experience genuinely drives expected user behavior or commercial impact.
-   **Safe Code Deployment**: For quickly and safely rolling out new features by gradually exposing them to a segment of users.
-   **Large User Bases**: Ideal for companies with high website traffic (at least 10,000 users) that can generate statistically significant results quickly.
-   **Data-Driven Cultures**: When internal stakeholders value quantitative data and statistical evidence to support product decisions.
-   **High-Risk Changes**: When making changes with potentially significant negative impact, such as pricing adjustments, login flows, or onboarding experiences, where destroying value is a concern.
-   **Established Companies**: Where the A/B testing infrastructure is already in place, making it cost-effective to run subsequent tests.
-   **When Alternatives are Expensive**: For large consumer companies, where recruiting representative samples for qualitative research can be time-consuming and costly.
-   **Startups or Low-Traffic Products**: A/B testing is *not* suitable due to insufficient sample sizes; qualitative methods or simpler quantitative analysis are better.
-   **Design/Sales-Led Cultures**: A/B testing might be less impactful if statistical results are often discounted in favor of other types of insights.

## Patterns & frameworks
-   **Four Basic Steps to Run an A/B Test**:
    1.  **Picking a Success Metric**: Proactively identify the primary quantitative measure to improve, ensuring it is intuitive, measurable, actionable, and influenceable.
    2.  **Strong Hypothesis**: Formulate a clear, testable statement predicting how a specific product change will affect user behavior and the chosen success metric.
    3.  **Design the Experiment**: Determine the confidence level, required sample size, and optimal runtime (ideally 2-6 weeks) based on expected results and traffic.
    4.  **Run and Interpret**: Launch the test, monitor its progress (e.g., typically with a 50/50 traffic split), and categorize results as positive, inconclusive, or negative to inform subsequent actions.
-   **Good Hypothesis Template**: "Based on evidence, we believe [the change we will make] will encourage [a certain type of user] to behave in [a certain type of way]. We will know this to be true when [our metric] increases/decreases (by an estimated amount)."
-   **Characteristics of a Good Metric Framework**: A four-point checklist for evaluating the suitability of a metric: Is it intuitive, measurable, actionable, and influenceable/controlled?
-   **Result Interpretation Framework (Positive, Inconclusive, Negative)**: A model for categorizing A/B test outcomes and guiding follow-up actions:
    -   **Positive**: Roll out, double down on hypothesis.
    -   **Inconclusive**: Re-evaluate hypothesis, explore other user needs.
    -   **Negative**: Roll back, understand *why* the impact was negative (e.g., "good friction").
-   **Conservation of Intent**: A concept explaining why cumulative gains from multiple A/B tests often fall short of simple addition, suggesting a fundamental limit to how much user behavior can be altered by small optimizations.
-   **User Sensitivity to Change**: The pattern where the initial positive impact of a new feature tends to decrease over time as users become accustomed to it, and it becomes the new baseline.