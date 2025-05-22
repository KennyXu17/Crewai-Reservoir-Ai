# optimizer.py
# Select best stragety for highest FOPT

class RLOptimizerTool:
    def run(self, history):
        print("[RLOptimizer] Selecting best strategy based on FOPT...")
        best = max(history, key=lambda x: x.get("FOPT", 0))
        return best