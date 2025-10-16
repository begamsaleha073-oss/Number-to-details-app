import os
import requests

def handler(request, response):
    try:
        # read JSON body safely
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
        query = body.get("query") if isinstance(body, dict) else None
        if not query:
            return response.json({"error": "Missing query"}, status=400)

        api_token = os.environ.get("LEAK_API_TOKEN", "")
        if not api_token:
            return response.json({"error": "API key not configured. Set LEAK_API_TOKEN in environment variables."}, status=400)

        url = "https://leakosintapi.com/"
        payload = {"token": api_token, "request": str(query).split("\n")[0], "limit": 300, "lang": "ru"}
        r = requests.post(url, json=payload, timeout=30)
        try:
            data = r.json()
        except Exception:
            return response.json({"error": "Invalid response from upstream", "status_code": r.status_code, "body": r.text}, status=502)
        return response.json(data)
    except Exception as e:
        return response.json({"error": "Internal error", "detail": str(e)}, status=500)
