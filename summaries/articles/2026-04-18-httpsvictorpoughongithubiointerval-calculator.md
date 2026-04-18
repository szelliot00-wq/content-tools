# Show HN: I made a calculator that works over disjoint sets of intervals

Source: https://victorpoughon.github.io/interval-calculator/

## Summary
The author developed an open-source TypeScript calculator that implements interval arithmetic over disjoint sets of intervals. This project addresses a major limitation of standard interval arithmetic, which struggles with operations like division by intervals containing zero, yielding imprecise or useless results. By adopting the concept of "interval unions," the calculator can provide more accurate and useful outcomes, such as `[-∞, -1] U [0.5, +∞]` for `1 / [-1, 2]`.

## Key takeaways
- Standard interval arithmetic has significant limitations, particularly with division by intervals containing zero or non-continuous functions, often producing unhelpful `[-∞, +∞]` results or being undefined.
- The more robust solution is to define arithmetic over "disjoint unions of intervals," which allows for precise representation of results that are not single continuous intervals.
- The author's open-source project implements this advanced "interval union arithmetic" in a TypeScript calculator.
- The calculator uses IEEE 754 double precision floats with outward rounding to guarantee the accuracy of interval results, mitigating floating-point precision issues.