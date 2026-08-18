from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample economic data
economic_data = {
    "India": {
        "gdp_growth": 6.5,
        "inflation": 4.8,
        "unemployment": 7.2
    },
    "USA": {
        "gdp_growth": 2.4,
        "inflation": 3.0,
        "unemployment": 4.1
    },
    "China": {
        "gdp_growth": 5.0,
        "inflation": 1.2,
        "unemployment": 5.1
    }
}


@app.route("/")
def home():
    return jsonify({
        "message": "AI Powered Country Economic Prediction System",
        "status": "API is running"
    })


@app.route("/predict", methods=["GET"])
def predict():
    country = request.args.get("country")

    if country:
        data = economic_data.get(country)

        if data is None:
            return jsonify({
                "error": "Country not found"
            }), 404

        prediction = data["gdp_growth"] + 0.5

        return jsonify({
            "country": country,
            "predicted_gdp_growth": round(prediction, 2)
        })

    predictions = {}

    for country_name, data in economic_data.items():
        predictions[country_name] = round(
            data["gdp_growth"] + 0.5, 2
        )

    return jsonify({
        "predictions": predictions
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
