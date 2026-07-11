# Architecture

The Agentic Market Intelligence System is built on a multi-agent orchestration pattern.

## Components

1. **Planner Agent** (`src/agents/planner.py`)
   - Uses structural extraction (`generate_structured`) to take a broad business objective and break it into a typed `ExecutionPlan`.
   - Forces the LLM to output a precise list of tasks adhering to the 5 mandatory phases (Research, Competitors, Trends, Opportunities, Recommendations).

2. **Executor Agent** (`src/agents/executor.py`)
   - Operates on a single `Task` object.
   - Generates targeted queries based on the task description and prior context.
   - Utilizes a `WebSearchTool` to simulate gathering external knowledge.
   - Synthesizes raw findings into a cohesive analysis specific to that task.

3. **Synthesizer Agent** (`src/agents/synthesizer.py`)
   - Aggregates all `TaskResult` outputs.
   - Formats and refines the content into a cohesive, professional Markdown report, ensuring consistency and strong narrative flow.

## Data Models

Located in `src/core/models.py`, Pydantic models define the structure of data moving between agents:
- `Task`: A unit of work.
- `ExecutionPlan`: The overall plan containing a list of Tasks.
- `TaskResult`: The output of an executed Task.

## Tools

Located in `src/tools/web_search.py`, the `WebSearchTool` acts as a simulated data source, querying the LLM to represent external internet knowledge retrieval. In a production setting, this would be replaced with SerpApi or similar web scraping libraries.
