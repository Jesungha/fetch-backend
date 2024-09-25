import requests
import json

# Base URL of your Flask application
BASE_URL = "http://localhost:5000"  # Adjust this if your server is running on a different port or host

def test_add_transactions():
    transactions = [
        {"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"},
        {"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"},
        {"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"},
        {"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z"},
        {"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"}
    ]

    for transaction in transactions:
        response = requests.post(f"{BASE_URL}/add", json=transaction)
        print(f"Adding transaction: {transaction}")
        print(f"Response status: {response.status_code}")
        print(f"Response content: {response.text}\n")
        assert response.status_code == 200, f"Failed to add transaction: {transaction}"

def test_spend_points():
    spend_request = {"points": 5000}
    response = requests.post(f"{BASE_URL}/spend", json=spend_request)
    print("Spending points:")
    print(f"Request: {spend_request}")
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.text}\n")
    assert response.status_code == 200, "Failed to spend points"
    return response.json()

def test_get_balance():
    response = requests.get(f"{BASE_URL}/balance")
    print("Getting balance:")
    print(f"Response status: {response.status_code}")
    print(f"Response content: {response.text}\n")
    assert response.status_code == 200, "Failed to get balance"
    return response.json()

if __name__ == "__main__":
    print("Starting tests...\n")

    print("1. Adding transactions:")
    test_add_transactions()

    print("2. Spending points:")
    spent_points = test_spend_points()
    print(f"Points spent: {json.dumps(spent_points, indent=2)}")

    print("3. Checking final balance:")
    final_balance = test_get_balance()
    print(f"Final balance: {json.dumps(final_balance, indent=2)}")

    print("\nAll tests completed.")