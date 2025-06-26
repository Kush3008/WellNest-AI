# utils/quote_api.py
import random

quotes_by_mood = {
    "stressed": [
        "Almost everything will work again if you unplug it for a few minutes, including you. — Anne Lamott",
        "Take a deep breath. You're stronger than you think."
    ],
    "anxious": [
        "You don’t have to control your thoughts. You just have to stop letting them control you. — Dan Millman",
        "Feelings are just visitors. Let them come and go."
    ],
    "sad": [
        "Every day may not be good, but there is something good in every day.",
        "This too shall pass."
    ],
    "neutral": [
        "Don’t wait for the right opportunity: create it. — George Bernard Shaw",
        "What you get by achieving your goals is not as important as what you become by achieving your goals."
    ],
    "happy": [
        "Happiness is not something ready made. It comes from your own actions. — Dalai Lama",
        "Keep shining. The world needs your light."
    ]
}

def get_motivational_quote(mood="neutral"):
    return random.choice(quotes_by_mood.get(mood.lower(), quotes_by_mood["neutral"]))
