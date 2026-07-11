from src.core.models import Task, TaskResult
from src.core.llm_client import LLMClient
from src.tools.web_search import WebSearchTool

class ExecutorAgent:
    def __init__(self):
        self.llm = LLMClient()
        self.search_tool = WebSearchTool()

    def execute(self, task: Task, context: str = "") -> TaskResult:
        print(f"[*] ExecutorAgent starting task: {task.title}")
        
        # Step 1: Formulate search queries based on the task description
        query_prompt = f"""
        Based on this task description, formulate a specific search query to gather the necessary market intelligence.
        Task: {task.title}
        Description: {task.description}
        Context from previous tasks: {context}
        
        Return ONLY the search query string.
        """
        search_query = self.llm.generate_text(query_prompt, temperature=0.1).strip()
        print(f"    - Search Query: {search_query}")
        
        # Step 2: Execute search
        search_results = self.search_tool.search(search_query)
        print(f"    - Search complete. Analyzing results...")
        
        # Step 3: Analyze and synthesize findings for this specific task
        analysis_prompt = f"""
        You are an expert Market Intelligence Analyst.
        Analyze the following search results to fulfill the task requirements.
        
        Task: {task.title}
        Task Description: {task.description}
        
        Search Results:
        {search_results}
        
        Provide a detailed, professional synthesis of the findings relevant to this task.
        Use markdown formatting.
        """
        findings = self.llm.generate_text(analysis_prompt, temperature=0.3)
        
        print(f"[*] ExecutorAgent completed task: {task.title}")
        return TaskResult(
            task_id=task.id,
            findings=findings,
            sources_used=[search_query]
        )
