README - LeakOSINT Vercel Flat Deploy (one-folder)

Files included (flat):
- index.html
- search.py
- update_key.py
- admin_verify_password.py
- admin_get.py
- admin_change_password.py
- vercel.json
- readme.txt

Important notes:
1) Vercel serverless functions using Python expect a handler(request, response) signature as used here.
2) Environment variable LEAK_API_TOKEN must be set in Vercel Project Settings -> Environment Variables.
3) Because Vercel serverless functions cannot persist file changes, admin actions that need persistence (API key or password) require updating Vercel env vars via the dashboard.
4) To deploy:
   - Zip these files (already prepared).
   - Create a GitHub repo and push these files, or upload directly to Vercel.
   - In Vercel, import the repo and deploy.
5) Admin password initial value = Happy@5278 (hardcoded). Change in code if you want to persist elsewhere.
