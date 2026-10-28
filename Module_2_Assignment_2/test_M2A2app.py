
import pytest
from M2A2app import app

# Create a Flask test client for sending requests
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# Test the GET endpoint
def test_hello(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.json["message"] == "Welcome to my API!"
    assert response.json["status"] == "success"


# Test the POST endpoint with valid numbers
def test_sum_valid_numbers(client):
    response = client.post(
        "/sum",
        json={"numbers": [10, 20, 30, 40]}
    )

    assert response.status_code == 200
    assert response.json["numbers"] == [10, 20, 30, 40]
    assert response.json["sum"] == 100


# Testing the POST to see if it can handle negative numbers in the list
def test_sum_negative_numbers(client):
    response = client.post(
        "/sum",
        json={"numbers": [-5, 10, -2]}
    )

    assert response.status_code == 200
    assert response.json["sum"] == 3


# Testing the POST endpoint to see if it can handle floats
def test_sum_decimal_numbers(client):
    response = client.post(
        "/sum",
        json={"numbers": [1.5, 2.5]}
    )

    assert response.status_code == 200
    assert response.json["sum"] == 4.0


# Here I am testing the POST with an empty list
def test_sum_empty_list(client):
    response = client.post(
        "/sum",
        json={"numbers": []}
    )

    assert response.status_code == 400
