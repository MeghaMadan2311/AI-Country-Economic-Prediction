import pandas as pd
from sklearn.linear_model import LinearRegression


def train_model(file_path="data.csv"):
    data = pd.read_csv(file_path)

    X = data[["inflation", "unemployment"]]
    y = data["gdp_growth"]

    model = LinearRegression()
    model.fit(X, y)

    return model


def predict_gdp(model, inflation, unemployment):
    prediction = model.predict([[inflation, unemployment]])
    return round(float(prediction[0]), 2)


if __name__ == "__main__":
    model = train_model()

    prediction = predict_gdp(
        model,
        inflation=4.0,
        unemployment=6.0
    )

    print("Predicted GDP growth:", prediction)
