# How AI Agents, LLMs & APIs Use Real-Time Data at the US Open

Video ID: `F3hlZSZc6UI`

## Summary
This video uses IBM's AI-powered serve analysis system at the 2026 US Open as a hands-on example to explain how LLMs, APIs, and AI agents work together. The core argument is that LLMs alone are limited by stale training data and poor numerical processing, so specialized backend services handle the heavy computation while APIs act as the handoff point to the model. The video walks through the full pipeline — from courtside cameras tracking 21 body joints at 50Hz, to structured scores, to an agent loop that retrieves and reasons over that data to answer a fan's natural-language question.

## Key insights
- **LLMs have a staleness problem**: A model trained on historical tennis data cannot tell you how a player is serving *right now* — real-time data must be injected via APIs or context-window grounding.
- **Raw data is the wrong interface for LLMs**: 3,000+ numbers per second of play would fill a context window with bulk coordinates that an LLM (a next-token predictor) is poorly suited to crunch. Specialized services compress this into a few kilobytes of structured, meaningful scores before the model ever sees it.
- **Divide labor by strength**: Specialized backend services measure and compute (biomechanics, joint angles, serve speed zones); the LLM's job is narrowly to reason over the results and produce a human-readable answer — a task it excels at.
- **APIs are the architectural seam**: The API is where the handoff between the specialized compute layer and the reasoning layer happens. It abstracts all the complexity of the camera pipeline into a clean, callable interface.
- **Agents are models + tools + a goal**: When a fan asks a question, an agent is invoked with a list of tool definitions (name, description, parameters). The model decides which tool to call, the harness executes the API call, and the result is fed back into context — looping until the model has enough information to answer.
- **The pattern generalizes**: The same architecture applies far beyond tennis — e.g., an agent diagnosing a production outage pulls from monitoring and log APIs the same way, with specialized systems doing the processing and the LLM doing the reasoning.