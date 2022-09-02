
from flask import Flask,request
from binance.client import Client
import requests,time,json
import os
from colorama import Style
from clint.textui import colored
from os.path import exists
from datetime import date
from datetime import datetime
 
import ntplib
from time import ctime



def RunAsAdmin(path_to_file,*args):
	os.system(r'Powershell -Command "Start-Process "'+path_to_file+'"'+ # CMD running Powershell
				' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
				' -Verb RunAs"' # Run file as administrator
	)

# RunAsAdmin('cmd.exe','arg1','arg2')

def Config_Time(time):
    
    return datetime.strptime(time,"%d/%m/%Y %H:%M:%S")

def convert_time_binance(gt):
    #Converts from Binance Time Format (milliseconds) to time-struct
    #From Binance-Trader Comment Section Code
    #gt = client.get_server_time()
    print("Binance Time: ", gt)
    print(time.localtime())
    aa = str(gt)
    bb = aa.replace("{'serverTime': ","")
    aa = bb.replace("}","")
    gg=int(aa)
    ff=gg-10799260
    uu=ff/1000
    yy=int(uu)
    tt=time.localtime(yy)
    #print(tt)
    return tt

def LogClient(data):
    try:
        New_Name = str(date.today())
        Name_Logfile = New_Name
        File_Name = r'BinanceAPIs\\Client\\Logfile'+"\\"+data['User']+"-"+Name_Logfile+".json"
        file_exits = exists(File_Name)

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
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        C.update({'date and time': dt_string})
        C.update(data)
        listObj.append(C)
        with open(File_Name,'w',encoding='utf-8') as json_file:
            json.dump(listObj,json_file,indent=4,ensure_ascii=False)
    except:
        print(colored.red('LogClient(data) 404'))

def Log(data):
    try:
        New_Name = str(date.today())
        Name_Logfile = New_Name
        File_Name = r'BinanceAPIs\\Master\\Logfile'+"\\"+data['User']+"-"+Name_Logfile+".json"
        file_exits = exists(File_Name)
      
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
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        C.update({'date and time': dt_string})
        C.update(data)
        listObj.append(C)
        
        with open(File_Name,'w',encoding='utf-8') as json_file:
            json.dump(listObj,json_file,indent=4,ensure_ascii=False)
    except:
        print(colored.red('Log(data) 404'))

def main():

    Log({'User':'Master','Msg': 'RUN BOT ...'})

    # c = ntplib.NTPClient()
    # response = c.request('time2.navy.mi.th')

    # try:
    #     import nntplib
    #     c = ntplib.NTPClient()
    #     response = c.request('pool.ntp.org')
    #     print(Config_Time(str(ctime(response.tx_time))))
    #     #print('time '+ str(Config_Time(str(ctime(response.tx_time)))))
    #     #os.system('time '+ str(Config_Time(str(ctime(response.tx_time)))))

    # except:
    #     print(colored.red('Could not sync with time server'))
    #     print(colored.red('Please run as administrator...'))
    #     input()
    #     quit()

    #####################################
    #### check Master File Config    ####
    #####################################

    file_exits = exists(r'BinanceAPIs\Master\BinanceAPIs.txt')

    if file_exits == False:
        print(colored.red('FileNotFoundError: BinanceAPIs.txt'))
        Log({
            'User': 'Master',
            'Msg':'FileNotFoundError BinanceAPIs.txt'})
        input()
        quit()

    # check Logfile OrderId

    file_exits = exists(r'BinanceAPIs\Master\Logfile\orderId.txt')

    if file_exits == False:
        print(colored.red('FileNotFoundError: Master\Logfile\orderId.txt'))
        Log({
            'User': 'Master',
            'Msg':'FileNotFoundError: Master\Logfile\orderId.txt'})
        input()
        quit()

   

    # file_exits = exists(r'BinanceAPIs\BinanceAPIs.txt')

    # if file_exits == False:
    #     print(colored.red('FileNotFoundError BinanceAPIs.txt'))
    #     Log({'Msg':'FileNotFoundError BinanceAPIs.txt'})
    #     input()
    #     quit()

    # file_exits = exists(r'BinanceAPIs\Config.txt')

    # if file_exits == False:
    #     print(colored.red('FileNotFoundError Config.txt'))
    #     Log({'Msg':'FileNotFoundError Config.txt'})
    #     input()
    #     quit()

    # config={}
    # try:
    #     with open(r'BinanceAPIs\Config.txt') as fh:
    #         for line in fh:
    #             command,description = line.strip().split(None,1)
    #             config[command] = description.strip()
    # except:
    #     pass

    # Api_Key_line = {}
    # try:
    #     with open(r'BinanceAPIs\BinanceAPIs.txt') as fh:
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
                C.update({lines[i].split()[0]:lines[i].split()[1]})
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

        os.system('w32tm/resync')
        
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
                Log({'User':'Master','Ask_time' : str(free_time)})
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
    
    app = Flask(__name__)
    
    @app.route(Config['webhook'],methods=['POST'])
    def webhook():
        return
    
if __name__ == '__main__':
    main()
