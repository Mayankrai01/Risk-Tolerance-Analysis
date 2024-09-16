import google.generativeai as genai
from crewai import Crew,Process
from agents import read_json_agent, financial_goals_assement_agent, investment_strategy_agent, portfolio_structure_agent, final_compilation_agent
from llm import llm
from tasks import read_json_task, financial_goals_assessment_task, investment_strategy_task, portfolio_structure_task, final_compilation_task
from json_extractor import extract_json
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
genai.configure(api_key=os.getenv("google_ai_api_key"))

# Forming the risk assessment crew
crew = Crew(
    # agents=[read_json_agent],
    agents=[read_json_agent, financial_goals_assement_agent, investment_strategy_agent, portfolio_structure_agent,final_compilation_agent],
    manager_llm=llm,
    planning_llm=llm,
    # tasks=[read_json_task],
    tasks=[read_json_task,financial_goals_assessment_task,investment_strategy_task,portfolio_structure_task,final_compilation_task],
    process=Process.sequential,
    verbose=False,
    memory=True,
    embedder={
        "provider": "google",
        "config": {
            "model": 'models/embedding-001',
            "task_type": "retrieval_document",
            "title": "Embeddings for Embedchain"
        }
    },
    cache=True,
    max_rpm=100,
    share_crew=True,
    output_log_file='crew_execution.log'
)

# Start the task execution process
result = crew.kickoff()

final_data=extract_json(result.raw)

with open("data.json", "w") as file:
    file.write(str(final_data))
