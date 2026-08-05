# What Are Large Database Models? AI for SQL Data

Video ID: `uU1EP9_4qBU`

## Summary
The video introduces Large Database Models (LDMs), a new category of AI model trained directly on relational database tables rather than text. Unlike LLMs, LDMs learn vector representations of structured data (rows and columns), enabling semantic SQL queries — such as finding similar customers — without hand-crafting filter conditions. The presenter walks through the five-step training process and highlights real-world use cases across insurance, fraud detection, and retail.

## Key insights
- **99% of enterprise data lives in relational databases**, never reaching an LLM — LDMs are designed to unlock that data in place, without extracting or moving it.
- **LDM queries replace rigid SQL filters with semantic similarity.** Instead of guessing which columns matter (age, city, spend), the model learns which values co-occur across all selected columns and finds similar rows automatically.
- **Numeric values are binned before tokenization.** Clustering numerically close values into buckets (e.g., ages 35–39 → B7) prevents the model from treating 37 and 38 as unrelated tokens, and handles rare continuous values that would otherwise be under-represented.
- **Each row is treated as an unordered "bag of words" sentence.** Every token is a column-name + value pair, so identical strings in different columns (e.g., "New York" in a city vs. region column) are kept distinct.
- **The trained model is loaded back into the database**, so queries run as standard SQL against data that never leaves its secured environment — addressing both cost and compliance concerns.
- **LDM queries can combine semantic search with standard SQL clauses** (e.g., find similar customers AND filter by country), giving the flexibility of AI alongside the precision of traditional SQL.
- **Supported query types include** similarity, anomaly detection (dissimilarity), clustering, analogy, and commonality — all expressible in SQL.
- **IBM's DB2 for z/OS shipped the first commercial LDM product in 2022** (SQL Data Insights), with a 2026 Pro version adding support for unstructured text and incremental model refresh.
- **No data scientist required for queries** — anyone who can write basic SQL can ask semantic questions directly, removing a major bottleneck in data analysis workflows.