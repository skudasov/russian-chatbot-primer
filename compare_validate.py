import os
from itertools import cycle
from colors import yellow, green, red


def test_ner_treshold(interpreter, cases):
    for utter, entities in cases.items():
        print(yellow("case: %s" % entities['case']))
        result_entities = interpreter.parse(utter)['entities']
        print(green('result entities: %s' % result_entities))
        for prediction_name, prediction_treshold in entities['entity']['ner_crf'].items():
            print('searching entity: %s with treshold %s' % (prediction_name, prediction_treshold))

            for res_ent in result_entities:
                if res_ent['entity'] == prediction_name and res_ent['confidence'] < prediction_treshold:
                    print(red("FAILED PREDICTION: %s prediction is %s that is below treshold %s"
                              % (prediction_name, res_ent['confidence'], prediction_treshold)))


def calculate_ner(interpreter, cases):
    names = []
    confidences = []
    for utter, entities in cases.items():
        result_entities = interpreter.parse(utter)['entities']
        for prediction_name, prediction_treshold in entities['entity']['ner_crf'].items():
            for res_ent in result_entities:
                if res_ent['entity'] == prediction_name:
                    names.append("%s -> %s" % (res_ent['value'], res_ent['entity']))
                    confidences.append(res_ent['confidence'])
    return names, confidences


def get_model_config_paths(filepath="./config"):
    for _, _, files in os.walk(filepath):
        return files


def plot_comparative_bars(model_names=None, entities=None, confidences=None):
    import numpy as np
    import matplotlib.pyplot as plt

    # data to plot
    n_groups = len(confidences[0])

    # create plot
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.15
    opacity = 0.8

    colors_cycle = cycle(['b', 'g', 'r', 'y'])

    step = 0
    for idx, model_name in enumerate(model_names):
        # step = bar_width if idx > 0 else 0
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
    plt.show()
