# Risk-Tolerance-Analysis

GET your SECRET KEYS from-
  1) https://platform.openai.com/api-keys
  2) https://console.groq.com/keys
  3) https://aistudio.google.com/app/apikey


Install the dependencies and RUN THE **CREW.PY** to see the workflow

In the **`agents.py`** file set **`verbose=True`** for all agents to see communication between agents in command shell

Agents.py contains the agents used
1. **`read_json_agent`**: Reads JSON files to extract and analyze demographic, financial, risk tolerance, and investment preference data using financial tools and expert knowledge.
2. **`financial_goals_assessment_agent`**: Assesses financial goals from the JSON data and reassesses the user's risk tolerance by analyzing current income, debt, and investment preferences. 

3. **`investment_strategy_agent`**: Analyzes investment strategies from financial data to evaluate how they influence the user's risk tolerance, focusing on income, debt, and goals.

4. **`portfolio_structure_agent`**: Evaluates portfolio structures from financial data and reassesses the user's risk tolerance based on their income, investment, and debt levels.

5. **`final_compilation_agent`**: Compiles and synthesizes the results from other agents to update and write new risk tolerance values into the JSON file based on all findings.


Tasks.py contains the task of respective agents

In the **`demo.txt`** file an example is shown of agents communication during the development phase

A new file would be created during execution of crew.py named as "**`crew_execution.log`**", it will store the logging results 

**`data.json`** contains sample output as per understanding

**For this project I've used "llama-3.1-70b-versatile" model as LLM, Crew AI for communication between agents, google-generativeai for embedding.
For model inferencing I've used Groq API.
Complete project has been made using free open source tools.**
