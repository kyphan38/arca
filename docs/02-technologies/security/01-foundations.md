# foundations

- [x] Progress: Done

## Real-World Production Scenario

![img](./img/01/01.png)

Mobile app request body

```json
POST /v1/transfers HTTP/1.1
Authorization: Bearer eyJhbGciOiJSUzI1NiIs...
Content-Type: application/json

{
  "source_account":      "VN0123456789",
  "destination_account": "VN9876543210",
  "amount":              { "value": 5000000, "currency": "VND" },
  "memo":                "Rent November"
}
```

## Core Security Frameworks

### CIA Triad

- Confidentiality: Data is only readable by authorized parties
  - Broken by: Eavesdropping, data leaks, etc.
- Integrity: Data is not modified without authorization, and modifications are detectable
  - Broken by: Tampering in transit, SQLi
- Availability: System is usable when needed
  - Broken by: DDoS, ransomware, etc.

### AAA Framework

- Authentication: Prove who (or what) is making the request
- Authorization: Decide what that identity is allowed to do
- Accounting / Audit: Record what was done by whom and when

### Trust Boundaries

- Rule: Data crossing trust boundaries must be re-authenticated, re-authorized, re-validated, encoded, and logged

### STRIDE Threat Model

| Letter | Threat | Violates | Example on QuickPayS |
| :---: | :--- | :--- | :--- |
| **S** | Spoofing | Authentication | Stolen JWT → attacker impersonates a customer |
| **T** | Tampering | Integrity | MITM rewrites `destination_account` in transit |
| **R** | Repudiation | Non-repudiation | Customer claims "I never authorized that transfer" - can you prove they did? |
| **I** | Information disclosure | Confidentiality | Error message leaks "account VN98… does not exist" (account enumeration) |
| **D** | Denial of Service | Availability | Flood `/v1/transfers` with bad-signature requests to exhaust CPU |
| **E** | Elevation of Privilege | Authorization | The red team finding above - acting on someone else's account |

### Attack Trees

- Attack tree: Decomposes target objective into sub-goals
  - Root: Attacker's objective
  - Children: Ways to achieve it (OR nodes by default; AND nodes require all children)

```markdown
GOAL: Steal funds from customer Y's account via QuickPay
├── OR: Compromise customer Y directly
│   ├── Phish credentials + bypass MFA
│   ├── SIM-swap to intercept SMS OTP    [cheap, high yield in retail banking]
│   └── Malware on Y's phone
├── OR: Compromise the API surface
│   ├── Steal/replay a valid JWT
│   ├── Find IDOR/BOLA on /v1/transfers  ← red-team finding
│   └── Bypass WAF and inject
├── OR: Compromise an insider
│   ├── Bribe a back-office operator
│   └── Compromise a CI/CD pipeline that can push code
└── OR: Compromise the rails
    └── Manipulate destination at clearing layer (out of scope here)
```
