train_data_path = "../textsum/e-data2/finished_files/chunked/train_*"
#valid_data_path = "data/chunked/valid/valid_*"
valid_data_path = "../textsum/e-data_test/finished_files/chunked/val_*"
test_data_path = "data/chunked/test/test_*"
#vocab_path = "data/vocab"
#vocab_path = "data/vocab"
vocab_path = "../textsum/e-data2/finished_files/vocab"
demo_vocab_path = "vocab"
demo_vocab_size = 40000

# Hyperparameters
hidden_dim = 512
emb_dim = 256
batch_size = 10
max_enc_steps = 1000  #99% of the articles are within length 55
max_dec_steps = 20  #99% of the titles are within length 15
beam_size = 4
min_dec_steps = 3
vocab_size = 40000

lr = 0.001
rand_unif_init_mag = 0.02
trunc_norm_init_std = 1e-4

eps = 1e-12
max_iterations = 5000000

#save_model_path = "data/saved_models"
save_model_path = "../pls-data/model"
demo_model_path = ""

intra_encoder = True
intra_decoder = True

cuda = False
