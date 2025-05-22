# sim_runner_agent.py
# This agent invokes the OPM simulator tool with a given strategy

from tools.opm_simulator import OPMSimulationTool

class SimRunnerAgent:
    def __init__(self):
        self.tool = OPMSimulationTool()

    def run(self, strategy):
        print("[SimRunnerAgent] Running simulation...")
        return self.tool.run(strategy)