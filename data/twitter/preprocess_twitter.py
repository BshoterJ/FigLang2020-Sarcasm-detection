# -*- coding:utf-8 -*-

import os
import jsonlines
import csv
import pandas as pd
import random


data = []

with open("sarcasm_detection_shared_task_twitter_training.jsonl","r+",encoding='utf-8') as f:
    for item in jsonlines.Reader(f):
        if item['label'] == 'SARCASM':
            item['label'] = 0
        else:
            item['label'] = 1

        data.append(item)

with open('twitter.csv', 'w+', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_head = ['context', 'response', 'label']
    csv_writer.writerow(csv_head)

    for i in range(len(data)):
        data_row = [(''.join(data[i]['context'])).replace('@USER', '').replace('<URL>',''),
                    (data[i]['response']).replace('@USER', '').replace('<URL>',''), data[i]['label']]
        csv_writer.writerow(data_row)


total = pd.read_csv("twitter.csv")

index = set(range(total.shape[0]))
K_fold = []
for i in range(5):
    if i == 4:
        tmp = index
    else:
        tmp = random.sample(index, int(1.0 / 5 * total.shape[0]))
    index = index - set(tmp)
    print("Number:", len(tmp))
    K_fold.append(tmp)

for i in range(5):
    print("Fold", i)
    os.system("mkdir data_{}".format(i))
    dev_index = list(K_fold[i])
    train_index = []
    for j in range(5):
        if j != i:
            train_index += K_fold[j]
    total.iloc[train_index].to_csv("data_{}/train.csv".format(i))
    total.iloc[dev_index].to_csv("data_{}/dev.csv".format(i))