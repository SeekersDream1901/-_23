import os
from function import query
from flask import Flask, request, jsonify


app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query():
    data = request.json
    result = ""
    try:
        for i in (1, len(data) // 2):
            result = query(cmd=data[f"cmd{i}"], value=data[f"value{i}"], file_name=data["file_name"], data=result)
        return jsonify(result)
    except FileNotFoundError:
        return f'Файл {data["file_name"]} не существует'
    except ValueError:
        return f'Команды {data[f"cmd{i}"]} не существует или введены неверные параметры'


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
