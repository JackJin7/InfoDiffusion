#python train.py -use_emb 0 -attention 0 -data_name twitter > log/twitter_emb_0_attn_0.log;
#python train.py -use_emb 0 -attention 1 -data_name twitter > log/twitter_emb_0_attn_1.log;
#python train.py -use_emb 1 -attention 0 -data_name twitter > log/twitter_emb_1_attn_0.log;
#python train.py -use_emb 1 -attention 1 -data_name twitter > log/twitter_emb_1_attn_1.log;

#python train.py -use_emb 0 -attention 0 -data_name douban > log/douban_emb_0_attn_0.log;
#python train.py -use_emb 0 -attention 1 -data_name douban > log/douban_emb_0_attn_1.log;
#python train.py -gpu 4 -use_emb 1 -attention 0 -data_name douban > log/douban_emb_1_attn_0.log;
#python train.py -gpu 4 -use_emb 1 -attention 1 -data_name douban > log/douban_emb_1_attn_1.log;

python train.py -gpu 4 -w_decay 1e-4 -use_emb 0 -attention 0 -data_name twitter > log/twitter/twitter_emb_0_attn_0_reg.log;
python train.py -gpu 4 -w_decay 1e-4 -use_emb 0 -attention 1 -data_name twitter > log/twitter/twitter_emb_0_attn_1_reg.log;
python train.py -gpu 4 -w_decay 1e-4 -use_emb 1 -attention 0 -data_name twitter > log/twitter/twitter_emb_1_attn_0_reg.log;
python train.py -gpu 4 -w_decay 1e-4 -use_emb 1 -attention 1 -data_name twitter > log/twitter/twitter_emb_1_attn_1_reg.log;

