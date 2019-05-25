# -*- coding: utf-8 -*-

CHALLANGES = [
    {
        'category': 'Animals',
        'answer': '`inu`',
        'question': 'Which option is dog?',
        'w1': '`neko`',
        'w2': '`buta`'
    },
    {
        'category': 'Animals',
        'answer': '`inu`',
        'question': 'which animal pees on the lamppost when we walk him?',
        'w2': '`Tori`',
        'w1': '`Shika`',
    },
    {
        'category': 'Animals',
        'answer': 'uma',
        'question': 'which of the following animals is the `Mottomo hayai`?',
        'w2': 'kame',
        'w1': 'ari',
    },
    {
        'category': 'Animals',
        'answer': '`Monkī`',
        'question': 'what animal eats `bananas` and `Ki ni noboru`?',
        'w2': '`Buta`',
        'w1': '`Ushi`',
    },
    {
        'category': 'Animals',
        'answer': 'lion',
        'question': 'what animal has a `Juzō` in egypt?',
        'w2': 'monkey',
        'w1': 'giraffe',
    },
    {
        'category': 'Animals',
        'answer': '`Ushi`',
        'question': '`Chīzu` is produced from which animal?',
        'w2': '`Neko`',
        'w1': '`Raion`',
    },
    {
        'category': 'Animals',
        'answer': '`Zō`',
        'question': 'What is the `Mottomo ōkī` animal?',
        'w2': '`Yagi`',
        'w1': '`Mausu`',
    },
    {
        'category': 'Fruits',
        'answer': 'watermelon',
        'question': 'which `Furūtsu` has the most `Tane`?',
        'w2': 'cherry',
        'w1': 'banana',
    },
    {
        'category': 'Fruits',
        'answer': 'strawberry',
        'question': 'The inside of this fruit is `ah ka`',
        'w2': 'mango',
        'w1': 'apple',
    },
    {
        'category': 'Fruits',
        'answer': '`Momo`',
        'question': 'Which fruit is used as a bum emoji?',
        'w2': '`Cherī`',
        'w1': '`Painappuru`',
    },
    {
        'category': 'Fruits',
        'answer': '`banana`',
        'question': 'which fruit is very long and slender?',
        'w2': '`Painappuru`',
        'w1': '`Ringo`',
    },
    {
        'category': 'Fruits',
        'answer': '`banana`',
        'question': 'which fruit is very long and slender?',
        'w2': '`Painappuru`',
        'w1': '`Ringo`',
    },
    {
        'category': 'Colours',
        'answer': '`ah ka`',
        'question': 'Newton discovered `Jūryoku` when an apple fell on his head. What colour was the `Ringo`?',
        'w2': '`Murasakino`',
        'w1': '`Shiro`',
    },
    {
        'category': 'Colours',
        'answer': 'red',
        'question': 'what colour is the planet `Kasei`?',
        'w2': 'green',
        'w1': 'purple',
    },
    {
        'category': 'Colours',
        'answer': 'blue',
        'question': "What colour is donald duck's `Bōshi`?",
        'w2': 'red',
        'w1': 'yellow',
    },
    {
        'category': 'Colours',
        'answer': 'blue',
        'question': 'If Alice is travelling 30km per hour south at noon, and Bob is travelling 15km per hour north, `Sora no iro wa nanidesu ka?`',
        'w2': 'yellow',
        'w1': 'green',
    },
    {
        'category': 'Colours',
        'answer': '`ah ka`',
        'question': "What's Donald Trump's `Sukinairo`?",
        'w2': '`Midori`',
        'w1': '`Orenji`',
    }
]

SKILL_TITLE = "My Language Tutor"

WELCOME_MESSAGE = ("Sure, what would you liked to be quizzed on? Select from the following: Animals, Fruits, or Colours")

START_QUIZ_MESSAGE = ("I'll give you five questions.")

EXIT_SKILL_MESSAGE = ("Thank you for playing! Quiz you later! Let's play again soon!")

REPROMPT_SPEECH = "Which other state or capital would you like to know about?"

HELP_MESSAGE = ("Would you like to exit the game? "
                "Would you like to change the category?")

MAX_QUESTIONS = 5

BAD_ANSWER = (
    "I'm sorry. {} is not something I know very much about in this skill.")

FALLBACK_ANSWER = (
    "Sorry. I can't help you with that. {}".format(HELP_MESSAGE))

SCORE = "Your {} score is {} out of {}. "

SPEECH_DESC = (
    "{} is the {}th state, "
    "admitted to the Union in {}.  "
    "The capital of {} is {}, and the "
    "abbreviation for {} is "
    "<break strength='strong'/><say-as interpret-as='spell-out'>"
    "{}</say-as>.  I've added {} to "
    "your Alexa app.  Which other state or capital would you like to "
    "know about? ")


