# Netstrings (1997)

Source: https://cr.yp.to/proto/netstrings.txt

## Summary
Netstrings, defined by D. J. Bernstein in 1997, are a simple wire format for encoding arbitrary byte strings as `<length>:<data>,`. The format is self-delimiting and length-prefixed, making it trivial to implement correctly in any language. Bernstein argues that netstrings are a reliable building block for network protocols, composable recursively, and inherently safer than delimiter-based encodings.

## Key takeaways
- **Format:** A netstring encodes a string as `len:string,` — e.g., `"hello world!"` becomes `12:hello world!,` and the empty string becomes `0:,`.
- **Length-prefixed by design:** Declaring the size upfront lets receivers pre-allocate exactly the right buffer, eliminating a whole class of memory bugs.
- **Security advantage over CRLF:** The classic `gets()`-based Finger buffer overflow happened because CRLF encoding doesn't declare size in advance, tempting implementors toward fixed buffers. Netstrings make the safe path the easy path.
- **Recursive composability:** Encoding a sequence of strings yields a single string, which can itself be netstring-encoded — enabling nested protocol layers without extra machinery.
- **Dead simple to implement:** Generating and parsing require only a handful of lines of C (or equivalent), reducing the surface area for implementation bugs.
- **No restrictions:** Any byte sequence of any length can be encoded; there are no reserved bytes or escape sequences to reason about.