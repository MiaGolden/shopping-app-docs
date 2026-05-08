from config import BASE_URL, TIMEOUT
import requests


class APIClient:
    def __init__(self, token=None, mock=False):
        self.token = token
        self.mock = mock

        if self.mock:
            from mock_api import MockAPI
            self.mock_api = MockAPI()

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.token}"
        } if self.token else {}

    def get(self, path):
        if self.mock:
            if path == "/products":
                return type("R", (), {"json": lambda: self.mock_api.get_products()})

        return requests.get(
            f"{BASE_URL}{path}",
            headers=self._headers(),
            timeout=TIMEOUT
        )

    def post(self, path, data):
        if self.mock:
            if path == "/orders":
                return type("R", (), {
                    "json": lambda: self.mock_api.create_order(data["product_id"]),
                    "status_code": 201
                })

        return requests.post(
            f"{BASE_URL}{path}",
            json=data,
            headers=self._headers(),
            timeout=TIMEOUT
        )
