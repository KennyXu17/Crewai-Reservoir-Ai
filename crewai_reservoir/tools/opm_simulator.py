# opm_simulator.py
# Run OPM simulation by writing strategy into a .DATA file and calling flow

import os
import shutil
import uuid
import subprocess

class OPMSimulationTool:
    def __init__(self, template_path="data/template.DATA", result_dir="data/results"):
        self.template_path = template_path
        self.result_dir = result_dir
        os.makedirs(result_dir, exist_ok=True)

    def run(self, strategy_dict):
        case_id = str(uuid.uuid4())[:8]
        case_path = os.path.join(self.result_dir, f"case_{case_id}.DATA")

        # 1. Write strategy into .DATA file 
        with open(self.template_path, "r") as f:
            template = f.read()

        for well, rate in strategy_dict.items():
            template = template.replace(f"<{well}>", str(rate))

        with open(case_path, "w") as f:
            f.write(template)

        # 2. Run OPM simulator
        try:
            cmd = f"flow {case_path}"
            print(f"[OPMSimulation] Running: {cmd}")
            subprocess.run(cmd, shell=True, check=True)
            output_path = os.path.join(self.result_dir, f"case_{case_id}.SMSPEC")
            return {"success": True, "output_path": output_path}
        except subprocess.CalledProcessError:
            return {"success": False, "output_path": None}