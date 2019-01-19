#### nlu-catapod

1) Install requirements
```
sudo pip3 install -r requirements.txt
```
2) Download multilang ner model from spacy
```
python -m spacy download xx_ent_wiki_sm
python -m spacy download en
```

3) LabeL conversation dataset for ner
```
npm i rasa-nlu-trainer
rasa-nlu-trainer -v data/training_data.json
```
4) Train models and compare (see config dir for pipelines)
```
python3 nlu_model.py --train --compare_ner
```

P.S:
if you have trouble with thinkc(spacy dep) on mojave install it first using opt
```
sudo pip3 install thinc==6.10.3 --global-option="-std=libc++"
```