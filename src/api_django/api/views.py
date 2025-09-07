from email.message import Message
from sys import stderr
from traceback import print_exc

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

from prettyprinter import pformat
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../../.."))
sys.path.append("/home/joech/json-py/src")
from lib.json import parse


def get_encoding_from_headers(content_type: str) -> str:
    msg = Message()
    msg["Content-Type"] = content_type
    return msg.get_param("charset", "utf-8", header="Content-Type")


@api_view(["POST"])
def parse_json(request):
    try:
        body = request.body
        encoding = get_encoding_from_headers(request.META.get("CONTENT_TYPE", ""))
        text = body.decode(encoding)
        result = parse(text)
        pretty = pformat(result, indent=2)
        return HttpResponse(pretty, status=200, content_type="text/plain")
    except Exception as e:
        print("Error:", str(e), file=stderr)
        print_exc(file=stderr)
        return Response(
            {"error": str(e), "code": 400},
            status=status.HTTP_400_BAD_REQUEST,
        )
