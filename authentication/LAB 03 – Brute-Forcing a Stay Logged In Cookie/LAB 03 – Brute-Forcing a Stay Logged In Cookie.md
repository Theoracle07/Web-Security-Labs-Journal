# LAB 03 – Brute-Forcing a Stay Logged In Cookie

## 🥇 Step 1: Log In
Log into your own account with "Stay logged in" selected. A persistent cookie is issued.

## 🧪 Step 2: Inspect the Cookie
In Burp, decode the stay-logged-in cookie using the Inspector panel. You’ll see:
`wiener:51dc30ddc473d43a6011e9ebba6ca770`
 - Compare this hash with MD5 + (password). If it matches, the structure is confirmed as = base64(username:md5(password))
   

## 🚪 Step 3: Log Out
To avoid interference, log out of your account.

## 🎯 Step 4: Send Request to Intruder
Highlight the cookie value in the GET `/my-account?id=wiener` request and send it to Intruder.

## ⚙️ Step 5: Configure Payload
Set your own password as payload.

## 🧱 Step 6: Apply Payload Processing Rules
Sequentially add:
- Hash → MD5
- Add prefix → `wiener:`
- Encode → Base64

## 📘 Step 7: Setup Grep Match
Add a grep match filter for `Update email`, which only appears when authenticated.

## ✅ Step 8: Test the Cookie
Start the attack. One payload should produce an authenticated response—this proves your setup works.

## 🔁 Step 9: Attack Carlos’s Cookie
Change the following:
- `id=wiener` → `id=carlos`
- Payload → candidate password list
- Prefix → `carlos:`

## 🏁 Step 10: Find the Winning Cookie
When the attack finishes, look for the response with `Update email`. The corresponding payload is Carlos's valid cookie.

---
# ✅ Key Takeaways

## 🔑 What i Learned

- The "Stay logged in" feature can introduce severe authentication vulnerabilities if improperly implemented.
- Storing persistent authentication cookies as `base64(username:md5(password))` allows for predictable brute-forcing when password hashes are weak or discoverable.
- Burp Suite's **Intruder + Payload Processing** combination can simulate custom hashing, encoding, and formatting logic—making it a powerful tool for brute-force automation.
- Grep Match in Burp helps detect success indicators in server responses without manual inspection.

---

## ⚠️ Precautions & Defensive Recommendations

- **Do not include password hashes in client-side cookies.** Authentication tokens should be random, unique, and validated securely on the server.
- **Avoid predictable token formats.** If an attacker can guess how cookies are generated, they can replicate valid ones.
- **Use strong hashing algorithms.** MD5 is outdated and vulnerable. Instead, use bcrypt, scrypt, or Argon2 for hashing sensitive data.
- **Secure cookie attributes:**  
  - Set `HttpOnly` and `Secure` flags  
  - Use short lifetimes for persistent cookies  
  - Consider binding tokens to device identifiers or IP ranges
- **Implement rate-limiting:** Prevent brute-force attacks by monitoring and throttling failed authentication attempts—even against cookies.

---

_This lab reinforces how simple logic flaws in authentication mechanisms can be weaponized. By understanding and reproducing them, we learn how to build systems that aren’t just functional—but resilient and secure._


🎉 Lab Solved.

