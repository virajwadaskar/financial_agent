
"""Simple financial research agent."""
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo



## web search agent 
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information and provide relevant results.",
    model=Groq(id="meta-llama/llama-prompt-guard-2-22m"),
    tools=[DuckDuckGo()],
    instructions=[
        "Use the DuckDuckGo tool to search for information on the web.",
        "Provide relevant results based on the user's query.",
    ],
    show_tool_calls=True,
    markdown=True,

)

##financial research agent
financial_research_agent = Agent(
name = "Financial Research Agent"
role = "Research stocks and financial news using available tools."
model = Groq(id="meta-llama/llama-prompt-guard-2-22m"),
tools = [
    YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        company_news=True, 
    )
    
    DuckDuckGo()],
instructions = [
    "Use the available tools to verify current market data and news.",
    "Cite sources and distinguish facts from analysis.",
    "Do not provide personalized financial advice.",
	show_tool_calls=True,
	markdown=True,
],

),
multiagent = Agent(
    name="Multi-Agent System",
    role="Coordinate between the Web Search Agent and Financial Research Agent to provide comprehensive financial research.",
    model=Groq(id="meta-llama/llama-prompt-guard-2-22m"),
    tools=[web_search_agent, financial_research_agent],
    instructions=[
        "Use the Web Search Agent to gather information from the web.",
        "Use the Financial Research Agent to analyze stocks and financial news.",
        "Combine insights from both agents to provide a comprehensive response.",
    ],
    show_tool_calls=True,
    markdown=True,
)
multiagent.print_response("Research the latest news and stock performance for Tesla (TSLA) and provide a summary of findings.",stream=True)
