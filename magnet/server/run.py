from typing import Optional
from flask import Flask, jsonify, request
from magnet.spider.duo33 import Duo33
import logging

app = Flask(__name__)

logger = logging.getLogger(__name__)


def _response(data):
    return {"code": 200, "msg": data, "status": "success"}


# 统一响应格式
def _suc(words: str, length: int, page: int, data: dict, source: int):
    return _response({
        "source": source,
        "words": words,
        "lenght": length,
        "data": data,
        "page": page,
    })


def _err(msg: str = "Request exception!"):
    return _response(msg)


@app.route("/")
def index():
    r = Duo33().main()
    return jsonify(r)


@app.route("/search")
def search():
    if request.method == "GET":
        words = request.args.get("words", None)
        page = request.args.get("page", 1)
        source = request.args.get("source", 1)
        # 默认获取资源
        if words is None:
            words = "中国纪录片"
        if int(source) == 1:
            r = Duo33().search(words, page)
        return _suc(words, len(r), page, r, source)
    else:
        return _err("request error")


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