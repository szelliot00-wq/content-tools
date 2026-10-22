# OpenAI CLI

Source: https://github.com/openai/openai-cli

## Summary
The OpenAI CLI is an official Go-based command-line tool for interacting with the OpenAI REST API. It follows a resource-based command structure and supports installation via Homebrew or Go. The repository is public on GitHub with 770 stars, 79 forks, and active development (559 commits, 150 branches).

## Key takeaways
- **Installation**: Available via `brew install openai/tools/openai` or `go install github.com/openai/openai-cli/cmd/openai@latest` (requires Go 1.26+).
- **Command structure**: Uses `openai <resource> [subresource...] <command> [flags...]`; standard endpoints need `OPENAI_API_KEY`, admin endpoints need `OPENAI_ADMIN_KEY`.
- **Output formats**: Defaults to human-readable text; use `--format json` or `--format jsonl` for machine-parseable output in scripts.
- **Image generation**: `openai images generate` saves images to `~/Downloads/gpt-images/` by default using model `gpt-image-2.5-sunburst`; `images create-variation` is retired — use `images edit` instead.
- **Update notices**: Checks for new releases at most once every 7 days when running interactively; disable with `OPENAI_CLI_NO_UPDATE_CHECK=1`.
- **Mutual TLS**: Beta support for mTLS client certificate authentication via `OPENAI_MTLS_CLIENT_CERT_FILE` and `OPENAI_MTLS_CLIENT_KEY_FILE`.
- **File inputs**: JSON flags support `@filename` syntax to read file contents; binary upload flags use plain paths without `@`.
- **Licensed** under Apache 2.0.