import json
from datetime import datetime
from database import get_scores


def save_history(scores=None):

    if scores is None:
        scores = get_scores()

    filename = "history.json"

    record = {
        "time": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "results": scores
    }

    try:

        with open(
            filename,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

    except:

        data = []

    data.append(record)

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )

    return "保存成功"

def load_history():

    try:

        with open(
            "history.json",
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        return json.dumps(
            data,
            ensure_ascii=False,
            indent=4
        )

    except:

        return "暂无历史记录"