
from flask import Flask,request
from binance.client import Client
import requests,time,json
import os
from colorama import Style
from clint.textui import colored
from os.path import exists
from datetime import date
import datetime
import ntplib
from time import ctime

print(colored.green('---------------------'))
print(colored.green('welcome to Binance_Futures_v_users_2.8'))
print(colored.green('by Meew Punk'))
print(colored.green('Facebook: Srang Srrkh'))
print(colored.green('https://www.facebook.com/SrangSrrkh'))


def RunAsAdmin(path_to_file,*args):
	os.system(r'Powershell -Command "Start-Process "'+path_to_file+'"'+ # CMD running Powershell
				' -ArgumentList @('+str(args)[1:-1]+')'+ # Arguments. [1:-1] to remove brackets
				' -Verb RunAs"' # Run file as administrator
	)

# RunAsAdmin('cmd.exe','arg1','arg2')

def Config_Time(time):
    return datetime.strptime(time,"%H:%M:%s")

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
        dt_string = now.strftime("%d/%m/%Y %H:%M:%s")
        C.update({'date and time': dt_string})
        C.update(data)

        listObj.append(C)
        with open(File_Name,'w',encoding='utf-8') as json_file:
            json.dump(listObj,json_file,indent=4,ensure_ascii=False)
    except:
        print(colored.red('Log(data) 404'))

def convert(date_time):
    format = '%b %d %Y %I:%M%p'  # The format
    datetime_str = datetime.datetime.strptime(date_time, format)
 
    return datetime_str
 
 
# Driver code
date_time = 'Dec 4 2018 10:07AM'
print(convert(date_time))

def main():

    Log({'Msg': 'RUN BOT ...'})

    c = ntplib.NTPClient()
    response = c.request('time2.navy.mi.th')

    try:
        import nntplib
        c = ntplib.NTPClient()
        response = c.request('pool.ntp.org')
        #print(Config_Time(str(ctime(response.tx_time))))
        os.system('time '+ str(Config_Time(str(ctime(response.tx_time)))))

    except:
        print(colored.red('Could not sync with time server'))
        print(colored.red('Please run as administrator...'))
        input()
        quit()

    file_exits = exists(r'BinanceAPIs\BinanceAPIs.txt')

    if file_exits == False:
        print(colored.red('FileNotFoundError BinanceAPIs.txt'))
        Log({'Msg':'FileNotFoundError BinanceAPIs.txt'})
        input()
        quit()

    file_exits = exists(r'BinanceAPIs\Config.txt')

    if file_exits == False:
        print(colored.red('FileNotFoundError Config.txt'))
        Log({'Msg':'FileNotFoundError Config.txt'})
        input()
        quit()

    config={}
    try:
        with open(r'BinanceAPIs\Config.txt') as fh:
            for line in fh:
                command,description = line.strip().split(None,1)
                config[command] = description.strip()
    except:
        pass

    Api_Key_line = {}
    try:
        with open(r'BinanceAPIs\BinanceAPIs.txt') as fh:
            for line in fh:
                command,description = line.strip().split(None,1)
                Api_Key_line[command] = description.strip()
    except:
        pass

    Line_token = str(Api_Key_line['token'])
    url_line = 'https://notify-api.line.me/api/notify'
    headers = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ Line_token}

    Api_key = {}
    try:
        with open(r'BinanceAPIs\BinanceAPIs.txt') as fh:
            for line in fh:
                command,description = line.strip().split(None,1)
                Api_key[command] = description.strip()
    except:
        pass


if __name__ == '__main__':
    main()
