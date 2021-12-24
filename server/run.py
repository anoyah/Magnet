from flask import Flask
import sys
sys.path.append("../")
from spider.spider import Duo33

app = Flask(__name__)


@app.route("/")
def index():
    Duo33().main()
    return "Hello,world"


app.run("0.0.0.0", 8091)
