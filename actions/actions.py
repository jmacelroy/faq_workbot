from typing import Any, Text, Dict, List
from urllib import response
from . import db_functions, debug_host
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from pythonping import ping
# import platform    # For getting the operating system name
# import subprocess  # For executing a shell command


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_custom_test"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="retrieving")
        # teasers = db_functions.show_brain_teaser()
        # dispatcher.utter_message(text=str(teasers))

        return []


class ShowBrainTeaser(Action):

    def name(self) -> Text:
        return "action_show_brain_teaser"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        result = db_functions.show_brain_teaser()
        question = result["question"]
        question_id = result["q_id"]
        dispatcher.utter_message(text=question)
        buttons =[]
        for d in result["options"]:
            fill_slot = '{"brain_teaser_answer" : "' + d + '"}'
            buttons.append({"title": d, "payload": f"/intent_brain_teaser_answer {fill_slot}"})
        dispatcher.utter_message(text="", buttons=buttons)

        return [SlotSet("question_id", question_id), SlotSet("brain_teaser_answer")]


class ValidateBrainTeaserAnswer(Action):

    def name(self) -> Text:
        return "action_validate_brain_teaser_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        brain_teaser_answer = tracker.get_slot('brain_teaser_answer')
        question_id = tracker.get_slot('question_id')

        if db_functions.brain_teaser_answer_check(q_id=question_id, answer=brain_teaser_answer):
            dispatcher.utter_message(text="Great Job! Let's move forward.")
        else:
            dispatcher.utter_message(text="Sorry, that was incorrect. Let's move forward.")

        return [SlotSet("brain_teaser_answer", None), SlotSet("question_id", None)]


class ActionDebugHostValidate(Action):

    def name(self) -> Text:
        return "action_debug_host_validate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot_value = tracker.get_slot("debug_host_proceed")
        if slot_value == 'No':
            dispatcher.utter_message(text= f"Operation canceled.")
        else:
            dispatcher.utter_message(text= f"fetching results.. please wait..")
                        # Option for the number of packets as a function of

            host_value = tracker.get_slot("debug_host_name")
            # param = '-n' if platform.system().lower()=='windows' else '-c'
            # command = ['ping', param, '1', host_value]
            # response = subprocess.call(command) == 0
            # debug_response = debug_host.ping(host_value)
            response = ping(host_value, verbose=True)
            dispatcher.utter_message(text= str(response))
        return [SlotSet("debug_host_name", None), SlotSet("debug_host_username", None), SlotSet("debug_host_password", None), SlotSet("debug_host_proceed", None)]