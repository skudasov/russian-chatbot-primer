cases = {
    "хочу пиццу, большую": {
        'case': 'знаки препинания',
        'entity': {
            'ner_crf': {
                'product_type': 0.90,
                'pizza_size': 0.90
            }
        }
    },
    'Хочу заказать б ольшую пиццу': {
        'case': 'выделяем сущность с пробелом',
        'entity': {
            'ner_crf': {
                'product_type': 0.90,
                'pizza_size': 0.90
            }
        }
    },
    'Хочу заказать пиццу с свром': {
        'case': 'выделяем сущность с ошибкой',
        'entity': {
            'ner_crf': {
                'product_type': 0.90,
                'pizza_topping': 0.90
            }
        }
    },
}
