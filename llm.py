from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
load_dotenv()


llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv("groq_api_key")
)