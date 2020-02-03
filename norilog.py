import json
from flask import Flask,render_template,redirect,request,Markup,escape
from datetime import datetime

application = Flask(__name__)

DATA_FILE = 'norilog.json'


def save_data(start,finish,memo,create_at):
    """

    :param start: 出発
    :param finish: 到着
    :param memo: メモ
    :param create_at:登録日
    """
    try:
        database = json.load(open(DATA_FILE,mode="r",encoding="utf-8"))
    except FileNotFoundError:
        database = []

    database.insert(0,{
        "start":start,
        "finish":finish,
        "memo":memo,
        "created_at":create_at.strftime("%Y-%m-%d %H:%M")
    })

    json.dump(database,open(DATA_FILE,mode="w",encoding="utf-8"),indent=4,ensure_ascii=False)


def load_data():
    try:
        # jsonモジュールでデータベースファイルを開きます
        database = json.load(open(DATA_FILE,mode="r",encoding="utf-8"))
    except FileNotFoundError:
        database = []

    return database


@application.route("/")
def index():
    rides = load_data()

    return render_template("index.html",rides=rides)


@application.route("/save",methods=["POST"])
def save():
    start = request.form.get("start")
    finish = request.form.get("finish")
    memo = request.form.get("memo")
    created_at = datetime.now()

    save_data(start,finish,memo,created_at)

    return redirect("/")


@application.template_filter("nl2br")
def nl2br_filter(s):
    """改行文字をbrタグに置き換えるテンプレートフィルタ"""
    return escape(s).replace("\r","").replace("\n",Markup("<br>"))


if __name__ == "__main__":
    application.run("127.0.0.1",8000,debug=True)

