# 🧠 Walkthrough – Broken Brute-Force IP Block

In this lab, we bypass weak brute-force protection by alternating login requests between our own account and Carlos's. This resets the failed login counter and lets us brute-force his password without triggering an IP block. 🧨

---

## 🔍 Step 1: Confirm the Defense Logic

- Try logging in with invalid credentials.
- After **3 failed attempts**, your IP gets blocked temporarily.
- But if you log in successfully with your own account after a few bad tries, the counter resets. That’s the flaw we’ll exploit.

---

## ✉️ Step 2: Capture a Login Request

- Use Burp Suite's Proxy to intercept a `POST /login` request.
- Use your account for this to test both success and failure behavior.
- Send the intercepted request to **Intruder** for attack setup.

🖼️ _See: `step2_proxy-login-capture.png`_

---

## 🎛️ Step 3: Configure Intruder (Pitchfork Mode)

- Use **Pitchfork** to alternate usernames and passwords in sync.
- Payload 1 (Username):
  - First: your own username
  - Then: `carlos`
- Payload 2 (Password):
  - Your actual password first (for successful login reset)
  - Then: candidate passwords for Carlos

🖼️ _See: `step3_intruder-pitchfork-setup.png`_

---

## 🧵 Step 4: Resource Pool Setup

- Create a **resource pool** in Burp.
- Set **Maximum concurrent requests = 1** to preserve the login sequence.
- This ensures each Carlos attempt is preceded by your legit login.

🖼️ _See: `step4_resource-pool-config.png`_

---

## 🚀 Step 5: Launch the Attack

- Start the Intruder attack.
- Use response filtering to spot `HTTP 302 Found` (success indicator).
- Look for a line where:
  - Username = `carlos`
  - Response = `302`
- That’s his valid password right there! 💥

🖼️ _See: `step5_successful-hit-302.png`_

---

## 🔓 Step 6: Confirm the Login

- Use the discovered password to log in as Carlos.
- You should land on his account page.

🖼️ _See: `step6_logged-in-carlos.png`_

---

## ⚠️ Key Takeaways

- IP-based protection is not enough if login counters reset too easily.
- Alternating login requests can bypass basic rate limits.
- Pitchfork + Resource Pool = stealth brute-force!

---

## 💡 Defensive Recommendations

- Don’t reset failed login counters too loosely
- Implement CAPTCHA after a threshold
- Track login attempts per user *and* IP
- Avoid trusting client IP headers blindly

