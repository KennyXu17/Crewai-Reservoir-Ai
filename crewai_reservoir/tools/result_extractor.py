# result_extractor.py
# Tool to extract FOPT and FWPT metrics from OPM SMSPEC or RSM output in scientific notation

import re

def parse_scientific(value_str):
    # Convert strings like 2.5340E+07 or 1.12E7 to float
    try:
        return float(value_str)
    except ValueError:
        # Fallback for scientific format
        match = re.search(r"([0-9]*\.?[0-9]+)[Ee]([+-]?[0-9]+)", value_str)
        if match:
            base, exp = match.groups()
            return float(base) * (10 ** int(exp))
        return None

class ResultExtractorTool:
    def run(self, spec_path):
        fopt = None
        fwpt = None
        pattern_fopt = re.compile("^\s*FOPT\s+([0-9Ee.+-]+)")
        pattern_fwpt = re.compile("^\s*FWPT\s+([0-9Ee.+-]+)")

        with open(spec_path, 'r') as f:
            for line in f:
                if fopt is None:
                    m = pattern_fopt.search(line)
                    if m:
                        fopt = parse_scientific(m.group(1))
                if fwpt is None:
                    m = pattern_fwpt.search(line)
                    if m:
                        fwpt = parse_scientific(m.group(1))
                if fopt is not None and fwpt is not None:
                    break

        return { 'FOPT': fopt, 'FWPT': fwpt }