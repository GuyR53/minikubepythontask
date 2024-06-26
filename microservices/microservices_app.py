# microservices/microservices_app.py

import os
import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)

# Route to consume a URL from environment variable, send request, and return response
@app.route('/')
def consume_url():
    # Get URL from environment variable
    url = os.getenv('TARGET_URL')
    if not url:
        return Response('TARGET_URL environment variable is not set', status=500)

    try:
        # Send GET request to the URL
        response = requests.get(url)
        # Return the response content and status code
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.exceptions.RequestException as e:
        return Response(str(e), status=500)


# Readiness probe endpoint
@app.route('/ready')
def readiness_check():
    return jsonify({'status': 'Ready'})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
