def get_coping_strategy(mood: str) -> str:
    mood = mood.lower()

    strategies = {
        "stressed": [
            "Take 5 minutes to breathe deeply and slowly.",
            "Break your tasks into smaller steps.",
            "Write down your thoughts to organize them."
        ],
        "anxious": [
            "Do a grounding exercise: list 5 things you see, hear, or feel.",
            "Limit caffeine and hydrate well.",
            "Try journaling for 5 minutes about what’s worrying you."
        ],
        "overwhelmed": [
            "Pick one task and set a 10-minute timer to work on it.",
            "Declutter your space to declutter your mind.",
            "Step outside or open a window for fresh air."
        ],
        "sad": [
            "Listen to music that comforts you.",
            "Call or message someone you trust.",
            "Remind yourself this feeling is valid, and it will pass."
        ],
        "angry": [
            "Physically release energy — go for a brisk walk or squeeze a stress ball.",
            "Take 10 deep breaths while counting backwards.",
            "Write an unsent letter to express your anger safely."
        ],
        "neutral": [
            "Check in with your breath or take a mindful pause.",
            "Take a short walk or stretch break.",
            "Reflect on something you're grateful for today."
        ],
        "happy": [
            "Celebrate this moment — journal what made you smile.",
            "Share your joy with a friend or loved one.",
            "Channel this energy into something creative or productive."
        ],
        "default": [
            "Take a mindful breath and reflect on what you need right now.",
            "Try a light physical activity like stretching or walking.",
            "Write down one positive intention for the rest of the day."
        ]
    }

    selected = strategies.get(mood, strategies["default"])
    return " • " + "\n • ".join(selected)
