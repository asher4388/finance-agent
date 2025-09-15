from google.adk.agents import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='An agent to help you find financial information about companies.',
    instruction='Answer user questions to the best of your knowledge',
)
