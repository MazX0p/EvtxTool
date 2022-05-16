import requests
from requests.structures import CaseInsensitiveDict
try:
   from elasticsearch import Elasticsearch
   requier = ''
except:
   requier = None
if requier is None:
   raise NameError("You need to run python3 -m pip install elasticsearch")

try:
   from evtxtoelk import EvtxToElk
   requier = ''
except:
   requier = None
if requier is None:
   raise NameError("You need to run python3 -m pip install evtxtoelk")

def title():
    print('+------------------------------------------')
    print('+  \033[34mBY: http://github.com/MazX0p \\ Mohamed Alzhrani                                    \033[0m')
    print('+  \033[36mpath -> ~/Desktop/test.evtx                                           \033[0m')
    print('+------------------------------------------')

def Elkto(path):
    url2 = "http://localhost:9200/hostlogs"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"mappings": {"hostlogs": {"properties": {"Event.System.TimeCreated.@SystemTime": {"type":"date"}}}}}'
    #EvtxToElk.evtx_to_elk(url,"http://localhost:9200")
    elastic_con = Elasticsearch(hosts=["localhost:9200"])
    #elastic_con.indices.delete(index='hostlogs', ignore=[400, 404])
    #response = elastic_con.indices.delete(index="hostlogs",ignore=[400, 404])
    #if 'acknowledged' in response:
       #if response['acknowledged'] == True:
           #print ("INDEX REFRESH SUCCESS FOR INDEX hostlgs:")
    #elif 'error' in response:
       #print ("ERROR")
    #print ('\nresponse:', response)
    try:
       EvtxToElk.evtx_to_elk(path,"http://localhost:9200")
       print ('\n DONE ADDED THE hostlogs, you should add it to kibana')
    except:
       print ('\n Incorrect Path !')
if __name__ == '__main__':
    title()
    path = input("Enter .evtx Path: \n")
    Elkto(path)
