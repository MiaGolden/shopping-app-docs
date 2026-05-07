from api_client import APIClient

client = APIClient()

def create_order(product_id):
    payload = {"product_id": product_id}
    response = client.post("/orders", payload)
    return response.status_code
