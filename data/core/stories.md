## success story
* order_food{"product_type": "пиццу", "product_addons": "ветчиной", "product_size": "большую"}
  - utter_confirm_order

## no addons
* order_food{"product_type": "пиццу", "product_size": "большую"}
  - utter_ask_addons
* tell_addons{"product_addons": "ветчиной""}
  - utter_confirm_order

## no size
* order_food{"product_type": "пиццу", "product_addons": "ветчиной"}
  - utter_ask_size
* tell_size{"product_size": "большую""}
  - utter_confirm_order

## no type
* order_food{"product_size": "большую", "product_addons": "ветчиной"}
  - utter_ask_type
* tell_type{"product_type": "пиццу""}
  - utter_confirm_order

## broken dialog flow
* inform_actions
  - utter_inform_actions
