
python run_bert.py \
--model_type bert \
--model_name_or_path bert-large-cased-wwm \
--do_train \
--do_eval \
--data_dir ./data/twitter/data_4 \
--output_dir ./model_bert \
--max_seq_length 64 \
--split_num 1 \
--lstm_hidden_size 512 \
--lstm_layers 1 \
--lstm_dropout 0.1 \
--eval_steps 500 \
--per_gpu_train_batch_size 16 \
--gradient_accumulation_steps 1 \
--warmup_steps 0 \
--per_gpu_eval_batch_size 32 \
--learning_rate 2e-5 \
--adam_epsilon 1e-6 \
--weight_decay 0 \
--train_steps 10000






