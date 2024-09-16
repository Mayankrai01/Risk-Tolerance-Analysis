import google.generativeai as genai
from crewai_tools import JSONSearchTool
import openai
import os
from llm import llm
from json_writer import JSONWriterTool
openai.api_key = os.getenv("OPENAI_API_KEY")

genai.configure(api_key=os.getenv("google_ai_api_key"))

financial_data_tool = JSONSearchTool(json_path='userForm.json',    
    config={
        "embedder": {
            "provider": "google",
            "config": {
                "model": "models/embedding-001", 
                "task_type": "retrieval_document"  
            },
        }
})

