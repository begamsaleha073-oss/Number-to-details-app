import os
def handler(request, response):
    api_token = os.environ.get("LEAK_API_TOKEN", "")
    return response.json({"token_set": bool(api_token)})
