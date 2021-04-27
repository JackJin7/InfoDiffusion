python train.py -gpu 6 -attention 0 -data_name memetracker > log/memetracker/memetracker_attn_0.log;
python train.py -gpu 6 -attention 1 -data_name memetracker > log/memetracker/memetracker_attn_1.log;
python train.py -gpu 6 -w_decay 1e-4 -attention 0 -data_name memetracker > log/memetracker/memetracker_attn_0_reg.log;
python train.py -gpu 6 -w_decay 1e-4 -attention 1 -data_name memetracker > log/memetracker/memetracker_attn_1_reg.log;
