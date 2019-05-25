# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""
import re
import logging
import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_bad_answer(item):
    """Return response text for incorrect answer."""
    return "{} {}".format(data.BAD_ANSWER.format(item), data.HELP_MESSAGE)


def get_current_score(score, counter):
    """Return the response text for current quiz score of the user."""
    return data.SCORE.format("current", score, counter)


def get_final_score(score, counter):
    """Return the response text for final quiz score of the user."""
    return data.SCORE.format("final", score, counter)


def get_ordinal_indicator(counter):
    """Return st, nd, rd, th ordinal indicators according to counter."""
    if counter == 1:
        return "1st"
    elif counter == 2:
        return "2nd"
    elif counter == 3:
        return "3rd"
    else:
        return "{}th".format(str(counter))


def __get_attr_for_speech(attr):
    """Helper function to convert attribute name."""
    return attr.lower().replace("_", " ").strip()


def get_question_without_ordinal(attr, item):
    return "What is the {} of {}. ".format(
        __get_attr_for_speech(attr), item["state"])


def get_question(counter, question, right, wrong1, wrong2):
    """Return response text for nth question to the user."""
    return (
        "Question {}. {} A: {} B: {} C: {}").format(
        counter,
        question,
        right,
        wrong1,
        wrong2)


def get_answer(attr, item):
    """Return response text for correct answer to the user."""
    if attr.lower() == "abbreviation":
        return ("The {} of {} is "
                "<say-as interpret-as='spell-out'>{}</say-as>. ").format(
            __get_attr_for_speech(attr), item["state"], item["abbreviation"])
    else:
        return "The {} of {} is {}. ".format(
            __get_attr_for_speech(attr), item["state"], item[attr.lower()])


def translate(text):
    """Translate text to given language."""
    # Example of text:
    #     "which of the following animals is the `Mottomo hayai`?"
    # exemple of output:
    #     "which of the following animals is the <voice name=\"Mizuki\"><lang xml:lang=\"ja-JP\">Mottomo hayai</lang></voice> ?"
    logger.info("In translate()")
    return re.sub(r'\`([^\`]+)\`', r'<voice name="Mizuki"><lang xml:lang="ja-JP">\1</lang></voice>', text)


def get_random_question(attr):
    """Get a random question not picked."""
    # Randomize here!
    for i, challange in enumerate(data.CHALLANGES):
        if challange['category'].lower() == attr['category'].lower() and i not in attr['done_questions']:
            return challange, i
    raise RuntimeError('Unable to get question for requested category %s; %s questions are done' % (attr['category'], len(attr['done_questions'])))


def ask_question(handler_input):
    # (HandlerInput) -> None
    """Get a random state and property, return question about it."""
    attr = handler_input.attributes_manager.session_attributes
    # FIXME: find a better way.
    if 'done_questions' not in attr:
        attr['done_questions'] = []
    challange, i = get_random_question(attr)

    attr['done_questions'].append(i)
    question = translate(challange['question'])
    attr["question"] = question
    attr["right"] = translate(challange['answer'])
    attr["counter"] += 1

    handler_input.attributes_manager.session_attributes = attr

    return get_question(attr["counter"], question, attr["right"], translate(challange['w1']), translate(challange['w2']))


def compare_token_or_slots(handler_input, value):
    """Compare value with slots or token,
        for display selected event or voice response for quiz answer."""
    if is_request_type("Display.ElementSelected")(handler_input):
        return handler_input.request_envelope.request.token == value
    else:
        return compare_slots(
            handler_input.request_envelope.request.intent.slots, value)


def compare_slots(slots, value):
    """Compare slot value to the value provided."""
    for _, slot in six.iteritems(slots):
        if slot.value is not None:
            return slot.value.lower() == value.lower()
    else:
        return False



