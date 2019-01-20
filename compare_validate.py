import os
from datetime import datetime
from itertools import cycle
from colors import yellow, green, red

def extract(data):
    return data['intent'], data['intent_ranking'], data['entities']

def test_tresholds(interpreter, cases):
    for utter, rules in cases.items():
        print(yellow("case: %s" % rules['case']))

        result = interpreter.parse(utter)

        intent, intent_rankings, result_entities = extract(result)
        if intent['name'] != rules['intent']:
            print(red("INTENT DETECTION FAILED: expecting %s, found %s" % (rules['intent'], intent['name'])))

        print(green('result entities: %s' % result_entities))
        for prediction_name, prediction_treshold in rules['entity']['ner_crf'].items():
            print('searching entity: %s with treshold %s' % (prediction_name, prediction_treshold))
            if isinstance(prediction_treshold, dict):
                if [e['entity'] == prediction_name for e in result_entities].count(True) != prediction_treshold['instances']:
                    print(red('ENTITY COUNT IS WRONG: %s, expecting %s'
                          % (prediction_name, prediction_treshold['instances'])))
                # treshold is inside dict, no other information is needed anymore
                prediction_treshold = prediction_treshold['val']

            for res_ent in result_entities:
                if res_ent['entity'] == prediction_name and res_ent['confidence'] < prediction_treshold:
                    print(red("FAILED PREDICTION: %s prediction is %s that is below treshold %s"
                              % (prediction_name, res_ent['confidence'], prediction_treshold)))


def calculate_ner(interpreter, cases):
    names = []
    confidences = []
    for utter, entities in cases.items():
        result = interpreter.parse(utter)
        for prediction_name, prediction_treshold in entities['entity']['ner_crf'].items():
            for res_ent in result['entities']:
                if res_ent['entity'] == prediction_name:
                    names.append("%s\n %s -> %s" % (result['text'], res_ent['value'], res_ent['entity']))
                    confidences.append(res_ent['confidence'])
    return names, confidences


def get_model_config_paths(filepath="./config"):
    for _, _, files in os.walk(filepath):
        return files

def fill_missing_data_with_zeroes(data):
    lens = []
    for e in data:
        lens.append(len(e))
    max_len = max(lens)
    for e in data:
        to_fill = max_len - len(e)
        if to_fill > 0:
            for _ in range(to_fill):
                e.append(0)
    return data

def generate_plot_name():
    return "%s-%s.png" % ("tests(intent, ner)-", datetime.now())

def plot_comparative_bars(model_names=None, entities=None, confidences=None, dpi=100):
    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = len(confidences[0])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.20
    opacity = 0.9

    colors_cycle = cycle(['b', 'g', 'r', 'y'])

    step = 0
    for idx, model_name in enumerate(model_names):
        plt.barh(index + step, confidences[idx], bar_width,
                 alpha=opacity,
                 color=next(colors_cycle),
                 label=model_name)
        step += bar_width

    plt.ylabel('Entities')
    plt.xlabel('Confidences')
    plt.title('Confidences by entities')
    plt.yticks(index + bar_width, entities)
    plt.legend()

    plt.tight_layout()
    plt.savefig(generate_plot_name(), dpi=dpi)
