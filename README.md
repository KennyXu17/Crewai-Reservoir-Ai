# CrewAI + Oil Reservoir Simulation

This project demonstrates how to integrate CrewAI multi-agent orchestration, large language models (LLMs), and OPM reservoir simulation to automate injection strategy design, batch runs, result analysis, optimization, and reporting.

---

## 📂 Repository Structure

```
crewai_reservoir/
├── agents/                # Agent definitions coordinating tasks
│   ├── planner_agent.py   # Generates injection strategies (DOE or LLM)
│   ├── sim_runner_agent.py# Submits strategies to OPM simulator
│   ├── analyzer_agent.py  # Extracts FOPT/FWPT metrics from outputs
│   ├── optimizer_agent.py # Selects best strategy based on history
│   └── reporter_agent.py  # Produces human-readable reports via LLM
├── tools/                 # Low-level utilities and wrappers
│   ├── doe_generator.py   # Sampling-based or rule-based strategy generator
│   ├── opm_simulator.py   # Writes .DATA files and calls `flow` executable
│   ├── result_extractor.py# Parses SMSPEC/RSM files to floats
│   ├── optimizer.py       # History-based strategy selector
│   └── report_writer.py   # LangChain-based LLM reporting tool
├── data/
│   ├── template.DATA      # OPM input template with placeholders
│   └── results/           # Directory to store simulation outputs
├── main.py                # Entry point: defines and runs the workflow
├── config.py              # Global constants and API keys
└── requirements.txt       # Python dependencies and version pins
```

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/QihangX1995/crewai_reservoir.git
   cd crewai_reservoir
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API key** in `config.py`:
   ```python
   OPENAI_API_KEY = "your_openai_api_key_here"
   ```

---

## ⚙️ Usage

1. **Prepare your `.DATA` template** in `data/template.DATA`, using placeholders `<inj1>`, `<inj2>`, … `<inj25>`.
2. **Run the pipeline**:
   ```bash
   python main.py
   ```
   - Generates strategies
   - Runs OPM simulations
   - Extracts FOPT/FWPT
   - Optimizes best strategy
   - Outputs a summary report

3. **Debugging**:
   - Use `debug_reporter.py` to inspect prompts and responses from the LLM tool.

---

## 🛠️ Extensibility

- **Swap DOE with LLM planning**: Set `use_llm=True` in `PlannerAgent` to drive strategy generation via prompts.
- **Advanced optimization**: Implement RL or Bayesian optimization in `tools/optimizer.py`.
- **Custom reporting**: Tweak `report_writer.py` prompts or integrate other LLMs.

---

## 📄 License

MIT License © 2025 KennyXu17
