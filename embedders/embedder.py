from allennlp.modules.token_embedders import Embedding,TokenEmbedder
from allennlp.modules.text_field_embedders import TextFieldEmbedder

# we need make a sub-class for embedder
# the core logic is :
# 

class GraphEmbedder(TextFieldEmbedder):
    def __init__(self):
        pass
    def forward(self):
        pass
    def get_output_dim(self):
        pass