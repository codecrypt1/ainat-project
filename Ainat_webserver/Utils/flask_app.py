import os

from flask import Flask, jsonify, request
from flask_cors import CORS

import boto3
from boto3.dynamodb.conditions import Key, Attr


dynamodb = boto3.resource(
    "dynamodb",
    aws_access_key_id=os.environ.get("ACCESS_KEY"),
    aws_secret_access_key=os.environ.get("SECRET_KEY"),
    region_name=os.environ.get("REGION")
)

app = Flask(__name__)
CORS(app)

@app.route("/signup", methods=["POST"])
def signup() :
    if request.method == "POST" :
        res = request.json
        name = res["Name"]
        email = res["Email"]
        password = res["Password"]
        
        table = dynamodb.Table("users")
        
        table.put_item(
            Item={
                "name": name,
                "email": email,
                "password": password
            }
        )
        
        return jsonify({
            "Status": "Success",
        }), 200
        
        
@app.route("/login", methods=["POST"])
def login() :
    if request.method == "POST" :
        res = request.json
        email = res["Email"]
        password = res["Password"]
        
        table = dynamodb.Table("users")
        response = table.query(
            KeyConditionExpression=Key("email").eq(email)
        )
        items = response["Items"]
        name = items[0]["name"]
        print(items[0]["password"])
        if password == items[0]["password"] :
            return jsonify(
                {
                    "Status": "Success"
                }
            )
        return jsonify({
            "Status": "Failure"
        })
        
if __name__ == "__main__" :
    app.run(debug=True, port=5000)