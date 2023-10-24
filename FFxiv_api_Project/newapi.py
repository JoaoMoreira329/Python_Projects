from flask import Flask, jsonify, request
import requests

app = Flask(__name)


@app.route("/fetch_new_api_data", methods=["GET"])
def fetch_new_api_data():
    url = "https://ffxiv-misc-data.p.rapidapi.com/ffxiv/job-v1"
    params = {"per_page": "9"}
    headers = {
        "X-RapidAPI-Key": "f5f15a1377mshe39ae238d398908p16141ejsn917d42e8db7e",
        "X-RapidAPI-Host": "ffxiv-misc-data.p.rapidapi.com",
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
