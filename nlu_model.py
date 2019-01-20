from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data

from rasa_nlu.config import RasaNLUModelConfig
# from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer, Metadata, Interpreter
from rasa_nlu import config

from colors import yellow
from compare_validate import test_tresholds, get_model_config_paths, plot_comparative_bars, calculate_plot_data, \
    fill_missing_data_with_zeroes, plot_intents
from tests.cases import cases


def train(data=None, config_file=None, model_dir=None, model_name=None):
    training_data = load_data(data)
    configuration = config.load(config_file)
    trainer = Trainer(configuration)
    trainer.train(training_data)
    trainer.persist(model_dir, fixed_model_name=model_name)

CFG_PREFIX = 'config_'
CFG_FORMAT = '.yml'

def get_model_name_by_cfg(cfg_path):
    return cfg_path.strip(CFG_PREFIX).strip(CFG_FORMAT)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="train model", action="store_true")
    parser.add_argument("--compare_ner", help="compare ner pipelines", action="store_true")
    args = parser.parse_args()

    if args.train:
        for p in get_model_config_paths():
            print(yellow('training model with cfg from path %s' % p))
            name_by_config = get_model_name_by_cfg(p)
            train(
                data='./data/training_data_ru.json',
                config_file='./config/%s' % p,
                model_dir='./models/%s' % name_by_config,
                model_name=name_by_config
            )
    if args.compare_ner:
        model_names = []
        ner_names = None
        entity_confidences = []
        intent_names = None
        intent_confidences = None

        for p in get_model_config_paths():
            model_name = get_model_name_by_cfg(p)
            print(yellow("loading model: %s" % model_name))
            interpreter = Interpreter.load('./models/%s/default/%s' % (model_name, model_name))

            test_tresholds(interpreter, cases)

            ner_names, ner_confidences, intent_names, intent_confidences = calculate_plot_data(interpreter, cases)
            print("intents: %s" % intent_confidences)
            model_names.append(model_name)
            entity_confidences.append(ner_confidences)

        print('entity_names: %s' % ner_names)
        for e in entity_confidences:
            print('data collected: %s' % len(e))
        fill_missing_data_with_zeroes(entity_confidences)
        plot_comparative_bars(
            plot_filename='ner',
            ylabel='Entities',
            xlabel='Confidences',
            title='Entities by confidences',
            model_names=model_names,
            entities=ner_names,
            confidences=entity_confidences
        )

        plot_intents(
            plot_filename='intent',
            ylabel='Intents',
            xlabel='Confidences',
            title='Intents by confidences',
            model_names=model_names,
            entities=intent_names,
            confidences=intent_confidences
        )
