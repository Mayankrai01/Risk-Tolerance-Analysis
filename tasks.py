from crewai import Task
from tools import financial_data_tool
from agents import read_json_agent, financial_goals_assement_agent, investment_strategy_agent, portfolio_structure_agent,final_compilation_agent
from llm import llm

# Risk Assessment Task
read_json_task = Task(
    description=(
        "Analyze the input file and provide the information on demographics, financials, risk tolerance, and investment preferences."
    ),
    expected_output='The information on demographics, financials, risk tolerance, and investment preferences.',
    tools=[financial_data_tool],
    agent=read_json_agent,
    llm=llm
)

financial_goals_assessment_task = Task(
    description=(
        "Extract the financial goals information from the input file and analyze the financial goals data."
    ),
    expected_output='The information and analysis of the financial goals.',
    # tools=[financial_data_tool],
    agent=financial_goals_assement_agent,
    llm=llm
)

investment_strategy_task = Task(
    description=(
        "Analyze the financial data to assess the client’s risk tolerance and provide an investment strategy based on the provided information."
    ),
    expected_output='The analysis of risk tolerance and a proposed investment strategy.',
    # tools=[financial_data_tool],
    agent=investment_strategy_agent,
    llm=llm
)
portfolio_structure_task = Task(
    description=(
        "Analyze the financial data to design a portfolio structure that matches the client’s risk tolerance and financial goals."
    ),
    expected_output='A detailed portfolio structure based on the client’s financial data.',
    # tools=[financial_data_tool],
    agent=portfolio_structure_agent,
    llm=llm
)

final_compilation_task = Task(
    description=(
        "Gather findings from the read_json_agent, financial_goals_assessment_agent, "
        "investment_strategy_agent, and portfolio_structure_agent. Compile the data, update the user's risk tolerance values "
        "to reflect changes in their financial situation or risk parameters, and write a new JSON file."
    ),
    expected_output="A new JSON file with updated risk tolerance values based on the client's current financial situation and risk preferences.",
    # tools=[financial_data_tool,json_writer_tool],
    agent=final_compilation_agent,
    llm=llm
)
