# An interactive intro to Elliptic Curve Cryptography

Source: https://growingswe.com/blog/elliptic-curve-cryptography

## Summary
The article "An interactive intro to Elliptic Curve Cryptography" provides a visual and step-by-step introduction to the mathematical principles behind ECC. It explains elliptic curves, their unique point addition and scalar multiplication operations, and how these are adapted for cryptography by using finite fields. The core concept demonstrated is the Elliptic Curve Discrete Logarithm Problem, which makes scalar multiplication easy but its reversal computationally infeasible, forming the basis for secure public/private key pairs and key exchange protocols like ECDH.

## Key takeaways
- ECC utilizes the mathematics of elliptic curves, defined by specific equations (e.g., `y^2 = x^3 + ax + b`), to build cryptographic systems.
- Fundamental operations on elliptic curves include point addition (finding a third point on the curve by drawing a line through two points and reflecting) and scalar multiplication (repeated point addition), which generate new points on the curve.
- The security of ECC stems from the Elliptic Curve Discrete Logarithm Problem (ECDLP): it's easy to compute a public key `P = kG` from a private key `k` and base point `G`, but computationally infeasible to find `k` given `P` and `G`.
- For practical cryptographic applications, elliptic curves are defined over finite fields (modulo a prime number), transforming continuous curves into a discrete set of points suitable for computer calculations.
- ECC offers strong security with significantly smaller key sizes and faster computational performance compared to traditional asymmetric encryption methods like RSA, making it highly efficient for modern cryptography.