# ASCII and Unicode quotation marks (2007)

Source: https://www.cl.cam.ac.uk/~mgk25/ucs/quotes.html

## Summary
The article "ASCII and Unicode quotation marks" by Markus Kuhn clarifies the critical distinction between straight ASCII quotation marks and typographically correct "smart" (curly) quotes. It explains that straight quotes (', ") are universal, machine-readable, and essential for programming, command lines, and generic plain text due to their simplicity and consistency. In contrast, curly quotes (‘ ’ “ ”) are aesthetically pleasing for human readability and typesetting but can cause issues when automatically converted or used in technical contexts. The author advises choosing the appropriate quote type based on context: straight for technical data and curly for final display when typography is paramount and character encoding is properly managed.

## Key takeaways
-   **Differentiate straight vs. curly quotes:** Straight ASCII quotes (', ") are for machine readability and universal plaintext, while "smart" (curly) quotes (‘ ’ “ ”) are for typographic aesthetics.
-   **Use straight quotes for technical contexts:** Programming, command lines, filenames, and plain text should exclusively use straight quotes for consistency and machine compatibility.
-   **Reserve curly quotes for controlled display:** Use typographic quotes only in environments like typesetting or web content where aesthetic presentation is paramount and character encoding is properly managed.
-   **Beware of automatic smart quote conversions:** Word processors' "smart quote" features can introduce problems when text is transferred to technical or code environments.
-   **Do not misuse other symbols as quotes:** Characters like grave accents (`) or primes (′ ″) have distinct meanings and are not interchangeable with quotation marks or apostrophes.
-   **Unicode supports diverse international quotes:** While Unicode offers many language-specific quotation marks (e.g., guillemets), the straight ASCII quotes remain universally usable for simple plaintext across all languages.