import os
from collections import defaultdict
from datetime import datetime
from itertools import cycle
from colors import yellow, green, red


def extract(data):
    return data['intent'], data['intent_ranking'], data['entities']


def test_tresholds(interpreter, cases):
    for utter, rules in cases.items():
        print(yellow("case: %s" % rules['case']))

        result = interpreter.parse(utter)

        intent, _, result_entities = extract(result)
        if not intent:
            print(red("INTENT DETECTION FAILED: expecting %s, found %s" % (rules['intent'], None)))
        elif intent['name'] != rules['intent']:
            print(red("INTENT DETECTION FAILED: expecting %s, found %s" % (rules['intent'], intent['name'])))

        print(green('result intents: %s' % intent))
        print(green('result entities: %s' % result_entities))
        for test_entity_data in rules['entity']['ner_crf']:
            print('searching entity: %s with treshold %s' % (test_entity_data['name'], test_entity_data['confidence']))
            for res_ent in result_entities:
                if res_ent['entity'] == test_entity_data['name']:
                    if res_ent['value'] != test_entity_data['value']:
                        print(red("FAILED PREDICTION: expecting %s -> %s, found %s -> %s"
                                  % (test_entity_data['name'], test_entity_data['value'], res_ent['entity'], res_ent['value'])))
                    elif res_ent['confidence'] < test_entity_data['confidence']:
                        print(red("FAILED PREDICTION: %s prediction is %s that is below treshold %s"
                                  % (test_entity_data['name'], res_ent['confidence'], test_entity_data['confidence'])))


def calculate_plot_data(interpreter, cases):
    intent_good = 0
    intent_total = 0
    ner_good = 0
    ner_total = 0

    ner_names = []
    ner_confidences = []
    intent_names = []
    intent_confidences = []
    for utter, case in cases.items():
        intent_names.append("id: %s -> %s" % (case['id'], case['intent']))
        result = interpreter.parse(utter)
        intent, _, result_entities = extract(result)
        if not intent:
            intent_total += 1
        elif intent['name'] == case['intent']:
            intent_good += 1
            intent_total += 1
            intent_confidences.append(intent['confidence'])
        elif intent['name'] != case['intent']:
            intent_total += 1

        for test_entity_data in case['entity']['ner_crf']:
            for idx, res_ent in enumerate(result_entities):
                if res_ent['entity'] == test_entity_data['name'] and res_ent['value'] == test_entity_data['value']:
                    ner_names.append("id: [%s] %s -> %s" % (case['id'], res_ent['entity'], res_ent['value']))
                    ner_confidences.append(res_ent['confidence'])
                    ner_good += 1
                    ner_total += 1
                    break
            else:
                ner_names.append(
                    "!ERR NOT FOUND! id: [%s] %s -> %s" % (case['id'], test_entity_data['name'], test_entity_data['value']))
                ner_confidences.append(0.0)
                ner_total += 1

    intent_rate = (intent_good / intent_total) if intent_total > 0 else 0
    ner_rate = (ner_good / ner_total) if ner_total > 0 else 0
    return ner_names, ner_confidences, intent_names, intent_confidences, intent_rate, ner_rate


def all_filenames_in_dir(dirpath):
    for _, _, files in os.walk(dirpath):
        return files


def fill_missing_data_with_zeroes(data):
    """
    Fill missing data with zeroes in order to plot graph
    :param data: [[]...]
    :return:  [[]...]
    """
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


def name_plot(name):
    return "tests-%s-%s.png" % (name, datetime.now())


def plot_comparative_bars(
        plot_filename=None,
        ylabel=None,
        xlabel=None,
        title=None,
        model_names=None,
        entities=None,
        confidences=None,
        total_rates=None,
        dpi=100):
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

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.yticks(index + bar_width, entities)
    plt.legend()

    plt.tight_layout()
    plt.savefig(name_plot(plot_filename), dpi=dpi)
