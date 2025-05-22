# config.py
# Global configuration for CrewAI reservoir simulation project

# OpenAI API key for LLM access
OPENAI_API_KEY = "1234567890"

# Paths for simulation template and result storage
TEMPLATE_PATH = "data/template.DATA"
RESULTS_DIR = "data/results"

# Number of injector wells and default DOE settings
NUM_WELLS = 25
NUM_STRATEGIES = 3
RATE_BOUNDS = (0, 1500)  # oil field injection rate bounds in stb/day
