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
        return response.json({"ok": password == ADMIN_PASS})
    except Exception as e:
        return response.json({"ok": False, "error": str(e)}, status=500)
