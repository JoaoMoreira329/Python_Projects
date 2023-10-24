# Import necessary modules and libraries
import asyncio
import logging
from flask import Flask, render_template, request, jsonify
import pyxivapi
from cachetools import LRUCache
from decouple import config

# Create a Flask app
app = Flask(__name__)

# Set API key
api_key = config("API_KEY")

# Initialize an LRU cache with a maximum size of 100 items
cache = LRUCache(maxsize=100)


# Define the route for the homepage
@app.route("/", methods=["GET", "POST"])
def display_info():
    if request.method == "POST":
        query = request.form["query"]
        context_groups = asyncio.run(fetch_info(query))
        return render_template("info.html", context_groups=context_groups, query=query)
    return render_template("index.html")


# Define the route for fetching information
@app.route("/get_info", methods=["POST"])
def get_items_info():
    query = request.form["query"]
    context_groups = asyncio.run(fetch_info(query))
    return jsonify(context_groups)


# Function to fetch lore information
async def fetch_info(query):
    try:
        if query in cache:
            return cache[query]

        client = pyxivapi.XIVAPIClient(api_key)
        lore = await client.lore_search(query=query)

        context_groups = {}
        for item in lore["Results"]:
            context = item["Context"]
            if context not in context_groups:
                context_groups[context] = []
            context_groups[context].append(item["Text"])

        await client.session.close()

        # Store the data in the cache
        cache[query] = context_groups
        return context_groups
    except pyxivapi.PxivapiException as e:
        # Handle the API key error, for example, by returning an error message.
        return render_template(
            "error.html", error="Invalid API key or API request failed."
        )
    except Exception as e:
        return {"error": "An unexpected error occurred"}


# Check if the script is run as the main application
if __name__ == "__main__":
    # Configure basic logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    # Run the Flask app in debug mode
    app.run(debug=True)
