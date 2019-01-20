cases = {
    "хочу пиццу, большую": {
        'id': 1,
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
        'id': 2,
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
        'id': 3,
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
        'id': 4,
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
        'id': 5,
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
        'id': 6,
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
