cases = {
    "хочу пиццу, большую": {
        'case': 'знаки препинания',
        'intent': 'order_food',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_size': 0.7
            }
        }
    },
    'Хочу заказать б ольшую пиццу': {
        'case': 'выделяем сущность с пробелом',
        'intent': 'order_food',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_size': 0.7
            }
        }
    },
    'Хочу заказать пиццу с свром': {
        'case': 'выделяем сущность с ошибкой',
        'intent': 'order_food',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_topping': 0.7
            }
        }
    },
    'Нужна пицца с глазами тритона и хвостом': {
        'case': 'выделяем сущность сильно превосходящую по размеру',
        'intent': 'order_food',
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
    'доставь пиццу с беконом, среднюю': {
        'case': 'меняем порядок слов',
        'intent': 'order_food',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_topping': 0.7
            }
        }
    },
    'вези 30см пиццу с луком и пармезаном': {
        'case': 'числа имеют значение?',
        'intent': 'order_food',
        'entity': {
            'ner_crf': {
                'product_type': 0.7,
                'pizza_size': 0.7,
                'pizza_topping': {
                    'val': 0.7,
                    'instances': 2
                }
            }
        }
    },
}
