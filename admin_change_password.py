ADMIN_PASS = "Happy@5278"

def handler(request, response):
    # Note: This serverless handler cannot persist password across deployments.
    # It only verifies and returns success if correct password provided.
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
        new_password = body.get("new_password")
        if password != ADMIN_PASS:
            return response.json({"error": "Invalid current password"}, status=403)
        # Instruct admin to update Vercel env to persist change.
        return response.json({"ok": True, "message": "Password change acknowledged (update ADMIN_PASS in deployment for persistence)"})
    except Exception as e:
        return response.json({"error": "Internal error", "detail": str(e)}, status=500)
