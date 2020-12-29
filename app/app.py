from typing import List, Dict
from flask import Flask
import mysql.connector
import json

app = Flask(__name__)


def favorite_foods() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'foods'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM food')
    # results = [{item: price} for (item, price) in cursor]

    results = ''
    for(items,price) in cursor:
        results += items+" "+ price+"<br>"
    cursor.close()
    connection.close()

    return results


@app.route('/')
def index() -> str:
    # return json.dumps({'favorite_food_items': favorite_emps()})
    return favorite_foods()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
