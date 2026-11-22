# Notes on the discrete Fourier transform (DFT)

Source: https://eli.thegreenplace.net/2026/notes-on-the-discrete-fourier-transform-dft/

## Summary
This article by Eli Bendersky explains the Discrete Fourier Transform (DFT) as a practical tool for frequency analysis of finite-duration discrete signals. It derives the DFT from the Discrete-Time Fourier Series (DTFS) by treating N signal samples as one period of a periodic signal, then connects the DFT to linear algebra via the Fourier matrix built from complex roots of unity. The article also covers the inverse DFT, an efficient Python implementation, the Fast Fourier Transform (FFT), and the phenomenon of spectral leakage.

## Key takeaways
- The DFT treats N finite samples as one period of a periodic signal, enabling exact frequency reconstruction using DTFS coefficients.
- The DFT is equivalent to sampling the continuous DTFT at N equally spaced frequency points, bridging continuous and discrete frequency representations.
- The DFT can be expressed as a matrix-vector multiplication using the Fourier matrix, whose rows — formed from powers of complex roots of unity — constitute an orthogonal basis for C^N.
- The inverse DFT (IDFT) follows naturally from the matrix formulation: the conjugate of the Fourier matrix, scaled by 1/N, is its inverse, allowing perfect signal reconstruction.
- Spectral leakage occurs when the sampled window does not align with a whole number of signal cycles, spreading energy across frequency bins; window functions are the standard mitigation in practice.
- NumPy's `fft.fft` implements the Fast Fourier Transform, which computes the same result as direct matrix multiplication but in O(N log N) operations instead of O(N²).