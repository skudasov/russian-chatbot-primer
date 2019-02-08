# -*- coding: utf-8 -*-
import logging
from datetime import datetime
from typing import Text, Dict, Any, List
import json

from rasa_core_sdk import Action, Tracker
from rasa_core_sdk.executor import CollectingDispatcher
from rasa_core_sdk.forms import FormAction
from rasa_core_sdk.events import SlotSet, UserUtteranceReverted, \
    ConversationPaused, FollowupAction, Form


logger = logging.getLogger(__name__)


class ActionOrderPizza(Action):

    def name(self):
        return "action_call_pizza"

    def run(self, dispatcher, tracker, domain):
        product_size = tracker.get_slot('product_size')
        product_type = tracker.get_slot('product_type')
        product_addons = tracker.get_slot('product_addon')
        print('TRIGGERED ACTION')
        return []

class ActionStoreOrder(Action):

    def name(self):
        return "action_store_order"

    def run(self, dispatcher, tracker, domain):
        ptype = next(tracker.get_latest_entity_values('product_type'), None)
        psize = next(tracker.get_latest_entity_values('product_size'), None)
        paddons = next(tracker.get_latest_entity_values('product_addons'), None)
        print('extracted: %s | %s | %s' % (ptype, psize, paddons))

        return [SlotSet('product_type', ptype)]