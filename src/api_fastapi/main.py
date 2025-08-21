from email.message import Message
from sys import stderr
from traceback import print_exc

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse

from prettyprinter import pformat
from src.lib.json import parse


def get_encoding_from_headers(content_type: str) -> str:
    msg = Message()
    msg["Content-Type"] = content_type
    return msg.get_param("charset", "utf-8", header="Content-Type")


app = FastAPI()


@app.post("/api/v1/parse")
async def parse_json(request: Request):
    try:
        body = await request.body()
        encoding = get_encoding_from_headers(request.headers.get("content-type", ""))
        text = body.decode(encoding)
        result = parse(text)
        pretty = pformat(result, indent=2)
        return PlainTextResponse(pretty, status_code=200)
    except Exception as e:
        print("Error:", str(e), file=stderr)
        print_exc(file=stderr)
        return JSONResponse(
            status_code=400, content={"ok": False, "error": str(e), "code": 400}
        )


def start():
    import uvicorn

    uvicorn.run("src.api_fastapi.main:app", host="127.0.0.1", port=8000, reload=True)
