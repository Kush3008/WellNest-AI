from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

def build_chain(memory):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")  # ✅ Reads from environment
    )

    prompt = PromptTemplate(
        input_variables=["input"],
        template="""
You are Wellnest 🌱, a supportive emotional wellness companion.

Here is the context of today’s check-in:
{input}

Respond like a caring friend or therapist. Be conversational, warm, and human.
If a quote is included, you may reflect on it — otherwise, do not invent one.
Avoid repeating the weather unless relevant. Vary your tone subtly.
"""
    )

    return LLMChain(llm=llm, prompt=prompt, memory=memory, verbose=True)
