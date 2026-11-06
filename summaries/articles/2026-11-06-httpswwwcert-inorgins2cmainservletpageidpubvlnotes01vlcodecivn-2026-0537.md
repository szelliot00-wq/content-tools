# Hardcoded credentials and other issues in Tata Motors App

Source: https://www.cert-in.org.in/s2cMainServlet?pageid=PUBVLNOTES01&VLCODE=CIVN-2026-0537

## Summary
CERT-In (India's Computer Emergency Response Team) published vulnerability note CIVN-2026-0537 on November 4, 2026, disclosing four HIGH-severity vulnerabilities in Tata Motors' connected vehicle apps iRA 2.0 (versions 26.7.3 and below) and iRA.ev (versions 26.7.2 and below). These apps provide remote vehicle commands, status monitoring, and trip information for ICE and EV customers respectively. The vulnerabilities were reported by Pranav Rajendran and could allow attackers to gain unauthorized access to vehicle services and sensitive user data.

## Key takeaways
- **CVE-2026-121144 (Hardcoded Credentials):** Service account credentials, API keys, and auth tokens are embedded in the app package — any unauthenticated attacker can extract them by downloading the app.
- **CVE-2026-121145 (Insecure WebView):** Insufficient URL/origin validation in the WebView component allows a remote attacker to inject malicious content, steal live bearer tokens, and impersonate users.
- **CVE-2026-121146 (Information Disclosure):** Authentication tokens are written to debug/development logs; a local attacker with log access can retrieve and reuse session tokens to impersonate users.
- **CVE-2026-121147 (Broken SSL Pinning):** Certificate pinning is improperly implemented, leaving network traffic vulnerable to interception or modification by a man-in-the-middle attacker.
- **Fix:** Users should update to the latest versions of both apps via the Google Play Store or Apple App Store.