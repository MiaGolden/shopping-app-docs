```python
import requests

BASE_URL = "https://api.shopapp.com"


def get_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        return response.json()
    return []


def create_order(product_id):
    data = {"product_id": product_id}
    response = requests.post(f"{BASE_URL}/orders", json=data)
    return response.status_code


if __name__ == "__main__":
    products = get_products()
    print("Products:", products)

    if products:
        status = create_order(products[0]["id"])
        print("Order status:", status)
