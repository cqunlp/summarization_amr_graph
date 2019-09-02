# summarization_amr_graph

1. download [CNN/DM](https://cs.nyu.edu/~kcho/DMQA/) dataset
2. install ```pip install neuralcoref```, some binaryfile errors might occur if you use the latest version of Spacy, if you have same issue, try the command ```pip install spacy==2.1.0```
3. clone the camr repository to parse the resolved sentences. use the bash file ```camr_parse.bash```. this tool need python 2.x version instead of 3.x.
    3.1. before use the bash script, you need download the amr-anno model, follow the commands below:
    ```
    wget http://www.cs.brandeis.edu/~cwang24/files/amr-anno-1.0.train.m.tar.gz
    tar xzf amr-anno-1.0.train.m.tar.gz
    ```
    3.2. you should use java 1.8.x to avoid some problems.

    3.3. you also need install some python wheels
    ```
    pip install bllipparser
    ```

3. jamr or camr to parse text(not decided)
4. TBD..