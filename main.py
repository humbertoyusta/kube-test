import logging
from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(filename='/app/logs/main.log', level=logging.DEBUG)

@app.route('/api')
def hello():
    app.logger.info('API route was accessed')
    return jsonify(
        name="Hello",
        description="Humberto",
        Url=request.url
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4444, debug=True)
