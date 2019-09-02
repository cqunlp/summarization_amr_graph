import spacy

# load NeuralCoref and add it to the pipe of SpaCy's model
import neuralcoref
import argparse

def read_file(file_path):
    text = ''
    with open(file_path,'r',encoding='utf-8') as f:
        for i in f.readlines():
            text += str(i)
    return text

def coref_resolution(source,target):
    nlp = spacy.load('en')
    coref = neuralcoref.NeuralCoref(nlp.vocab)
    nlp.add_pipe(coref, name='neuralcoref')

    source_text = read_file(source)
    target_text = read_file(target)
# You're done. You can now use NeuralCoref the same way you usually manipulate a SpaCy document and it's annotations.
    source_doc = nlp(source_text)
    target_doc = nlp(target_text)

    return source_doc._.coref_resolved, target_doc._.coref_resolved

def save_file(text,file_name):
    with open(file_name,'w',encoding='utf-8') as f:
        f.write(text)
    f.close

def main():
    arg_parser = argparse.ArgumentParser(description='Input file is article text and abstract text')
    arg_parser.add_argument('-s','--source',type=str,help='the source file is a txt containing the article text')
    arg_parser.add_argument('-t','--target',type=str,help='the target file is a txt containing the abstract text')

    args = arg_parser.parse_args()

    source, target = coref_resolution(args.source,args.target)
    
    save_file(source,'source_resolved')
    save_file(target,'target_resolved')
    # print(source)
    # print(target)

    
if __name__ == "__main__":
    main()