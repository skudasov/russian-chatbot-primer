cases = {
    "хочу пиццу, большую": {
        'id': 1,
        'case': 'знаки препинания',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_type',
                    'value': 'пиццу',
                    'confidence': 0.7,
                },
                {
                    'name': 'product_size',
                    'value': 'большую',
                    'confidence': 0.7,
                }
            ]
        }
    },
    'Хочу заказать б ольшую пиццу': {
        'id': 2,
        'case': 'выделяем сущность с пробелом',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_type',
                    'value': 'пиццу',
                    'confidence': 0.7
                },
                {
                    'name': 'product_size',
                    'value': 'ольшую',
                    'confidence': 0.7
                }
            ]
        }
    },
    'Хочу заказать пиццу с свром': {
        'id': 3,
        'case': 'выделяем сущность с ошибкой',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_type',
                    'value': 'пиццу',
                    'confidence': 0.7
                },
                {
                    'name': 'product_addon',
                    'value': 'свром',
                    'confidence': 0.7
                }
            ]
        }
    },
    'Нужна пицца с глазами тритона и хвостом': {
        'id': 4,
        'case': 'выделяем сущность сильно превосходящую по размеру',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_type',
                    'value': 'пицца',
                    'confidence': 0.7
                },
                {
                    'name': 'product_addon',
                    'value': 'глазами тритона',
                    'confidence': 0.7
                },
            ],
        }
    },
    'доставь пиццу с беконом, среднюю': {
        'id': 5,
        'case': 'меняем порядок слов',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_type',
                    'value': 'пицца',
                    'confidence': 0.7
                },
                {
                    'name': 'product_size',
                    'value': 'среднюю',
                    'confidence': 0.7
                },
                {
                    'name': 'product_addon',
                    'value': 'беконом',
                    'confidence': 0.7
                }
            ],
        }
    },
    'вези 30см пиццу с луком и пармезаном': {
        'id': 6,
        'case': 'числа имеют значение?',
        'intent': 'order_food',
        'entity': {
            'ner_crf': [
                {
                    'name': 'product_addon',
                    'value': 'луком',
                    'confidence': 0.7
                },
                {
                    'name': 'product_addon',
                    'value': 'пармезаном',
                    'confidence': 0.7
                },
                {
                    'name': 'product_type',
                    'value': 'пицца',
                    'confidence': 0.7
                },
                {
                    'name': 'product_size',
                    'value': '30см',
                    'confidence': 0.7
                },
            ]
        }
    },
}
