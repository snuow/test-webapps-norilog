import json

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