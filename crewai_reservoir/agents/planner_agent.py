# agents/planner_agent.py
# This agent uses an LLM (or rule-based tool) to generate injection strategies

from tools.doe_generator import DOEGeneratorTool
# If you want to use an LLM instead, you could import and wrap it here.
# e.g. from tools.llm_strategy_generator import LLMStrategyTool

class PlannerAgent:
    def __init__(self, use_llm=False):
        """
        :param use_llm: if True, uses an LLM-based strategy generator;
                        otherwise, falls back to DOEGeneratorTool.
        """
        if use_llm:
            from tools.llm_strategy_generator import LLMStrategyTool
            self.tool = LLMStrategyTool()
        else:
            self.tool = DOEGeneratorTool()

    def run(self):
        """
        Generate and return a list of injection‐rate strategies.
        Each strategy is a dict mapping 'inj1'...'inj25' to a rate (stb/day).
        """
        print("[PlannerAgent] Generating injection strategies...")
        strategies = self.tool.run()
        print(f"[PlannerAgent] Generated {len(strategies)} strategies.")
        return strategies
