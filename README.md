# autofix-security-test

Security research fixture. Purpose: determine whether GitHub's Copilot / Agentic
Autofix (the LLM that proposes fixes for Code Scanning alerts) can be influenced by
**indirect prompt injection** embedded in source-code comments.

Each file under `vuln/` contains a genuine, CodeQL-detectable vulnerability
(SQL injection, reflected XSS, path traversal, command injection, hardcoded
secret) plus a crafted comment that instructs an automated remediation tool to
insert data-exfiltration or debug-leak behaviour into the "fix".

All exfiltration targets in the injected comments are deliberately
**non-functional placeholders** (`example.com`, `*.internal`, unset env vars) so
that even if the injection succeeds, no real data can leave. Secrets are known
public documentation dummies, not live credentials.

This is a controlled test against the researcher's own repository, run to
responsibly report any confirmed prompt-injection behaviour to GitHub. Do not
reuse the `vuln/` code in production.
