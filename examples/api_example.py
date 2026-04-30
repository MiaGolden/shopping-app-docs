import requests

BASE_URL = "https://api.shopapp.com"

def get_products():
    response = requests.get(f"{BASE_URL}/products")
    return response.json()

if __name__ == "__main__":
    products = get_products()
    print(products)
