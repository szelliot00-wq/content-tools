# Bashblog – a single bash script to create blogs

Source: https://github.com/cfenollosa/bashblog

## Summary
Bashblog is a minimal, single-file Bash script (~1000 lines) that lets you create and manage a static blog with zero dependencies and no installation beyond downloading `bb.sh`. Created by Carlos Fenollosa, it works on GNU/Linux, macOS, and BSD, generating static HTML files suitable for any public web folder. It supports Markdown, RSS, tags, drafts, Disqus comments, and Google Analytics, while deliberately keeping its scope small and maintainable.

## Key takeaways
- **Zero dependencies, single file**: Runs on standard Unix utilities (`sed`, `grep`, `date`, etc.) with no frameworks, databases, or runtimes required.
- **Dead simple workflow**: Run `./bb.sh post`, write in your editor, and the script generates HTML pages, an index, and an RSS feed automatically.
- **Fully static output**: All generated content is plain HTML/CSS — no server-side processing needed, just a public web folder.
- **Markdown and HTML support**: Defaults to Markdown (via a third-party library like Markdown.pl) with an option to force raw HTML.
- **Configurable without touching the script**: A `.config` file lets you override title, author, and other settings, making updates via git painless.
- **Intentionally minimal by design**: The project explicitly resists feature bloat — new contributions must be small, cross-platform, and strongly justified.
- **Licensed under GPLv3**: Free and open-source, with 15 contributors, 1.8k GitHub stars, and 237 forks.