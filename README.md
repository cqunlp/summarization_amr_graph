# summarization_amr_graph

This is the re-implementation for the paper : Toward Abstractive Summarization Using Semantic Representations


We will note our develop step in next few months.

## step 1
1. Transform the origin CNN/Daily Mail dataset into AMR format.

    This part will follow the   paper [Automatic Lossless-Summarization](https://www.sciencedirect.com/science/article/pii/S1877050918314522) and its' [repository](https://github.com/ritwikmishra/Lossless-ATS).
2. the problem is that Lossless-ATS do not use the state-of-the-art models to parse text, and alse use python2.x, we will refine the code in the brach[https://github.com/cqunlp/summarization_amr_graph/tree/cnndm_to_amr]