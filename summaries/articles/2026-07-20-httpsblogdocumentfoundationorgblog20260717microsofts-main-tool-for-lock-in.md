# How proprietary formats have become Microsoft’s main tool for lock-in

Source: https://blog.documentfoundation.org/blog/2026/07/17/microsofts-main-tool-for-lock-in/

## Summary
Published on the TDF Community Blog, this article by Italo Vignoli argues that Microsoft's proprietary document formats (DOC, XLS, DOCX, XLSX, PPTX) function as the primary mechanism for vendor lock-in, not through explicit restrictions but through subtle incompatibilities that make documents created in Microsoft Office render poorly in other software. The piece examines how Microsoft's OOXML format, despite receiving ISO standardization, was a deeply contested process that produced a spec so complex and tied to Microsoft's own implementation that no other software can fully support it. The author concludes that true digital sovereignty requires consciously choosing open standards like ODF, open fonts, and open archiving formats such as PDF/A.

## Key takeaways
- Lock-in works through friction, not prohibition: documents open in other apps but render incorrectly, making alternatives feel unreliable and driving users back to Microsoft products.
- OOXML's ISO standardization was procedurally controversial and produced a spec that only Microsoft Office fully implements — making it a "proprietary format with a standardization certificate" in practice.
- Microsoft defaults to OOXML Transitional (the legacy-laden variant only it supports fully) while burying or removing OOXML Strict, the cleaner version other software could actually implement.
- The stakes scale with organization size: for governments and hospitals, format lock-in means delegating custody of institutional memory to a private company whose commercial interests may diverge from the public interest.
- Historical digital formats have become unreadable when their supporting software disappeared — proprietary formats accelerate this risk by concentrating format knowledge in a single vendor.
- The solution exists and is non-technical: adopt ODF for documents, open fonts, and PDF/A for archiving — but it requires a deliberate policy decision by someone with authority to mandate it.
- Every format, font, and software choice is a governance decision, not a technical default; "digital sovereignty begins with the recognition that this is a choice."