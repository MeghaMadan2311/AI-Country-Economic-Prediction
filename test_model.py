from model import train_model, predict_gdp


def test_model_training():
    model = train_model("data.csv")
    assert model is not None


def test_gdp_prediction():
    model = train_model("data.csv")

    prediction = predict_gdp(
        model,
        inflation=4.0,
        unemployment=6.0
    )

    assert isinstance(prediction, float)
