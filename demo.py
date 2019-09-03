from allennlp.modules.seq2seq_encoders import PytorchSeq2SeqWrapper
from dgl.nn.pytorch import GatedGraphConv

# the gated graph neural network component
# do not need your own implementation, we use dgl

GGNN = PytorchSeq2SeqWrapper(GatedGraphConv(
    in_feats = 128, # equals source_embedding_size = 128
    out_feats = 256, # out_feats equals the GRUCell unit and output
    n_steps = 1, # ggnn_timesteps_per_layer = 1
    n_etypes = 1, # num_edge_type = count_lines(vocabulary) + num_unk_edges
    # num_unk_edges = 1 if allow_unk_edges else 0, default: 1
))
