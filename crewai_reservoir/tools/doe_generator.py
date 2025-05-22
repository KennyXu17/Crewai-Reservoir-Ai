# doe_generator.py
# Generates injection strategies using rule-based or sampling-based methods

import random

class DOEGeneratorTool:
    def __init__(self, num_wells=25, num_strategies=3, rate_bounds=(0, 1500)):
        self.num_wells = num_wells
        self.num_strategies = num_strategies
        self.rate_bounds = rate_bounds

    def run(self):
        strategies = []
        for i in range(self.num_strategies):
            strategy = {
                f"inj{j+1}": random.randint(self.rate_bounds[0], self.rate_bounds[1])
                for j in range(self.num_wells)
            }
            strategies.append(strategy)
        print(f"[DOEGenerator] Generated {len(strategies)} strategies.")
        return strategies
