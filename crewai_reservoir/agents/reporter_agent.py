# reporter_agent.py
# Generates human-readable report using an LLM (LLMReportTool)

from tools.report_writer import LLMReportTool

class ReporterAgent:
    def __init__(self):
        # Initialize the LLM report generator tool
        self.tool = LLMReportTool()

    def run(self, best_result):
        """
        best_result: dict containing 'strategy' and metrics (e.g., FOPT, FWPT)
        Returns a generated report string.
        """
        print("[ReporterAgent] Generating report...")
        report = self.tool.run(best_result)
        print("[ReporterAgent] Report generated")
        return report
