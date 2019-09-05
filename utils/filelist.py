import os
import argparse

def _generate_urls_list(file_path,type):
    f = open(type+'_urls_list.txt','w',encoding = 'utf-8')
    for root,dirs,files in os.walk(file_path):
        for i in files:
            # print(i)
            if 'article' in i:
                f.write(os.path.join(root,i)+'\n')
                # break

    f.close()


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--path',default = '',type = str ,help = 'The source cnn/dailymail dataset story path')
    arg_parser.add_argument('--type', default = 'train', type = str, help = 'dataset type, use train,val,test')
    args = arg_parser.parse_args()
    _generate_urls_list(args.path,args.type)
    