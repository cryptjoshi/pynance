from glob import glob
import json
from lib2to3.pgen2 import token
from statistics import quantiles
from sys import api_version
from turtle import color
from flask import Flask,request
from binance.client import Client
import requests,time,datetime,json
from utils import red,green
from main import main

green('starting.....')
url = 'http://localhost:3000/login'
green('Enter Email')
email = input()
green('Enter password')
password = input()
data = {'email': email,'password':password}

app = Flask(__name__)

try:
    headers = {'content-type': 'application/json'}
    res = requests.post(url=url,data=json.dumps(data),headers=headers)
   
    if res.text == 'Invalid':
        red('***********************')
        red('****** Register *******')
        red('***********************')
        red('http://locahost:3000/register')
        quit()
    else:
        green('***********************')
        data = res.json()
        green(data['msg'])
        green('Welcome '+data['username'])
        green('***********************')

except Exception as e:
    red('****** Login not Success ******')
    red(e)
    quit()

@app.route('/',methods=['get'])
def runner():
    return "Welcome to Webhook"

@app.route('/webhook',methods=['POST'])
def webhook():
    global api_key,api_secret,token
    if request.method == 'POST':

        try:
            if request.json['data'] :
                status = request.json['data']
                symbol = request.json['symbol']
                quantity=request.json['quantity']
                leverage =  request.json['leverage']
                tp = request.json['tp']
                sl = request.json['sl']
                green(str('data:'+status))
                green('symbol:'+symbol)
                green('quantity:'+quantity)
                green('leverage:'+leverage)
                green('tp:'+tp)
                green('sl:'+sl)
 
                if status == "buy" or status == "BUY" or status == "Buy" :
                    try:
                        green(status)
                    except:
                        red(status)
        except:
            red('Request Error')
        
        return "Data Received!"
    
app.run(host='0.0.0.0',port=8080)

 