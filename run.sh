python train.py -use_emb 0 -attention 0 -data_name twitter > twitter_emb_0_attn_0.log;
python train.py -use_emb 0 -attention 1 -data_name twitter > twitter_emb_0_attn_1.log;
python train.py -use_emb 1 -attention 0 -data_name twitter > twitter_emb_1_attn_0.log;
python train.py -use_emb 1 -attention 1 -data_name twitter > twitter_emb_1_attn_1.log;