# Protecting SSH Keys with macOS Secure Enclave

Source: https://gatezh.com/posts/macos-secure-enclave-ssh-keys/

## Summary
This article by Serge Gatezh walks through storing SSH keys in the macOS Secure Enclave using only built-in tools — no third-party apps. The private key is generated inside the Secure Enclave hardware and never leaves it, requiring Touch ID for every SSH operation. The author ultimately decided against this native approach due to the ugly `ctccardtoken` Touch ID prompt, and plans to use the third-party app Secretive instead, which provides a better UI while still using Secure Enclave under the hood.

## Key takeaways
- **Hardware-backed security**: Secure Enclave keys are non-exportable — the private key never exists on disk or in memory, making it impossible to steal even on a fully compromised Mac.
- **Setup requires `sc_auth` + `ssh-keygen`**: Create the key with `sc_auth create-ctk-identity -k p-256-ne -t bio`, export a key handle with `ssh-keygen -w /usr/lib/ssh-keychain.dylib -K`, and set `SSH_SK_PROVIDER=/usr/lib/ssh-keychain.dylib`.
- **Explicit SSH config needed**: The key file `id_ecdsa_sk_rk` is not auto-discovered by SSH; it must be listed explicitly in `~/.ssh/config` under `IdentityFile`.
- **Always use Touch ID (`-t bio`)**: Without biometric protection, malware could silently use the key; Touch ID gives visibility into every SSH operation.
- **No backup possible**: Secure Enclave keys are tied to a single Mac and cannot be exported. The workaround is to register multiple keys (e.g., from a YubiKey or second Mac) in `authorized_keys`.
- **UX caveat**: The native Touch ID prompt shows "ctccardtoken needs to authenticate" — an unpolished message from the low-level CryptoTokenKit framework. Secretive is a recommended alternative for a better user experience.