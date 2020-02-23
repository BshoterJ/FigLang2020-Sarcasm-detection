# Sarcasm-detection

Sarcasm detection is the second shared task of [FigLang2020](https://sites.google.com/view/figlang2020/shared-tasks) ,co-located with ACL 2020

For more information about the shared task and to participate visit [CodaLab site](https://competitions.codalab.org/competitions/22247#learn_the_details-overview)

## Dataset

**Training data** can be downloaded in [Github](https://github.com/EducationalTestingService/sarcasm)

- ***label*** : `SARCASM` or `NOT_SARCASM`
- ***response*** :  the sarcastic response, whether a sarcastic Tweet or a Reddit post
- ***context*** : the conversation context of the ***response***
	- Note, the context is an ordered list of dialogue, i.e., if the context contains three elements, `c1`, `c2`, `c3`, in that order, then `c2` is a reply to `c1` and `c3` is a reply to `c2`. Further, if the sarcastic response is `r`, then `r` is a reply to `c3`.
---
For instance, for the following example : 

`"label": "SARCASM", "response": "Did Kelly just call someone else messy? Baaaahaaahahahaha", "context": ["X is looking a First Lady should . #classact, "didn't think it was tailored enough it looked messy"]`

The response tweet, "Did Kelly..." is a reply to its immediate context "didn't think it was tailored..." which is a reply to "X is looking...". Your goal is to predict the label of the "response" while also using the context (i.e, the immediate or the full context).

- **Twitter** : constructed a data set of 5,000 English Tweets balanced between the `SARCASM` and `NOT_SARCASM` classes.
-  **Reddit** : it is a dataset of 4,400 Reddit posts balanced between the `SARCASM` and `NOT_SARCASM` classes.

## Envirement
- python 3.6
- torch 1.0+
- scikit-learn
- tqdm
- pandas
- jsonlines

## Experiments on Twitter

Model| F1-score | input
:-: | :-: | :-: |
bert(cased-large-wwm)+gru | 84.479% |  response
bert(cased-large-wwm)+gru | 84.295% |  context+response 

## RUN
1、Download bert pretain model to `./bert-large-cased-wwm` and rename them as:

`config.json`;`pytorch_model.bin`;`vocab.txt`

2、Prepare the training and dev data(4:1 and 5 fold)

	python ./data/twitter/preprocess_twitter.py 

3、Train the model

	sh run_bert sh
