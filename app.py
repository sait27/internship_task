from flask import Flask, request, jsonify

app = Flask(__name__)

FORBIDDEN_CHARS = ["'", "--", ";", "/*", "*/", "#", "\"", "\\"]

FORBIDDEN_KEYWORDS = [
    "SELECT", "INSERT", "UPDATE", "DELETE", 
    "DROP", "CREATE", "ALTER", "EXEC", "UNION", "OR", "AND"
]

@app.route('/v1/sanitized/input/', methods=['POST'])
def sanitize_input():
    data = request.get_json()
    payload = data.get("payload", "")

    if any(char in payload for char in FORBIDDEN_CHARS):
        return jsonify({"result": "unsanitized"})

    if any(keyword in payload.upper() for keyword in FORBIDDEN_KEYWORDS):
        return jsonify({"result": "unsanitized"})

    return jsonify({"result": "sanitized"})


if __name__ == '__main__':
    app.run(debug=True)
