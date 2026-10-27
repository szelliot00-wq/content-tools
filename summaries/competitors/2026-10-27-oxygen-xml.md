# oXygen XML Editor — Changes 2026-10-27

### Product overview

## What Changed
Oxygen XML added a new "Security" page to their Support navigation section, inserting it between "Mailing Lists" and "Contact Us."

## Notable Updates
- New **Security** link added to the Support footer section — likely a dedicated security disclosure or vulnerability reporting page
- All other changes are internal reference ID renumbering (element refs shifted by 1 throughout), which is a side effect of inserting the new Security link — no content was added or removed elsewhere

---

### Feature matrix

## What Changed
The diff shows only internal reference ID renumbering across the entire page — every element reference (e.g., `[ref=e78]` → `[ref=e79]`) shifted up by one, consistent with a single new element being inserted early in the DOM.

## Notable Updates
- **New product added to the feature matrix**: A new checkbox item was inserted at the top of the "Select Products" list. Previously the list started with "XML Editor" at ref e73; now "XML Editor" is at ref e74, with a new item occupying ref e73 (not named in the visible diff text, but its insertion caused all subsequent refs to renumber).
- **Feature matrix table gained a column**: The header row now shows 6 product columns with an additional "Professional" tier cell (ref e2281), suggesting a new product or license tier was added to the comparison table.
- No pricing text, feature descriptions, or navigation link labels changed — all content strings are identical; only the structural ref IDs shifted.

---

### Pricing

## What Changed
Oxygen XML's shop page added a dedicated **Security** link to the Support navigation section, and all internal element references shifted by one (indicating a new DOM node was inserted).

## Notable Updates
- **New "Security" page link** added to the Support section footer nav, between "Mailing Lists" and "Contact Us" — likely a new security disclosure or vulnerability policy page
- All other content (products, pricing, license tiers) is unchanged — the ref number shifts throughout the diff are purely a side-effect of the single new node insertion, not actual content changes

---

### Release history

## What Changed
A new "Security" page link was added to the Support section of the footer navigation.

## Notable Updates
- New **Security** link added to the footer's Support section (inserted between "Mailing Lists" and "Contact Us")
- All other differences are internal reference ID renumbering — no content, pricing, or product changes

---

