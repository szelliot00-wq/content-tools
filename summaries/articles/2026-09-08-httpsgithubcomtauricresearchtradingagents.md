# Multi-Agents LLM Financial Trading Framework

Source: https://github.com/TauricResearch/TradingAgents

## Summary
TradingAgents is an open-source multi-agent LLM framework (103k GitHub stars) that simulates a real-world trading firm by deploying specialized AI agents — analysts, traders, and risk managers — that collaborate and debate to produce trading decisions. Built on LangGraph, it supports a wide range of LLM providers and markets, and includes features like decision logging, checkpoint resume, and cross-run learning. It is intended as a research scaffold, not financial advice.

## Key takeaways
- **Multi-agent architecture**: Specialized agents cover fundamentals, sentiment, news, and technical analysis, plus a trader agent and risk/portfolio management layer that engage in dynamic discussion.
- **Broad LLM provider support**: Works with OpenAI, Anthropic, Google, xAI, DeepSeek, Qwen, Ollama (local), AWS Bedrock, Azure OpenAI, and any OpenAI-compatible server.
- **Global market coverage**: Supports any ticker on Yahoo Finance — US, Hong Kong, Tokyo, London, India, Canada, Australia, China A-shares, and crypto.
- **Persistent learning**: A decision log tracks past trades, computes realized returns vs. SPY, generates reflections, and injects lessons into future runs for the same ticker.
- **Crash recovery**: Optional checkpoint resume via LangGraph saves state after each node, so interrupted runs restart from the last successful step.
- **Non-deterministic by design**: Results vary across runs due to LLM sampling and live data sources; it's a research tool, not a backtestable strategy with fixed returns.
- **Easy deployment**: Installable via pip or Docker, with a CLI and Python package API for programmatic use.