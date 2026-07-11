from src.core.llm_client import LLMClient

class WebSearchTool:
    def __init__(self):
        self.llm = LLMClient()

    def search(self, query: str) -> str:
        """
        Simulates a web search by asking the LLM to provide detailed, 
        realistic search results or knowledge on the query.
        """
        prompt = f"""
        You are a simulated Web Search Engine.
        Provide a comprehensive summary of the information you would find on the web for the following query:
        "{query}"
        
        Format the output as a set of key findings, articles, or data points. Include realistic numbers where appropriate.
        """
        return self.llm.generate_text(prompt, temperature=0.3)
