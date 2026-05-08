class MockAPI:
    def get_products(self):
        return [
            {"id": 1, "name": "Phone", "price": 500},
            {"id": 2, "name": "Laptop", "price": 1200}
        ]

    def create_order(self, product_id):
        return {
            "order_id": 123,
            "status": "created",
            "product_id": product_id
        }
