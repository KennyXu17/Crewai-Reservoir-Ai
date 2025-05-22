# optimizer_agent.py
# Selects the best injection strategy based on FOPT metrics

from tools.optimizer import RLOptimizerTool

class OptimizerAgent:
    def __init__(self):
        self.tool = RLOptimizerTool()

    def run(self, history):
        """
        history: list of dicts containing 'strategy', 'FOPT', and 'FWPT'
        Returns the strategy dict with the highest FOPT.
        """
        if not history:
            raise ValueError("No history data provided to OptimizerAgent")

        print("[OptimizerAgent] Selecting best strategy based on FOPT...")
        # Choose the entry with maximum FOPT
        best_entry = max(history, key=lambda entry: entry.get('FOPT', float('-inf')))
        print(f"[OptimizerAgent] Best FOPT: {best_entry['FOPT']:.2e}")
        return best_entry['strategy']
