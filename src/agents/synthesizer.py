from typing import List
from src.core.models import TaskResult, ExecutionPlan
from src.core.llm_client import LLMClient

class SynthesizerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def synthesize(self, plan: ExecutionPlan, results: List[TaskResult]) -> str:
        print(f"[*] SynthesizerAgent is compiling the final report...")
        
        results_context = ""
        for task in plan.tasks:
            # Find corresponding result
            result = next((r for r in results if r.task_id == task.id), None)
            if result:
                results_context += f"## Task: {task.title}\n"
                results_context += f"Findings:\n{result.findings}\n\n"
        
        prompt = f"""
        You are a Chief Strategy Officer.
        Review the findings from the various market intelligence tasks and synthesize them into a cohesive, highly professional Market Intelligence Report.
        
        Business Objective: "{plan.objective}"
        
        Task Findings:
        {results_context}
        
        The final report MUST be formatted in Markdown and include the following sections:
        - Executive Summary
        - Market Research
        - Competitor Analysis
        - Trend Discovery
        - Opportunity Identification
        - Strategic Recommendations
        
        Ensure smooth transitions between sections and a highly professional tone.
        """
        
        final_report = self.llm.generate_text(prompt, temperature=0.2)
        print(f"[*] SynthesizerAgent completed the report.")
        return final_report
