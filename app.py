from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():
    title = request.form['title']
    content = request.form['content']
    doc = {
        'title': title,
        'content': content
    }
    db.user.insert_one(doc)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    all = list(db.user.find({},{'_id':False}))
    return {"result": all}


@app.route('/post', methods=['DELETE'])
def delete_post():
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)