import os

def read_processed_files(file_path):
    processed = set()
    for root,dirs,files in os.walk(file_path):
        for i in files:
            processed.add('/home/lv/splited/train/articles/'+i[0:-4]+'\n')
    return processed

def read_all_files():
    all_files = set()
    processed = read_processed_files('/home/lv/dataset/CNN_DM_graph/processed/splited/train/xml')
    with open('/home/lv/train_urls_list.txt','r',encoding='utf-8') as f:
        for i in f.readlines():
            all_files.add(i)
    remain = all_files-processed
    write_remain_files(remain)

def write_remain_files(remain):
    with open('/home/lv/train_remain.txt','w',encoding='utf-8') as f:
        for i in remain:
            f.write(i)
    f.close()

read_all_files()