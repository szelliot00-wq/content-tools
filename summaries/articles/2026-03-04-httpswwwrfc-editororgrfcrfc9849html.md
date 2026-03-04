# RFC 9849. TLS Encrypted Client Hello

Source: https://www.rfc-editor.org/rfc/rfc9849.html

## Summary
RFC 9849 defines Encrypted Client Hello (ECH), a TLS extension designed to enhance user privacy by encryptulating the Server Name Indication (SNI) within the ClientHello message. This mechanism prevents passive network observers from identifying the specific domain a user is trying to connect to. ECH works by sending an outer, unencrypted ClientHello to a "fallback" server, while nesting an encrypted inner ClientHello containing the true SNI and other sensitive parameters, allowing only the intended server to decrypt and process the request.

## Key takeaways
-   **Solves SNI Leakage:** ECH addresses a critical privacy vulnerability where the Server Name Indication (SNI) in the TLS ClientHello message is sent in plaintext, allowing network observers to see which websites a user is visiting.
-   **Mechanism:** It encrypts the actual SNI and other sensitive handshake parameters within an "inner" ClientHello, which is then encapsulated in an "outer" unencrypted ClientHello. The server uses pre-shared public keys (often distributed via DNS) to decrypt the inner ClientHello.
-   **Enhanced Privacy:** By hiding the target domain name from passive observers, ECH significantly improves user privacy and makes it harder for intermediaries to monitor or censor web activity based on specific domain names.
-   **Dependencies and Limitations:** ECH requires server-side support, relies on secure mechanisms like DNS HTTPS Resource Records for key distribution, and is designed for TLS 1.3 and later. While it encrypts the domain, it does not hide the target server's IP address.