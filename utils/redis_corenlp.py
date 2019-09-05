import redis
import stanfordnlp
import os
from multiprocessing import Process
import argparse
from signal import signal, SIGINT,SIGTERM
from sys import exit

def annotate_one_file(file_path,url):
    command = "wget --post-file {} \"{}\" -O test.story.xml".format(file_path,url)
    os.system(command)


def connect_redis(ip,port):
    r = redis.Redis(host=ip,port=port)
    return r

def connect_corenlp_server(ip,port):
    url = "{}:{}/?properties={'annotators':'tokenize,ssplit,pos,lemma,ner,parse,depparse,coref','coref.algorithm':'neural','pipelineLanguage':'en','outputFormat':'xml'}".format(ip,port)
    
def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)

def main():
    
    while 1:
        pass

if __name__ == "__main__":
    signal(SIGINT, handler)
    signal(SIGTERM, handler)
    main()
