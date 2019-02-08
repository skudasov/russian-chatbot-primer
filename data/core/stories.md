## single path               <!-- name of the story - just for debugging -->
* order_food               <!-- intent -->
  - action_store_order        <!-- action -->
  - slot{"product_type": "пиццу"}
  - slot{"product_size": "большую"}
  - slot{"product_addons": "ветчиной"}
  - utter_confirm_order