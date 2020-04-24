import json
from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    """
    :return:response
    """
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!"
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
