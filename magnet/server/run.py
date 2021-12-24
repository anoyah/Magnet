from typing import Optional
from flask import Flask, jsonify, request
from magnet.spider.duo33 import Duo33
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)


@app.route("/")
def index():
    r = Duo33().main()
    return jsonify(r)


@app.route("/search")
def search():
    # if request.method == "get":
    words = request.args.get("words", None)
    if words is None:
        words = "中国纪录片"
    r = Duo33().search(words)
    return jsonify({
        "words": words,
        "lenght": len(r),
        "data": r,
    })


def run(port: int):
    if port is None:
        port = 8091
    try:
        port = int(port)
    except Exception as exception:
        logger.error(f"{exception}")
        raise TypeError("port error")
    if isinstance(port, int):
        app.run("0.0.0.0", port)
    else:
        raise TypeError("port needs int tpye.")