import os
from crewai import Agent
from tools import financial_data_tool
from llm import llm

#agent to read json file

read_json_agent = Agent(
    role='Read JSON Input Agent',
    goal='Read the JSON file for information on demographics, financials, risk tolerance, and investment preferences.',
    # verbose=True,
    memory=True,
    backstory=(
        "Expert in extracting information from json input"
    ),
    tools=[financial_data_tool],
    allow_delegation=True,
    llm=llm
)

# agent to assess financial goals

financial_goals_assement_agent = Agent(
    role='Get information on financial goals Agent',
    goal="""Read the JSON file for information on financial goals and provide an updated analysis on how it affects risk tolerance. 
            Use this information to reassess the user's risk tolerance based on: Current income, investments, and debt levels,Investment goals 
            and preferences, Existing tolerance levels and target values.""",
    # verbose=True,
    memory=True,
    backstory=(
            "Expert in extracting information related to financial goals from the data"
    ),
    allow_delegation=True,
    llm=llm
)

# Create a investment strategy agent

investment_strategy_agent = Agent(
    role='Investment strategy Agent',
    goal="""Analyze financial data to assess investment strategy and provide an updated analysis on how it affects risk tolerance.
            Use this information to reassess the user's risk tolerance based on: Current income, investments, and debt levels, Investment goals
            and preferences, Existing tolerance levels and target values.""",
    # verbose=True,
    memory=True,
    backstory=(
        "Expert in extracting information related to investment strategy from the data"
    ),
    allow_delegation=True,
    llm=llm
)


# Create a portfolio structure agent

portfolio_structure_agent = Agent(
    role='Portfolio structure Agent',
    goal="""Analyze financial data to assess portfolio structure and provide an updated analysis on how it affects risk tolerance.'
            Use this information to reassess the user's risk tolerance based on: Current income, investments, and debt levels, Investment goals
            and preferences, Existing tolerance levels and target values.""",
    # verbose=True,
    memory=True,
    backstory=(
        "Expert in extracting information related to portfolio structure from the data"
    ),
    allow_delegation=True,
    llm=llm
)

final_compilation_agent = Agent(
    role='Final Compilation Agent',
    goal='Compile findings from all agents and update the risk tolerance values in a new JSON file.',
    # verbose=True,
    memory=True,
    backstory=(
        "Expert in compiling data from various sources and updating the risk tolerance values based on analysis."
    ),
    allow_delegation=True,
    llm=llm
)
