# Financial Agent

A simple multi-agent financial research project built with Python and the `phi` framework. The project combines a web search agent and a financial research agent to gather market and company information for analysis.

## Features

- Web research using DuckDuckGo
- Financial market data retrieval using Yahoo Finance tools
- Multi-agent coordination for combined research outputs
- Groq-powered AI agents for summarization and analysis

## Project Structure

- `Financial_agent.py` - main agent setup and execution logic
- `requirements.txt` - project dependencies

## Tech Stack

- Python
- `phi`
- `groq`
- `yfinance`
- `duckduckgo-search`

## Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Groq API key in the environment before running the script:

   ```bash
   set GROQ_API_KEY=your_api_key_here
   ```

4. Run the script:

   ```bash
   python Financial_agent.py
   ```

## Example

The script currently researches Tesla (`TSLA`) and summarizes the latest news and stock performance using the connected agents.

## Notes

This project is for educational and research purposes. It is not personalized financial advice.
