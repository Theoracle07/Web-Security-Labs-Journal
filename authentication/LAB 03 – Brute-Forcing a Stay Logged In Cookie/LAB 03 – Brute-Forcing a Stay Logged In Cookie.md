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

🎉 Lab Solved.

