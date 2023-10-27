from flask import Flask, request, jsonify, render_template
import pyshorteners

app = Flask(__name__)
url_store = []  # Dictionary to store URL mappings

# Create API - Shorten a URL
@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    title = data.get('title')
    long_url = data.get('long_url')
    
    if not title or not long_url:
        return jsonify({"error": "Both title and long URL are required"}), 400
    print('URL STORE', url_store)
    short_url = shorten(long_url)
    url_store.append({"title": title, "long_url": long_url, "short_url": short_url})
    return jsonify({"title": title, "short_url": short_url})

# API - Search for URLs
@app.route('/search', methods=['GET'])
def search_url():
    data = request.get_json()
    term = data.get('term')
    print('TERM', term)
    results = []
    for item in url_store:
        if term.lower() in item['title'].lower():
            results.append(item)
    
    return jsonify(results)


# Web Interface
@app.route('/')
def home():
    return "Welcome to the URL Shortener Service"

# Helper function to shorten a URL using pyshorteners
def shorten(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

    
if __name__ == '__main__':
    app.run(debug=True)
