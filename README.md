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

