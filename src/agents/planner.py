from src.core.models import ExecutionPlan
from src.core.llm_client import LLMClient

class PlannerAgent:
    def __init__(self):
        self.llm = LLMClient()

    def plan(self, objective: str) -> ExecutionPlan:
        prompt = f"""
        You are an expert Market Intelligence Planner.
        Your goal is to break down the following business objective into a structured execution plan.
        The plan MUST include the following 5 distinct phases as tasks:
        1. Market Research
        2. Competitor Analysis
        3. Trend Discovery
        4. Opportunity Identification
        5. Strategic Recommendations
        
        Business Objective: "{objective}"
        
        Provide a detailed description for what needs to be researched or analyzed in each task.
        """
        
        print(f"[*] PlannerAgent is breaking down the objective: {objective}")
        plan = self.llm.generate_structured(prompt, ExecutionPlan)
        print(f"[*] PlannerAgent generated {len(plan.tasks)} tasks.")
        return plan
