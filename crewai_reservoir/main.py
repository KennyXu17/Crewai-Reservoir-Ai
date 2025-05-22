from agents.planner_agent import PlannerAgent
from agents.sim_runner_agent import SimRunnerAgent
from agents.analyzer_agent import AnalyzerAgent
from agents.optimizer_agent import OptimizerAgent
from agents.reporter_agent import ReporterAgent

def run_pipeline():
    strategies = PlannerAgent().run()
    history = []

    for strategy in strategies:
        result = SimRunnerAgent().run(strategy)
        if not result['success']:
            continue

        metrics = AnalyzerAgent().run(result['output_path'])
        history.append({"strategy": strategy, **metrics})

    best = OptimizerAgent().run(history)
    report = ReporterAgent().run(best)
    print("\n=== REPORT ===\n")
    print(report)
