
from http import client
from lzma import FORMAT_AUTO
from pickle import TRUE
from statistics import LinearRegression
from turtle import color, position
from flask import Flask,request
from binance.client import Client
import requests,time,json
from os import path
from colorama import Style
from clint.textui import colored
import os.path
from datetime import datetime
from datetime import date
import ntplib
from time import ctime

print(colored.green('---------------------'))
print(colored.green('welcome to Binance_Futures_v_users_2.8'))
print(colored.green('by Meew Punk'))
print(colored.green('Facebook: Srang Srrkh'))
print(colored.green('https://www.facebook.com/SrangSrrkh'))

def Config_Time(times):
    return time.strftime ("%x",times)
    

def LogClient(data):
    try:
        New_Name = str(date.today())
        Name_Logfile = New_Name
        File_Name = r'BinanceAPIs\\Client\\Logfile'+"\\"+data['User']+"-"+Name_Logfile+".json"
        file_exits = os.path.exists(File_Name)

        if file_exits == False:
            Create_file = [

            ]
            with open(File_Name,'w') as outfile:
                json.dump(Create_file,outfile)
        listObj = []
        with open(File_Name,encoding='utf-8') as fp:
            listObj = json.load(fp)

        C = {}
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%s")
        C.update({'date and time': dt_string})
        C.update(data)

        listObj.append(C)
        with open(File_Name,'w',encoding='utf-8') as json_file:
            json.dump(listObj,json_file,indent=4,ensure_ascii=False)
    except:
        print(colored.red('Log(data) 404'))

def Log(data):
    try:
        New_Name = str(date.today())
        Name_Logfile = New_Name
        File_Name = r'BinanceAPIs\\Master\\Logfile'+"\\"+data['User']+"-"+Name_Logfile+".json"
        file_exits = os.path.exists(File_Name)

        if file_exits == False:
            Create_file = [

            ]
            with open(File_Name,'w') as outfile:
                json.dump(Create_file,outfile)
        listObj = []
        with open(File_Name,encoding='utf-8') as fp:
            listObj = json.load(fp)

        C = {}
        
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%s")
        C.update({'date and time': dt_string})
        C.update(data)

        listObj.append(C)
        with open(File_Name,'w',encoding='utf-8') as json_file:
            json.dump(listObj,json_file,indent=4,ensure_ascii=False)
    except:
        print(colored.red('Log(data) 404'))


Log({
    'User': 'Master',
    'Msg': 'Run Bot Binance Futures CopyTrade'
})


#####################################
#### check sync with Time Server ####
#####################################

c = ntplib.NTPClient()
response = c.request('time2.navy.mi.th')

try:
    import nntplib
    c = ntplib.NTPClient()
    response = c.request('pool.ntp.org')
    print(str(ctime(response.tx_time)))
    #os.system('time'+ str(Config_Time(str(ctime(response.tx_time)))))

except:
    print(colored.red('Could not sync with time server'))
    print(colored.red('Please run as administrator...'))
    input()
    quit()


#####################################
#### check Master File Config    ####
#####################################

file_exits = os.path(r'BinanceAPIs\Master\BinanceAPIs.txt')

if file_exits == False:
    print(colored.red('FileNotFoundError: BinanceAPIs.txt'))
    Log({
        'User': 'Master',
        'Msg':'FileNotFoundError BinanceAPIs.txt'})
    input()
    quit()

# check Logfile OrderId

file_exits = os.path(r'BinanceAPIs\Master\Logfile\orderId.txt')

if file_exits == False:
    print(colored.red('FileNotFoundError: Master\Logfile\orderId.txt'))
    Log({
        'User': 'Master',
        'Msg':'FileNotFoundError: Master\Logfile\orderId.txt'})
    input()
    quit()





file_exits = os.path(r'BinanceAPIs\Master\Config.txt')

if file_exits == False:
    print(colored.red('FileNotFoundError: BinanceAPIs\Master\Config.txt'))
    Log({
        'User': 'Master',
        'Msg':'FileNotFoundError: BinanceAPIs\Master\config.txt'})
    input()
    quit()

# config={}
# try:
#     with open(r'BinanceAPIs\Master\Config.txt') as fh:
#         for line in fh:
#             command,description = line.strip().split(None,1)
#             config[command] = description.strip()
# except:
#     pass

# Api_Key_line = {}
# try:
#     with open(r'BinanceAPIs\Master\BinanceAPIs.txt') as fh:
#         for line in fh:
#             command,description = line.strip().split(None,1)
#             Api_Key_line[command] = description.strip()
# except:
#     pass


#### convert txt to json

with open(r'BinanceAPIs\Master\BinanceAPIs.txt',encoding='utf-8') as f:
    lines = f.readlines()

C = {}
listObj = []
i = 0

while True:
    try:
        if lines[i].split()[0] != '':
            C.update({lines[i].split()[]:lines[i].split()[1]})
            i +=1
    except:
        listObj.append(C)
        with open(r'BinanceAPIs\Master\BinanceAPIs.json','w',encoding='utf-8') as f:
            json.dump(listObj,f,indent=4,ensure_ascii=False)

        i+=1
        C = {}

        try:
            lines[i].split()[0]
        except:
            break

#### read json store on object
listAPI = []
with open(r'BinanceAPIs\Master\BinanceAPIs.json',encoding='utf-8') as fp:
     listAPI = json.load(fp)

# Api_Key_line = {}
# try:
#     with open(r'BinanceAPIs\Master\BinanceAPIs.txt') as fh:
#         for line in fh:
#             command,description = line.strip().split(None,1)
#             Api_Key_line[command] = description.strip()
# except:
#     pass

Line_token = str(listAPI[0]['token'])
url_line = 'https://notify-api.line.me/api/notify'
headers = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ Line_token}
api_key = str(listAPI[0]['api_key'])
api_secret = str(listAPI[0]['api_secret'])
client = Client(api_key,api_secret)
local_time1 = int(time.time()*1000)
server_time = client.get_server_time()
free_time = server_time['serverTime'] - local_time1


print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
print('ServerTime:',server_time['serverTime'])
print('Local_time:',local_time1)
print('Ask_time:',free_time)


if float(free_time) <= -1000 or float(free_time)>= 1000:
    print(colored.red('Sync Time in windows ...'))

    Log({
        'User':'Master',
        'Sync Time in Windows': str(free_time)
    })

    while True:
        time.sleep(1)
        local_time1 = int(time.time()*1000)
        server_time = client.get_server_time()
        free_time = server_time['serverTime'] - local_time1

        if float(free_time) <= -1000 or float(free_time) >= 1000:
            pass
    
        else:
            print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
            print('ServerTime:',server_time['serverTime'])
            print('Local_time:',local_time1)
            print('Ask_time:',free_time)
            Log({'Ask_time' : str(free_time)})
            print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
            break

print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))

No = 1 
for lineAPI in listAPI:

    api_key = str(lineAPI['api_key'])
    api_secret = str(lineAPI['api_secret'])
    client = Client(api_key,api_secret)

    Line_token = str(lineAPI['token'])
    url_line = 'https://notify-api.line.me/api/notify'
    headers = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ Line_token}

    try:
        balance_USDT = round(float(client.futures_account_balance()[6]['balance']),2)
        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print(colored.green('No. :'+str(No)))
        print(colored.green('APIs :'+'Master'))
        print(colored.green('User :'+str(lineAPI['User'])))
        print(colored.green('Balance_future UDST :'+ str(balance_USDT)))
        print(colored.green('Balance_API Status :'+ 'Normal'))
        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        No +=1

        Log({
            'User': str(lineAPI['User']),
            'Balance_Furture USDT': str(balance_USDT),
            'Balance_API Status': 'Normal'
        })
    except:
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print(colored.red('No. :'+str(No)))
        print(colored.red('User :'+str(lineAPI['User'])))
        print(colored.red('Balance_API Status :'+ 'Invalid'))
        print(colored.red('api_key :'+ str(lineAPI['api_key'])))
        print(colored.red('api_secret Status :'+str(lineAPI['api_secret'])))
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        No +=1

        Log({
            'User': str(lineAPI['User']),
            'Balance_API Status:': 'Invalid'
        })

        mag = 'Balance_API Status: Invalid'
        requests.post(url_line,headers=headers,data= {'messages':msg})
        input('')
        quit()


################################################################
#####  Client
####  convert client txt to json
##################################################################
with open(r'BinanceAPIs\Client\BinanceAPIs.txt',encoding='utf-8') as f:
    lines = f.readlines()

C = {}
listObj = []
i = 0

while True:
    try:
        if lines[i].split()[0] != '':
            C.update({lines[i].split()[]:lines[i].split()[1]})
            i +=1
    except:
        listObj.append(C)
        with open(r'BinanceAPIs\Client\BinanceAPIs.json','w',encoding='utf-8') as f:
            json.dump(listObj,f,indent=4,ensure_ascii=False)

        i+=1
        C = {}

        try:
            lines[i].split()[0]
        except:
            break

listAPI_Client = []
with open(r'BinanceAPIs\Client\BinanceAPIs.json',encoding='utf-8') as fp:
     listAPI_Client = json.load(fp)

No = 1 
for lineAPI_Client in listAPI_Client:

    api_key = str(lineAPI_Client['api_key'])
    api_secret = str(lineAPI_Client['api_secret'])
    client = Client(api_key,api_secret)

    Line_token = str(lineAPI_Client['token'])
    url_line = 'https://notify-api.line.me/api/notify'
    headers = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ Line_token}

    try:
        balance_USDT = round(float(client.futures_account_balance()[6]['balance']),2)
        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print(colored.green('No. :'+str(No)))
        print(colored.green('APIs :'+'Master'))
        print(colored.green('User :'+str(lineAPI_Client['User'])))
        print(colored.green('Balance_future UDST :'+ str(balance_USDT)))
        print(colored.green('Balance_API Status :'+ 'Normal'))
        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        No +=1

        LogClient({
            'User': str(lineAPI_Client['User']),
            'Balance_Furture USDT': str(balance_USDT),
            'Balance_API Status': 'Normal'
        })
    except:
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print(colored.red('No. :'+str(No)))
        print(colored.red('User :'+str(lineAPI_Client['User'])))
        print(colored.red('Balance_API Status :'+ 'Invalid'))
        print(colored.red('api_key :'+ str(lineAPI_Client['api_key'])))
        print(colored.red('api_secret Status :'+str(lineAPI_Client['api_secret'])))
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        No +=1

        LogClient({
            'User': str(lineAPI_Client['User']),
            'Balance_API Status:': 'Invalid'
        })

        mag = 'Balance_API Status: Invalid'
        requests.post(url_line,headers=headers,data= {'messages': msg})
        input('')
        quit()

def Main():
    
    def BUY(User,symbol,leverage,quantity):
        try:
            SidePosition = client.futures_get_position_mode()
            if SidePosition['dualSidePosition'] == False:
                client.futures_change_leverage(symbol=symbol,leverage=leverage)
                order = client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='BUY',
                    quantity=quantity)
            
             if SidePosition['dualSidePosition'] == True:
                client.futures_change_leverage(symbol=symbol,leverage=leverage)
                order = client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='BUY',
                    positionSide= "LONG",
                    quantity=quantity)
            
            if order:
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                print(colored.green('Success Create_Order BUY/LONG'))
                print(colored.green('orderId'+' '+ str(order['orderId'])))
                print(colored.green('symbol'+' '+ str(order['symbol'])))
                print(colored.green('origQty'+' '+ str(order['origQty'])))
                print(colored.green('side'+' '+ str(order['side'])))
                print(colored.green('leverage'+' '+ str(leverage)))
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))

                msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity) + '\n side :'+ str(order['side'])
                requests.post(url_line,headers=headers,data={'message': msg})

                log_data = {
                    'User' : User,
                    'Stu' : 'Order Success',
                    'symbol': symbol,
                    'quantity': quantity,
                    'side': order['side'],
                    'leverage': leverage,
                    'orderId' : order['orderId']
                }
                LogClient(log_data)

                with open(r'BinanceAPIs\Master\Logfile\orderId.txt','a') as f:
                    f.write(str(order['orderId'])+'\n')

            print(colored.red('-------------------------------------------'))
            print('')
        
        except:
            msg = 'Order Unsuccess'
            requests.post(url_line,headers=headers,data={'message': msg})
            print(colored.red('-------------------------------------------'))
            print(colored.red('ERROR Create_Order BUY'))
            print(colored.red('-------------------------------------------'))
      
            log_data = {
                'User': User,
                'stu' : 'Order Unsuccess'
            }
            LogClient(log_data)

    def SELL(User,symbol,leverage,quantity):
        try:
            SidePosition = client.futures_get_position_mode()
            if SidePosition['dualSidePosition'] == False:
                client.futures_change_leverage(symbol=symbol,leverage=leverage)
                order = client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='SELL',
                    quantity=quantity)
            
            if SidePosition['dualSidePosition'] == True:
                client.futures_change_leverage(symbol=symbol,leverage=leverage)
                order = client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='SELL',
                    positionSide= "SHORT",
                    quantity=quantity)
            
            if order:
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                print(colored.green('Success Create_Order SELL/SHORT'))
                print(colored.green('orderId'+' '+ str(order['orderId'])))
                print(colored.green('symbol'+' '+ str(order['symbol'])))
                print(colored.green('origQty'+' '+ str(order['origQty'])))
                print(colored.green('side'+' '+ str(order['side'])))
                print(colored.green('leverage'+' '+ str(leverage)))
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))

                msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity) + '\n side :'+ str(order['side'])
                requests.post(url_line,headers=headers,data={'message': msg})

                log_data = {
                    'User' : User,
                    'Stu' : 'Order Success',
                    'symbol': symbol,
                    'quantity': quantity,
                    'side': order['side'],
                    'leverage': leverage,
                    'orderId' : order['orderId']
                }
                LogClient(log_data)

                with open(r'BinanceAPIs\Master\Logfile\orderId.txt','a') as f:
                    f.write(str(order['orderId'])+'\n')

            print(colored.red('-------------------------------------------'))
            print('')
        
        except:
            msg = 'Order Unsuccess'
            requests.post(url_line,headers=headers,data={'message': msg})
            print(colored.red('-------------------------------------------'))
            print(colored.red('ERROR Create_Order BUY'))
            print(colored.red('-------------------------------------------'))
      
            log_data = {
                'User': User,
                'stu' : 'Order Unsuccess'
            }
            LogClient(log_data)
    
    def Close_Order_Buy(User,symbol,quantity):
        SidePosition = client.futures_get_position_mode()
        if SidePosition['dualSidePosition'] == False:
            try:
                try:       
                    order = client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='SELL',
                    quantity=quantity)
                    if order:
                        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                        print(colored.green('Success Close_Order BUY'+ str(quantity)))
                        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                        msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity)
                        requests.post(url_line,headers=headers,data={'message': msg})

                        log_data = {
                            'User' : User,
                            'Stu' : 'Order Success',
                            'symbol': str(symbol),
                            'quantity': str(quantity)
                        }
                        LogClient(log_data)

                except:
                    pass
            except:
                pass
        
        if SidePosition['dualSidePosition'] == True:
            try:
                try:       
                    order = client.futures_create_order(
                    symbol=symbol,
                    type= Client.ORDER_TYPE_MARKET,
                    positionSide='LONG',
                    side='SELL',
                    quantity=quantity)
                    if order:
                        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                        print(colored.green('Success Close_Order BUY'+ str(quantity)))
                        print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                        msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity)
                        requests.post(url_line,headers=headers,data={'message': msg})

                        log_data = {
                            'User' : User,
                            'Stu' : 'Order Success',
                            'symbol': str(symbol),
                            'quantity': str(quantity)
                        }
                        LogClient(log_data)

                except:
                    pass
            except:
                pass
        
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print('')
        print('')
    
    def Close_Order_SELL(User,symbol,quantity):
        SidePosition = client.futures_get_position_mode()
        if SidePosition['dualSidePosition'] == False:
            try:
                try:       
                    client.futures_create_order(
                    symbol=symbol,
                    type='MARKET',
                    side='BUY',
                    quantity=quantity,reduceOnly=True)
                except:
                    pass
                msg = 'Sell_short'
                requests.post(url_line,headers=headers,data={'message': msg})

                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                print(colored.green('Success Close_Order SELL'))
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity)
                requests.post(url_line,headers=headers,data={'message': msg})
                log_data = {
                    'User' : User,
                    'Stu' : 'Order Success',
                    'symbol': str(symbol),
                    'quantity': str(quantity)
                }
                LogClient(log_data)

            except:
                    pass
        
        if SidePosition['dualSidePosition'] == True:
            try:
                try:       
                    order = client.futures_create_order(
                    symbol=symbol,
                    type= Client.ORDER_TYPE_MARKET,
                    positionSide='SHORT',
                    side='BUY',
                    quantity=quantity)
                except:
                    pass
                msg = 'Sell_short'
                requests.post(url_line,headers=headers,data={'message': msg})
                     
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                print(colored.green('Success Close_Order SELL'))
                print(colored.green('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
                msg = 'Order Success \n Asset :' + str(symbol) + ' \n Quantity :' + str(quantity)
                requests.post(url_line,headers=headers,data={'message': msg})

                log_data = {
                    'User' : User,
                    'Stu' : 'Order Success',
                    'symbol': str(symbol),
                    'quantity': str(quantity)
                }
                LogClient(log_data)

            except:
                pass
        
        
        print(colored.red('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))
        print('')
        print('')
    
    def Create_Order_File(data):

        try:
            New_Name = str(date.today())
            Name_Logfile = New_Name
            File_Name = r'BinanceAPIs\\Master\\Create_Order_File\\Order_File.json'
            file_exits = os.path.exists(File_Name)

            if file_exits == False:
                Create_file = [

                ]
                with open(File_Name,'w') as outfile:
                    json.dump(Create_file,outfile)
            listObj = []
            with open(File_Name,encoding='utf-8') as fp:
                listObj = json.load(fp)

            C = {}
            
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%s")

            def GenerateCode():
                digits = "0123456790"
                OTP = ""

                for i in range(6):
                    OTP += digits[math.floor(random.random()*10)]

                return OTP
            
            C.update({'Time and Date': dt_string})
            C.update({'ID_Code': GenerateCode()})
            C.update(data)

            listObj.append(C)
            with open(File_Name,'w',encoding='utf-8') as json_file:
                json.dump(listObj,json_file,indent=4,ensure_ascii=False)
        except:
            print(colored.red('Log(data) 404'))
    
    # if __name__ == '__main__':
    #     app.run(host='0.0.0.0',port=int(Config['Port']))
        
    