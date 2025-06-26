from memory.memory_config import get_memory
from chains.wellnest_chain import build_chain
from utils.weather_api import get_weather
from utils.quote_api import get_quote
from tools.mood_analyzer import analyze_mood
from tools.coping_strategy import get_strategy

def main():
    memory = get_memory()
    chain = build_chain(memory)

    print("Welcome to Wellnest 💚 — your mental health buddy.")
    print("Type how you're feeling today. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            farewell_quote = get_quote("neutral")
            print(f"\nWellnest 🧠: I'm always here if you need me. Here's something to take with you:\n\"{farewell_quote}\"\nTake care! 🌿")
            break

        mood = analyze_mood(user_input)
        strategy = get_strategy(mood)
        weather = get_weather()
        
        # Only sometimes fetch quote — e.g., 1 in 3 messages
        import random
        quote = get_quote(mood) if random.random() < 0.33 else None

        # Combine input for single-key input compatibility
        input_block = f"""
User said: {user_input}
Detected mood: {mood}
Suggested strategy: {strategy}
Weather: {weather}"""

        if quote:
            input_block += f"\nMotivational quote: {quote}"

        # Run the chain with only one key: "input"
        response = chain.run({"input": input_block})
        print(f"\nWellnest 🧠: {response}\n")

if __name__ == "__main__":
    main()
