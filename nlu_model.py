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
from compare_validate import test_ner_treshold, get_model_config_paths, plot_comparative_bars, calculate_ner, \
    fill_missing_data_with_zeroes, test_intents_treshold
from tests.ner_cases import cases


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
        entity_names = None
        entity_confidences = []

        for p in get_model_config_paths():
            model_name = get_model_name_by_cfg(p)
            print(yellow("loading model: %s" % model_name))
            interpreter = Interpreter.load('./models/%s/default/%s' % (model_name, model_name))


            test_intents_treshold(interpreter, cases)
            test_ner_treshold(interpreter, cases)

            entity_names, confidences = calculate_ner(interpreter, cases)
            model_names.append(model_name)
            entity_confidences.append(confidences)

        print('entity_names: %s' % entity_names)
        for e in entity_confidences:
            print('data collected: %s' % len(e))
        fill_missing_data_with_zeroes(entity_confidences)
        plot_comparative_bars(
            model_names=model_names,
            entities=entity_names,
            confidences=entity_confidences
        )
