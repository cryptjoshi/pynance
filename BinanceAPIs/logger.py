from fileinput import filename
from typing import final
from clint.textui import colored 
import json
from datetime import date
from datetime import datetime
from os.path import exists
from utils import red,green
import requests

url_line = 'https://notify-api.line.me/api/notify'

class Logger:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self,config):
        self.config = config
        self.url_line = url_line
        self.token = str(self.config['token'])
        self.notify = self.config['notify']
        self.headers = {'Content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ self.token}
  
    def notification(self,msg):
        if self.notify :
            requests.post(self.url_line,headers=self.headers,data= {'messages':msg})
        



    def Log(self,data):
        try:
            logfile = str(date.today())

            file_name = r'Log'+"\\"+data['User']+"-"+logfile+".json"
            exits_file = exists(file_name)
        
            if exits_file == False:
                data = []
                with open(file_name,'w') as _file:
                    json.dump(data,_file)
                    
            list_obj = []
            with open(file_name,encoding='utf-8') as fp:
                list_obj = json.load(fp)
            
            O = {}
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            O.update({'Date': dt_string})
            O.update(data)
            list_obj.append(O)
            
            with open(file_name,'w',encoding='utf-8') as json_file:
                json.dump(list_obj,json_file,indent=4,ensure_ascii=False)
            
            
        except:
            red('Cannot Write or Read')


    def TransactionLog(self,data):
        try:
            logfile = str(date.today())
            
            file_name = r'Transactions'+"\\"+data['User']+"-"+logfile+".json"
            exits_file = exists(file_name)
        
            if exits_file == False:
                data = []
                with open(file_name,'w') as _file:
                    json.dump(data,_file)
                    
            list_obj = []
            with open(file_name,encoding='utf-8') as fp:
                list_obj = json.load(fp)
            
            O = {}
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            O.update({'Date': dt_string})
            O.update(data)
            list_obj.append(O)
            
            with open(file_name,'w',encoding='utf-8') as json_file:
                json.dump(list_obj,json_file,indent=4,ensure_ascii=False)
             
        except:
            red('Cannot Write or Read')


    def Transaction(self,data):
        try:
            
            file_name = r'Transactions'+"\\orderId.json"
            exits_file = exists(file_name)
        
            if exits_file == False:
                data = []
                with open(file_name,'w') as _file:
                    json.dump(data,_file)
                    
            list_obj = []
            with open(file_name,encoding='utf-8') as fp:
                list_obj = json.load(fp)
            
            O = {}
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            O.update({'Date': dt_string})
            O.update(data)
            list_obj.append(O)
            
            with open(file_name,'w',encoding='utf-8') as json_file:
                json.dump(list_obj,json_file,indent=4,ensure_ascii=False)
            self.notification(data['msg'])
            self.TransactionLog(data)
        except:
            red('Cannot Write or Read')
    
