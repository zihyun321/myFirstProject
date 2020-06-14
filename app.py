from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

# HTML을 주는 부분
@app.route('/map')
def map():
    return render_template('map.html')

#"""
@app.route('/get', methods=['GET'])
def listing():
    # 1. 모든 document 찾기 & _id 값은 출력에서 제외하기
    info = list(db.info.find({},{"_id":False}))

    # 2. info라는 키 값으로 info 내려주기
    return jsonify({'result':'success', 'msg':'GET 연결되었습니다!', 'info': info})


## API 역할을 하는 부분
@app.route('/post', methods=['POST']) #name, address 저장
def save_info():
    name_receive = request.form['name_receive']
    address_receive = request.form['address_receive']
    info = {
        'name' : name_receive,
        'address' : address_receive
    }
    db.info.insert_one(info)
    return jsonify({'result':'success'})
#"""

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)
