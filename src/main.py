import os
import argparse
from dotenv import load_dotenv

from src.agents.planner import PlannerAgent
from src.agents.executor import ExecutorAgent
from src.agents.synthesizer import SynthesizerAgent

def main():
    parser = argparse.ArgumentParser(description="Agentic Market Intelligence System")
    parser.add_argument("--objective", type=str, required=True, help="The business objective to execute.")
    parser.add_argument("--output", type=str, default="data/sample_report.md", help="Output file path for the report.")
    args = parser.parse_args()

    # Load environment variables
    load_dotenv()
    if not os.environ.get("GEMINI_API_KEY"):
        print("WARNING: GEMINI_API_KEY environment variable is not set.")
        print("Please set it in a .env file or export it directly.")
        return

    objective = args.objective
    print(f"=== Starting Autonomous Market Intelligence ===")
    print(f"Objective: {objective}\n")

    # Initialize Agents
    planner = PlannerAgent()
    executor = ExecutorAgent()
    synthesizer = SynthesizerAgent()

    # Phase 1: Planning
    print("--- Phase 1: Planning ---")
    plan = planner.plan(objective)
    print("Execution Plan:")
    for i, task in enumerate(plan.tasks, 1):
        print(f"  {i}. {task.title} - {task.description}")
    print("\n")

    # Phase 2: Execution
    print("--- Phase 2: Execution ---")
    results = []
    context = ""
    for task in plan.tasks:
        result = executor.execute(task, context=context)
        results.append(result)
        # Update context with brief summary of finding
        context += f"Task {task.title} Findings: {result.findings[:200]}...\n"
    print("\n")

    # Phase 3: Synthesis
    print("--- Phase 3: Synthesis ---")
    final_report = synthesizer.synthesize(plan, results)
    
    # Save Output
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(final_report)
    
    print(f"\n=== Mission Accomplished ===")
    print(f"Report saved to {args.output}")

if __name__ == "__main__":
    main()
