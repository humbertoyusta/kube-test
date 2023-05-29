from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api')
def hello():
    return jsonify(
        name="Hello",
        description="Humberto",
        Url=request.url
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4444, debug=True)