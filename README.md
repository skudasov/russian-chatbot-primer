#### nlu-catapod

1) Install requirements

    ```
    sudo pip3 install -r requirements.txt
    ```

2) Download multilang ner model from spacy
    ```
    python3 -m spacy download xx_ent_wiki_sm
    python3 -m spacy download en
    ```

3) Retrain, run, act
    ```
    make train-nlu && make train-core && make run-server
    curl -XPOST localhost:5005/conversations/default/respond -d '{"query":"хочу большую пиццу с ветчиной"}'
    ```
4) Train model manually
    ```
    python3 -m rasa_nlu.train --data data/training_data_new.md -c config/config_spacy_multilang.yml --fixed_model_name new_data
    ```
    then evaluate confusion matrix
    ```
    python3 -m rasa_nlu.evaluate --data data/training_data_new.md -m models/nlu/default/new_data --mode evaluation
    ```

5) Train models and compare between models or datasets (see config dir for pipelines)
    ```
    python3 testrunner.py --compare_crossmodel
    python3 testrunner.py --compare_crossdataset --model config_spacy_multilang.yml
    ```
5) Confusion matrix, intent prediction distribution
    ```
    python3 -m rasa_nlu.evaluate --data data/training_data_ru.json -m models/spacy_multilang/default/spacy_multilang --mode evaluation 
    python3 -m rasa_nlu.evaluate --data data/training_data_ru.json -c config/config_spacy_multilang.yml --mode crossvalidation 
    ```

P.S:
if you have trouble with thinkc(spacy dep) on mojave install it first using opt
```
sudo pip3 install thinc==6.10.3 --global-option="-std=libc++"
```