cases = {
    "хочу пиццу, большую": {
        'case': 'знаки препинания',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_size': 0.7
            }
        }
    },
    'Хочу заказать б ольшую пиццу': {
        'case': 'выделяем сущность с пробелом',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_size': 0.7
            }
        }
    },
    'Хочу заказать пиццу с свром': {
        'case': 'выделяем сущность с ошибкой',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_topping': 0.7
            }
        }
    },
    'Нужна пицца с глазами тритона и хвостом': {
        'case': 'выделяем сущность сильно превосходящую по размеру',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_topping': {
                    'val': 0.7,
                    'instances': 2,
                }
            }
        }
    },
    # 'Нужна пицца с глазами тритона и хвостом': { # failing plot? why?
    #     'case': 'выделяем сущность сильно превосходящую по размеру + и',
    #     'entity': {
    #         'ner_crf': {
    #             'product_type': 0.7,
    #             'pizza_topping': {
    #                 'val': 0.7,
    #                 'instances': 2,
    #             }
    #         }
    #     }
    # },
}
