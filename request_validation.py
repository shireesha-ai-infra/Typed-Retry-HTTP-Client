import httpx

# fetch user and get response
def fetch_user(url:str) -> httpx.Response:
    response = httpx.get(url, timeout=5)
    return response

def validate_response(response :httpx.Response) -> dict:
    # 1. Status Validation
    if response.status_code != 200:
        raise Exception(f"Request failed: {response.status_code}")
    
    # 2. Content type validation
    content_type = response.headers.get("content-type","")
    if "application/json" not in content_type:
        raise Exception("Invalid response format, Expected JSON")
    
    # 3. Parse Safely
    data = response.json()

    # Structure validation
    if not isinstance(data, dict):
        raise Exception("Invalid JSON Structure, expected object")

    # 4. Basic structure validation
    if not isinstance(data.get("id"), int):
        raise Exception("Invalid id")
    
    if not isinstance(data.get("name"), str):
        raise Exception("Invalid name")
    
    return data


def fetch_and_validate_response(url:str) -> dict:
    response = fetch_user(url)
    return validate_response(response)