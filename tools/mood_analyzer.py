def analyze_mood(user_input):
    text = user_input.lower()
    if any(word in text for word in ["sad", "down", "tired", "depressed", "anxious"]):
        return "low"
    elif any(word in text for word in ["happy", "excited", "joyful", "grateful"]):
        return "high"
    else:
        return "neutral"
