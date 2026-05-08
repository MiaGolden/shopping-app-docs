from examples.api_client import APIClient


class ShopSDK:
    def __init__(self, token=None, mock=False):
        self.client = APIClient(token=token, mock=mock)

    def products(self):
        return self.client.get("/products").json()

    def create_order(self, product_id):
        return self.client.post("/orders", {"product_id": product_id}).json()
