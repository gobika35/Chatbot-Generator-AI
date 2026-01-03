def guard_response(response: str):
    banned = ["politics", "religion"]
    for word in banned:
        if word in response.lower():
            return "I can help only with business-related questions."
    return response
