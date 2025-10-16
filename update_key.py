ADMIN_PASS = "Happy@5278"

def handler(request, response):
    try:
        body = {}
        if hasattr(request, "json"):
            try:
                body = request.json()
            except Exception:
                body = {}
        else:
            try:
                body = request.get_json()
            except Exception:
                body = {}
        password = body.get("password")
        new_key = body.get("new_key")
        if password != ADMIN_PASS:
            return response.json({"error": "Invalid admin password"}, status=403)
        # echo back for frontend; instruct to set env var on Vercel
        return response.json({"ok": True, "message": "Received new key (set LEAK_API_TOKEN in Vercel env for persistence)", "api_key": new_key})
    except Exception as e:
        return response.json({"error": "Internal error", "detail": str(e)}, status=500)
