from allennlp.modules.seq2seq_encoders import PytorchSeq2SeqWrapper,Seq2SeqEncoder

from dgl.nn.pytorch import GatedGraphConv
from allennlp.models import Model
from allennlp.modules.text_field_embedders import TextFieldEmbedder
from allennlp.data.vocabulary import Vocabulary
# the gated graph neural network component
# do not need your own implementation, we use dgl

GGNN = PytorchSeq2SeqWrapper(GatedGraphConv(
    in_feats = 128, # equals source_embedding_size = 128
    out_feats = 256, # out_feats equals the GRUCell unit and output
    n_steps = 1, # ggnn_timesteps_per_layer = 1
    n_etypes = 1, # num_edge_type = count_lines(vocabulary) + num_unk_edges
    # num_unk_edges = 1 if allow_unk_edges else 0, default: 1
))

class GraphToSequence(Model):
    def __init__(self,
        embedder : TextFieldEmbedder,
        encoder: Seq2SeqEncoder,
        vocab: Vocabulary
        # there need a abstractive decoder, I do not know how to fix it yet.
    ):
        super.__init__(vocab)
        self.embedder = embedder
        self.encoder = encoder
        
    def forward(self):
        """
        1. embedding the sentence(or just parsed graph) into graph vector
        2. encoder the graph
        3. decoder the encoded graph use LSTM or GRU
        4. return loss
        """
        pass
        
