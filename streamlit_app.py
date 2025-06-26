import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from chains.wellnest_chain import build_chain
from tools.mood_analyzer import analyze_mood
from tools.coping_strategy import get_coping_strategy
from utils.weather_api import get_weather
from utils.quote_api import get_motivational_quote
from memory.memory_config import get_memory
from dotenv import load_dotenv

load_dotenv()
memory = get_memory()
chain = build_chain(memory)

st.set_page_config(page_title="Wellnest AI Companion", page_icon="💚")
st.title("Wellnest 💚 — Your Emotional Wellness Companion")

st.markdown("Please describe how you're feeling today 👇")

# ✅ New dynamic user input fields
location = st.text_input("Where are you located?", placeholder="e.g., Delhi")
user_input = st.text_area("Your check-in:", placeholder="Hey, I woke up late and have so much work to do...")

if st.button("Analyze"):
    if not user_input.strip():
        st.warning("Please enter something to reflect on.")
    else:
        with st.spinner("Analyzing your emotions..."):

            mood = analyze_mood(user_input)
            strategy = get_coping_strategy(mood)

            # ✅ Dynamic weather and quote
            weather = get_weather(location or "Delhi")
            quote = get_motivational_quote(mood)

            input_block = f"""
User said: {user_input}
Detected mood: {mood}
Suggested strategy: {strategy}
Weather: {weather}
Motivational quote: {quote}
"""

            response = chain.run({"input": input_block})

        st.subheader("🌤️ Analysis Summary")
        st.markdown(f"**Primary Mood:** {mood}")
        st.markdown(f"**Strategy:** {strategy}")
        st.markdown(f"**Weather Info:** {weather}")
        st.markdown(f"**Quote:** {quote}")

        st.divider()

        st.subheader("💬 Wellnest's Response")
        st.markdown(response)
