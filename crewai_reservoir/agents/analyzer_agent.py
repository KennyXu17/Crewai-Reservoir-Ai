# analyzer_agent.py
# Extracts FOPT and FWPT from simulation output using ResultExtractorTool

import os
from tools.result_extractor import ResultExtractorTool

class AnalyzerAgent:
    def __init__(self):
        self.tool = ResultExtractorTool()

    def run(self, result_dir):
        """
        Locate the SMSPEC (or RSM) file in the result directory
        and extract FOPT/FWPT metrics.
        """
        # Find the first .SMSPEC (or .RSM) file
        spec_file = next(
            (f for f in os.listdir(result_dir) if f.lower().endswith(('.smspec', '.rsm'))),
            None
        )
        if spec_file is None:
            raise FileNotFoundError(f"No SMSPEC/RSM file found in {result_dir}")
        spec_path = os.path.join(result_dir, spec_file)

        print(f"[AnalyzerAgent] Extracting metrics from {spec_path}...")
        metrics = self.tool.run(spec_path)
        print(f"[AnalyzerAgent] Extracted metrics: {metrics}")
        return metrics