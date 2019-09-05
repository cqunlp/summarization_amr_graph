# Structured Neural Summarization

<!-- ## Use GCN or GRN -->
## step1

the first thing we need to ensure is that the traning process
1. read arguments and build model (cause the origin version was based on Tensorflow and now we will use Pytorch to achieve the purpose)
    1. Attention layer (BahdanauAttention or Coverage one)
    2. Embedder (args: vocabulary, tokens, embedding_size,dropout_rate.. and so on)
    3. Decoder(basic RNN or others)
    4. Models(Graph2Sequence or SequenceGraph2Sequence)

    so we need define our own Embedder, Decoder and Models.

    Have done:
    1. use GGNN from DGL as the Encoder, the next part is Embedding and Reader

2. the preprocessing speed is too slow (avg 20s/file)
so I have to write a multiprocess tool to speed up that. or if cannot finish in short time, I'll make a distributed tool

The origin [repository](https://github.com/CoderPat/structured-neural-summarization) didn't show all the instruction for data preprocessing, but the utils(.py file) did exist here, I tried it and rewrite the instructions below:
1. clone the [cnn-dailymail](https://github.com/abisee/cnn-dailymail) urls_list repository
2. rename urls list into this kind `{PREFIX}_{TYPE}.txt`, `PREFIX` include `cnn, dailymail`, `TYPE` include `train,val,test`
3. split the origin `.story` file into `.article, .abstr`. (you need install docopt)
    ```
    python splitfiles.py PREFIX path/to/stories path/to/splited/
    ```
4. use stanford corenlp to obtain the parsed `.xml` file
    ```
    ./corenlp.sh -annotators tokenize,ssplit,pos,lemma,ner,parse,depparse,coref -coref.algorithm neural -filelist path/to/filelist.txt outputFormat xml -outputDirectory /path/to/output/xml
    ```