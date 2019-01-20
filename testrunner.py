from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu.model import Interpreter

from colors import yellow, green
from compare_validate import test_tresholds, all_filenames_in_dir, plot_crossmodel_comparative_bars, calculate_plot_data, \
    fill_missing_data_with_zeroes
from tests.cases import cases
from constants import *
from nlu_model import train

def get_model_name_by_cfg(cfg_path):
    return cfg_path.strip(CFG_PREFIX).strip(CFG_FORMAT)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--train", help="train model", action="store_true")
    parser.add_argument("--compare_crossmodel", help="compare intents + ner for different model pipelines", action="store_true")
    parser.add_argument("--compare_crossdataset", help="compare intents + ner for different train sets", action="store_true")
    parser.add_argument("--model", help="train model", action="store")
    args = parser.parse_args()

    interpreters = []

    model_names = []
    ner_names = None
    cross_ner_confidences = []
    intent_names = None
    cross_intent_confidences = []

    comparison_method = None

    if args.compare_crossdataset:
        comparison_method = 'cross-dataset by %s model' % args.model
        for d in all_filenames_in_dir(DATA_DIR):
            if args.model is None:
                print('no model is specified. use --model modelcfg.yml')
                break
            print(yellow('training model with data from path %s' % d))
            train(
                data='./data/%s' % d,
                config_file='./config/%s' % args.model,
                model_dir='./models/%s' % d,
                model_name=d
            )
            model_names.append(d)
            print(yellow("loading model: %s" % d))
            interpreters.append(Interpreter.load('./models/%s/default/%s' % (d, d)))

    if args.compare_crossmodel:
        comparison_method = 'cross-model'
        for p in all_filenames_in_dir(CFG_DIR):
            print(yellow('training model with cfg from path %s' % p))
            name_by_config = get_model_name_by_cfg(p)
            train(
                data='./data/training_data_ru.json',
                config_file='./config/%s' % p,
                model_dir='./models/%s' % name_by_config,
                model_name=name_by_config
            )
            model_name = get_model_name_by_cfg(p)
            model_names.append(get_model_name_by_cfg(p))
            print(yellow("loading model: %s" % model_name))
            interpreters.append(Interpreter.load('./models/%s/default/%s' % (model_name, model_name)))

    for i in interpreters:
        test_tresholds(i, cases)

        ner_names, ner_confidences, intent_names, intent_confidences = calculate_plot_data(i, cases)
        print("intents: %s" % intent_confidences)
        cross_ner_confidences.append(ner_confidences)
        cross_intent_confidences.append(intent_confidences)

    fill_missing_data_with_zeroes(cross_intent_confidences)
    fill_missing_data_with_zeroes(cross_ner_confidences)
    print(yellow("intent names: %s" % intent_names))
    print(yellow("intent confidences: %s" % cross_intent_confidences))
    print(yellow("ner names: %s" % ner_names))
    print(yellow("ner confidences: %s" % cross_ner_confidences))

    print(green('generating plots'))
    print('model_names: %s' % model_names)

    plot_crossmodel_comparative_bars(
        plot_filename='ner',
        ylabel='Entities',
        xlabel='Confidences',
        title='Entities by confidences (%s)' % comparison_method,
        model_names=model_names,
        entities=ner_names,
        confidences=cross_ner_confidences
    )

    plot_crossmodel_comparative_bars(
        plot_filename='intent',
        ylabel='Intents',
        xlabel='Confidences',
        title='Intents by confidences (%s)' % comparison_method,
        model_names=model_names,
        entities=intent_names,
        confidences=cross_intent_confidences
    )
