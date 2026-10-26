# The result of the C++26 DIS ballot

Source: https://train-it.eu/blog/cpp26-contracts-the-ballot-result/

## Summary
C++26 failed its ISO DIS (Draft International Standard) ballot — the first time any C++ draft has ever been rejected at this stage, and possibly the first failure for any SC22 language standard. The draft fell short on both required thresholds: it needed at least two-thirds of P-member votes in favor (got 60%) and no more than 25% negative votes (got 41%). The opposition centered almost entirely on the new contracts feature. The next WG21 meeting in Búzios, Brazil (November 2026) will be the first opportunity for the committee to decide how to proceed.

## Key takeaways
- C++26 is the first C++ draft to ever fail a DIS ballot; no prior C++ draft had even a single vote against.
- The ballot failed on both counts: 12/20 votes in favor (needed 14) and 9/22 negative votes (allowed 5).
- Nine countries voted No: Denmark, Finland, Iran, Italy, Japan, Luxembourg, Romania, Spain, and Sweden.
- The contracts feature was the primary reason for opposition — disputes center on whether contract assertions should be checkable/droppable at the implementation's discretion or provide stronger, compiler-enforced guarantees.
- Key features held up include reflection, `std::execution`, library hardening, and contracts — all now in limbo.
- The leading suggestion from WG21 Direction Group member Daveed Vandevoorde is to remove contracts from C++26 so the rest of the standard can ship.
- Compiler implementations (GCC 16, Clang) are not affected by the ballot result and continue shipping C++26 draft features.
- The full text of national-body comments won't be published until mid-January 2027 at the latest.
- The author hopes contracts remain in compilers to build the real-world experience that critics say is lacking — avoiding a chicken-and-egg problem for future standardization attempts.