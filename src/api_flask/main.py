from email.message import Message
from sys import stderr
from traceback import print_exc

from flask import Flask, request, Response, jsonify

from prettyprinter import pformat
from src.lib.json import parse


def get_encoding_from_headers(content_type: str) -> str:
    msg = Message()
    msg["Content-Type"] = content_type
    return msg.get_param("charset", "utf-8", header="Content-Type")


app = Flask(__name__)


@app.route("/api/v1/parse", methods=["POST"])
def parse_json():
    try:
        body = request.get_data()
        encoding = get_encoding_from_headers(request.headers.get("Content-Type", ""))
        text = body.decode(encoding)
        result = parse(text)
        pretty = pformat(result, indent=2)
        return Response(pretty, status=200, mimetype="text/plain")
    except Exception as e:
        print("Error:", str(e), file=stderr)
        print_exc(file=stderr)
        return jsonify({"error": str(e), "code": 400}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
