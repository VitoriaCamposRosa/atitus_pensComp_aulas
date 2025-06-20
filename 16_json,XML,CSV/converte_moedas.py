import http.client
import json
from unittest.mock import patch

def get_response(coin_a: str, coin_b: str) -> dict:
    conn = http.client.HTTPSConnection("api.coinbase.com")
    conn.request("GET", f"/v2/prices/{coin_a}-{coin_b}/buy")
    response = conn.getresponse()
    response_text = response.read().decode()
    conn.close()
    return json.loads(response_text)

def get_valid_currencies() -> dict:
    conn = http.client.HTTPSConnection("api.coinbase.com")

    conn.request("GET", "/v2/currencies")
    traditional = json.loads(conn.getresponse().read().decode())["data"]

    conn.request("GET", "/v2/currencies/crypto")
    crypto = json.loads(conn.getresponse().read().decode())["data"]

    conn.close()
    return {
        "traditional": [c["id"] for c in traditional],
        "crypto": [c["code"] for c in crypto]
    }

def is_valid_currency(currency: str, valid_currencies: dict) -> bool:
    return (
        currency in valid_currencies["traditional"] or
        currency in valid_currencies["crypto"]
    )

def get_exchange_rate(coin_a: str, coin_b: str) -> float:
    response = get_response(coin_a, coin_b)
    return float(response["data"]["amount"])


def get_new_value(coin_a: str, coin_b: str, value: float) -> float:
    rate = get_exchange_rate(coin_a, coin_b)
    return value * rate

def test_get_valid_currencies():
    currencies = get_valid_currencies()
    assert isinstance(currencies, dict)
    assert "USD" in currencies["traditional"]
    assert "BTC" in currencies["crypto"]

def test_is_valid_currency():
    currencies = get_valid_currencies()
    assert is_valid_currency("USD", currencies) is True
    assert is_valid_currency("BRL", currencies) is True
    assert is_valid_currency("XYZ", currencies) is False

def test_get_new_value_with_mock(monkeypatch): 
     def mock_get_response(coin_a: str, coin_b: str) -> dict:
        return {"data": {"amount": "5.0"}}
    
    monkeypatch.setattr('__main__.get_response', mock_get_response)
    
    assert get_new_value(10, "USD", "BRL") == 50.0 