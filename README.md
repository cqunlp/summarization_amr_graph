# summarization_amr_graph

This is the re-implementation for the paper : Toward Abstractive Summarization Using Semantic Representations


We will note our develop step in next few months.

## Step1
1. Transform the origin CNN/Daily Mail dataset into AMR format.

    This part will follow the   paper [Automatic Lossless-Summarization](https://www.sciencedirect.com/science/article/pii/S1877050918314522) and its' [repository](https://github.com/ritwikmishra/Lossless-ATS).
2. the problem is that Lossless-ATS do not use the state-of-the-art models to parse text, and alse use python2.x, we will refine the code in the brach [cnndm_to_amr](https://github.com/cqunlp/summarization_amr_graph/tree/cnndm_to_amr)

## Step2
1. In this step, we use allennlp and DGL to re-implement the graph-to-sequence model mentioned in [Structured Neural Summarization](https://github.com/CoderPat/structured-neural-summarization)
2. The code is avaliable in branch [structured_model](https://github.com/cqunlp/summarization_amr_graph/tree/structured_model)

## Step3 
1. graph-to-graph for Molecular
2. internal-graph for text