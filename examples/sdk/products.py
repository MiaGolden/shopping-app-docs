from api_client import APIClient

client = APIClient()

def fetch_products():
    response = client.get("/products")
    return response.json()
