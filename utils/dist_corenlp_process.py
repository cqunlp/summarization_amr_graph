import requests
from threading import Thread
from queue import Queue

from typing import List
import argparse
import os
import requests
import time
server_list = [
    '192.168.13.117:9000',
    '192.168.13.103:9000',
    '192.168.13.112:9000',
    '192.168.13.110:9000',
    '192.168.13.131:9000',
    '192.168.13.129:9000',
    '192.168.13.114:9000',
    '192.168.199.213:9000',
    '192.168.199.107:9000',
    '127.0.0.1:9000',
    '202.202.5.140:9000',
    '202.202.5.140:9001',
    '202.202.5.140:9002',
    '202.202.5.140:9003',

    # '172.50.52.147:9000',
]
def annotate_by_command(origin_file,url,stored_file):
    command = "wget --post-file {} \"{}\" -O {}".format(origin_file,url,stored_file)
    t = os.popen(command)
    t = str(t)
    print(t)

def store_file(stored_file,content):
    with open(stored_file ,'wb+') as f:
        f.write(content)
    f.close 

def annotate_by_request(origin_file,url,stored_file):
    url = "http://{}/?properties=%7B'annotators'%3A'tokenize%2Cssplit%2Cpos%2Clemma%2Cner%2Cparse%2Cdepparse%2Ccoref'%2C'coref.algorithm'%3A'neural'%2C'pipelineLanguage'%3A'en'%2C'outputFormat'%3A'xml'%7D".format(url)
    files = {'file':open(origin_file,'rb')}
    
    try:
        r = requests.post(url,files=files)
    except Exception as e:
        print(e,url)
        return 1
    # print(r)
    if r.status_code == 200:
        store_file(stored_file,r.content)
        return 0
    else:
        return 1

def connect_corenlp_server(url):
    url = url + "/?properties={'annotators':'tokenize,ssplit,pos,lemma,ner,parse,depparse,coref','coref.algorithm':'neural','pipelineLanguage':'en','outputFormat':'xml'}"
    return url
def get_stored_file(origin_file,stored_path):
    return os.path.join(stored_path,origin_file.split('/')[-1]+'.xml')

def generate_xml(stored_path,queue,server):
    # queue = Queue(queue)
    times = 0
    while queue.not_empty:
        item = queue.get()
            # url = connect_corenlp_server(server)
        stored_file = get_stored_file(item,stored_path)
            # annotate_one_file(item,url,stored_file)
        time = annotate_by_request(item,server,stored_file)
        times += time
        if time == 1:
            queue.put(item)
        else:
            if time > 0:
                time -= 1
        if times > 10:
            print('break')
            break
def queue_count(queue):
    count = queue.qsize()
    while queue.not_empty:
        time.sleep(60)
        now = queue.qsize()
        print('remain:{},{}/sec'.format(now,(count-now)/60))
        count = now
def read_list(file_path) -> Queue:
    queue = Queue()
    with open(file_path, 'r' ,encoding = 'utf-8') as f:
        for i in f.readlines():
            queue.put(str(i).strip())
    return queue
def main(args):
    queue = read_list(args.file_list)
    thread_list = []
    # for i in range(1):
    for i in range(len(server_list)):
        t = Thread(target=generate_xml,args=(args.stored_path,queue,server_list[i],))
        thread_list.append(t)
    counter = Thread(target=queue_count, args=(queue,))
    thread_list.append(counter)
    for i in thread_list:
        i.start()
    for i in thread_list:
        i.join()
    
    
if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--file_list',default = '',type=str, help='input the file list of the article data')
    arg_parser.add_argument('--stored_path',default = '', type = str, help = 'input the dir you want to store the xml data')
    args = arg_parser.parse_args()
    main(args)
