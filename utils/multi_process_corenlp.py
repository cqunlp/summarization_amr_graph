from multiprocessing import Process, cpu_count
import argparse
import os
def split_list(url_list, cpu_count):
    file_list = []
    with open(url_list,'r',encoding = 'utf-8') as f:
        lines = f.readlines()
        count = len(lines)
        div = int(count / cpu_count)
        # print(count,div,lines)
        for i in range(cpu_count):
            with open(os.path.join(os.path.abspath(os.path.dirname(__file__)),str(i)+'.txt'),'w') as w:
                if i != (cpu_count-1):
                    # print(f.readlines())
                    w.writelines(lines[i* div:(i+1) * div])
                else:
                    w.writelines(lines[i* div:count])
            file_list.append(str(i)+'.txt') 
    
    return file_list 
def rm_list(file_list):
    for i in file_list:
        os.remove(i)

def run_corenlp(file_list,corenlp_path,output_path,counter):
    """
    ./corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref -coref.algorithm neural -filelist path/to/filelist.txt outputFormat xml -outputDirectory /path/to/output/xml
    """
    # print(os.environ)
    # print(os.path.abspath(os.path.dirname(__file__)))
    command = 'java -mx8g -cp ' + '\"{}\"'.format(os.path.join(corenlp_path,'*')) + ' edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref -coref.algorithm neural -threads 2 -filelist ' + os.path.join(os.path.abspath(os.path.dirname(__file__)),file_list) + ' outputFormat xml -outputDirectory ' + output_path
    print(command)
    t = os.popen(command)
    t.readlines()
    # while True:
    #     data = t.readline()
    #     if data == '':
    #         break
    #     if 'done' in data and 'story' in data:
    #         counter += 1
    #         print(counter)
    #     if counter % 100 == 0:
    #         print(counter)
    # print(t.read().split())

def main(url_list,corenlp_path,output_path):
    # cpu_num = cpu_count()
    cpu_num = 1
    file_list = split_list(url_list,cpu_num)
    process_list = []
    counter = 0
    for i in range(cpu_num):
        t = Process(target=run_corenlp, args=(file_list[i],corenlp_path,output_path,counter))
        process_list.append(t)

    for i in process_list:
        i.start()
        # print(os.sched_getaffinity(i.pid))
    for i in process_list:
        i.join()
    
    rm_list(file_list)


    # q = Queue()
    # w = Process(target = add, args = (q,))
    # r = Process(target = read, args = (q,))

    # w.start()
    # r.start()

if __name__ == "__main__":
    """
    ./corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref -coref.algorithm neural -filelist path/to/filelist.txt outputFormat xml -outputDirectory /path/to/output/xml
    """
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument('--url_list',default = '', type = str, help = 'input the path of url_list')
    arg_parse.add_argument('--corenlp',default = '', type = str, help = 'input the path of corenlp')
    arg_parse.add_argument('--output',default = '', type = str, help = 'input the path of output')
    args = arg_parse.parse_args()
    main(args.url_list,args.corenlp,args.output)
