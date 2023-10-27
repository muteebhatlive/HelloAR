from flask import Flask, request, jsonify, render_template
import pyshorteners

app = Flask(__name__)
urls = [] 

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    title = data.get('title')
    long_url = data.get('long_url')
    
    if not title or not long_url:
        return jsonify({"error": "Both title and long URL are required"}), 400
    print('URL STORE', urls)
    short_url = shorten(long_url)
    urls.append({"title": title, "long_url": long_url, "short_url": short_url, "hits" : 0})
    return jsonify({"title": title, "short_url": short_url})

@app.route('/search', methods=['GET'])
def search_url():
    data = request.get_json()
    term = data.get('term')
    print('TERM', term)
    print(urls)
    results = []
    for item in urls:
        if term.lower() in item['title'].lower():
            results.append(item)
    
    return jsonify(results)



def shorten(long_url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_url)

@app.route('/hit', methods=['POST'])
def increment_hits():
    short_url = request.get_json().get('short_url')

    for item in urls:
        if item['short_url'] == short_url:
            item['hits'] += 1
            return jsonify({"message": "Hit count incremented for " + short_url})

    return jsonify({"error": "Short URL not found"}), 404
    
@app.route('/get-metadata', methods=['GET'])
def get_metadata():
    short_url = request.get_json().get('short_url')

    for item in urls:
        if item['short_url'] == short_url:
            return jsonify(item)

    return jsonify({"error": "Short URL not found"}), 404
    
if __name__ == '__main__':
    app.run(debug=True)
