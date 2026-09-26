# oXygen XML Editor — Changes 2026-09-26

### Product overview

## What Changed
Oxygen XML Editor's site added a formal cookie consent dialog with accept/reject/customize options, replacing a simpler cookie notice banner.

## Notable Updates
- Added a "We value your privacy" cookie consent dialog with **Reject all**, **Customize**, and **Accept all** buttons
- Added a **Cookie Settings** link in the footer alongside the existing Sitemap, Terms of Use, and Privacy Policy links
- Removed the previous inline cookie notice bar (simple "Find out more about cookies" link with a dismiss button)

All other differences are internal element reference ID renumbering with no visible content or structural changes.

---

### Feature matrix

## What Changed
The Oxygen XML Editor feature matrix page appears to have undergone an internal restructuring, with all element reference IDs incremented by 3 across the entire page — a strong signal that new content was inserted near the top of the page's interactive element tree.

## Notable Updates
- **New product checkbox added to the feature matrix selector**: The "Select Products" list gained an additional entry — reference IDs for all five product checkboxes (XML Editor, XML Developer, JSON Editor, XML Author, Web Author) shifted up by ~3, indicating a new item was inserted before them in the DOM. The product names themselves remain unchanged.
- **No pricing changes detected**: All product tier labels (Enterprise, Professional, Academic, Personal) are identical between versions.
- **No new features or feature categories**: Every feature row and section heading (XML Editing Tools, DITA Support, AI Tools, Collaboration, Publishing, etc.) carries over unchanged — only reference ID numbers shifted.
- **AI Tools section unchanged**: The "Oxygen AI Positron Assistant Enterprise" row remains present with the same product coverage as before.
- **Likely cause**: A new UI element (possibly a checkbox, filter, or product option) was inserted near the top of the navigation or product selector, causing a cascade of ID renumbering throughout the rest of the page with no visible content changes.

---

### Pricing

## What Changed
Oxygen XML's shop page added a proper cookie consent dialog and a new "Cookie Settings" link in the footer, replacing the previous minimal cookie notice banner.

## Notable Updates
- New cookie consent dialog ("We value your privacy") with Reject all / Customize / Accept all buttons, replacing the old simple "Find out more about cookies" link
- "Cookie Settings" link added to the footer privacy section alongside Sitemap, Terms of Use, and Privacy Policy
- All other differences are internal element reference ID renumbering with no visible content changes — pricing, products, and navigation remain unchanged

---

### Release history

## What Changed
Oxygen XML's release history page added a new "Cookie Settings" link in the footer and replaced the old simple cookie banner with a full cookie consent dialog offering "Reject all," "Customize," and "Accept all" options.

## Notable Updates
- New **Cookie Settings** link added to the footer alongside Sitemap, Terms of Use, and Privacy Policy
- Old inline cookie notice replaced with a modal **"We value your privacy"** consent dialog with granular controls (Reject all / Customize / Accept all)
- "Privacy Policy" link text now has a trailing space, suggesting a minor text adjustment (likely cosmetic/incidental)
- No product releases, pricing changes, or new feature announcements were detected in this diff — all version history entries (including the most recent **Ai Positron 8.4** from September 21, 2026) remain unchanged

---

