from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_country_prediction():
    client = app.test_client()

    response = client.get("/predict?country=India")

    assert response.status_code == 200

    data = response.get_json()

    assert data["country"] == "India"
    assert "predicted_gdp_growth" in data


def test_all_country_predictions():
    client = app.test_client()

    response = client.get("/predict")

    assert response.status_code == 200

    data = response.get_json()

    assert "predictions" in data
    assert len(data["predictions"]) > 0
