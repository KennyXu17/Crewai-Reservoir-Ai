# report_writer.py
# LLM-based report generation tool using LangChain

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from config import OPENAI_API_KEY

class LLMReportTool:
    def __init__(self, model_name="gpt-4", temperature=0.0):
        # Read API key from config.py
        self.llm = ChatOpenAI(model=model_name, temperature=temperature, openai_api_key=OPENAI_API_KEY)

    def run(self, result_summary):
        prompt = f"""
You are a petroleum engineer. Analyze the following simulation results and write a professional summary:

- FOPT: {result_summary['FOPT']:.2e}
- FWPT: {result_summary['FWPT']:.2e}
- Injection Strategy: {result_summary['strategy']}

Provide insights on well contributions and suggest improvements.
"""
        response = self.llm([HumanMessage(content=prompt)])
        return response.content
