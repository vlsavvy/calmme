# CalmMe – An Emotional Wellbeing Agent (MCP + Letta)

CalmMe is an intelligent emotional-wellbeing agent that detects stress signals, responds to heart-rate anomalies, and delivers discreet grounding interventions.

This prototype does **not require wearables** — instead it uses a lightweight web simulator that streams synthetic heart-rate data to the agent.

Later, the sensing layer can be swapped for:

* a wrist wearable app
* Verisense SDK sensors
* any MCP-compliant data emitter

---

## ✨ Features

* 🧠 **Local Letta Agent**

  * Runs entirely on-device using open-source Letta framework.
  * Supports reasoning, memory, and reactive workflows.

* 🔌 **MCP-Compliant Interface**

  * CalmMe exposes its capabilities as MCP Tools.
  * Compatible with Verisense / Any MCP host.

* ❤️ **Stress Signal Simulator**

  * No smartwatch or wearable needed.
  * Web UI generates synthetic HR spikes, variability drops, and stress indicators.

* 🕊️ **Interventions**

  * Breathing prompts
  * Cognitive reframing
  * Safety / grounding routines
  * Affirmations based on user’s stress profile

---

## ⚙️ Architecture

```
[Web Simulator] → HR events → [FastAPI Backend] → [MCP Adapter]  
                                                 → [Letta Agent] → Interventions
```

---

## 🏁 Running Locally

### 1. Clone the repo

```
git clone https://github.com/<your-username>/CalmMe.git
cd CalmMe
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the Letta Agent

```
python calmme_agent/agent.py
```

### 5. Start Simulator API

```
uvicorn simulator.api:app --reload --port 8001
```

### 6. Open the Web UI (optional)

If using a simple HTML/JS UI:

```
open simulator/web_ui/index.html
```

---

## 🔑 Do I Need A Letta API Key?

**No.**
This project uses *local Letta runtime* (open-source) — no cloud API key needed.

Only if you choose to use:

* Lepta Cloud hosted agents
* Cloud LLM credits
  then you’d need signup + wallet.

For this hackathon prototype:
**Local Letta = fully free + no wallet + no signup.**

---

## 🧩 MCP Tools Exposed

CalmMe exposes:

### 1. `stress_event`

Send HR/HRV data to the agent.

### 2. `get_state`

Return current stress evaluation.

### 3. `intervene`

Trigger a grounding or breathing routine.

### 4. `conversation`

Chat with CalmMe for emotional guidance.

These appear automatically when the host (e.g., Verisense) loads the MCP manifest.

---

## 📦 Deploying to Verisense (Hackathon)

1. Push this repo
2. Build small Docker image:

```
docker build -t calmme-agent .
```

3. Deploy via Verisense dashboard (they load MCP tools automatically)
4. Verisense hosts the runtime, CalmMe behaves like a plug-in

---

# 📝 Roadmap

* Real wearable integration (BLE / Android Wear)
* Micro-stress inference model
* Personalized intervention library
* Continuous memory graph for emotional patterns

---

# License

MIT License
