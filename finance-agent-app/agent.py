from google.adk.agents import Agent
import requests

from .tools import get_financial_data

# def get_stock_quote(company_name: str):
#     """
#     Retrieves the stock quote for a given company.
#     """
#     mcp_server_url = "https://glama.ai/mcp/instances/svuec7nlpl/mcp"
#     try:
#         response = requests.post(mcp_server_url, json={"company_name": company_name})
#         response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
#         return response.text
#     except requests.exceptions.RequestException as e:
#         return f"Error fetching stock quote for {company_name}: {e}"
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent to help you find financial information about companies.',
    instruction="""
        ***Goals***
        You are a financial assistant. Your goal is to provide accurate financial information to the user.
        
        ***Steps to follow***
        Ask the user which company they want data for        
        - If the user provides a company name, use the `get_financial_data` tool to retrieve its financial information.
        - If the user does not provide a company name, ask them for one.
        Use the available tools to fetch financial data for companies when requested.
        If you cannot find the data, inform the user and ask for another company.
    """,
    tools=[get_financial_data]
)
