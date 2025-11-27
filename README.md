# CalmMe
CalmMe is an intelligent emotional-wellbeing agent that analyzes heart-rate signals, detects stress patterns, and generates discreet, personalized interventions.  The current version is a web-based prototype that simulates a wearable experience by ingesting heart-rate readings via an MCP endpoint.

Got it — I’ll rewrite the CalmMe description to match **your real design**:

✔ CalmMe **uses heart-rate data**
✔ It **simulates** a wearable-like experience **through a web/MCP interface**
✔ Later it can be ported into a true wearable / mobile app
✔ So the repo should clearly state: “prototype using web ingestion; future wearable integration”

Here is a corrected, precise description.

---

# ✅ **Corrected Repository Description (Realistic & Accurate)**

# **CalmMe — Emotional Stability Assistant**

### *MCP-Compliant | Letta-Powered Agent | Wearable-Ready Prototype*

**CalmMe** is an intelligent emotional-wellbeing agent that analyzes heart-rate signals, detects stress patterns, and generates discreet, personalized interventions.

The current version is a **web-based prototype** that simulates a wearable experience by ingesting heart-rate readings via an MCP endpoint. In future iterations, CalmMe will integrate directly with **wearables**, **smart rings**, **fitness bands**, or a **mobile app sensor API**.

---

## 🎯 **Why a Web Prototype?**

Wearable apps require:

* sensor APIs
* native SDKs
* Bluetooth HR monitors
* mobile OS permissions
* hardware pairing

These cannot be fully built in a hackathon timeline.

So CalmMe uses:

**➡ MCP Ingestion (`/ingest_hr`)**
to simulate a device sending heart-rate data.

This mimics the exact behavior of a wearable **without needing hardware**.

Future version:
↗ integrate Apple HealthKit, FitBit APIs, Garmin SDK, Oura API, or Bluetooth HR sensors.

---

## 🚀 **Core Capabilities**

### **1️⃣ MCP Server (Wearable Simulator)**

* `/ingest_hr` endpoint receives heart-rate readings
* Simulates “device → agent” flow
* Registers as MCC/MCP-compliant for VersiSense

### **2️⃣ Letta Agent (Mind+Memory)**

* Stores HR history
* Learns daily stress patterns
* Performs LLM reasoning for personalized suggestions
* Generates subtle interventions (via MCP tool)

### **3️⃣ Discreet Alerts**

Via MCP tool:

```
set_discreet_alert(level, message)
```

This could later become:

* vibration pattern on wearable
* silent push notification
* short calming prompt

### **4️⃣ Future: Native Wearable Integration**

The repo includes planned support for:

* Android Wear / WearOS
* Fitbit SDK
* Oura Cloud API
* Generic Bluetooth HR sensors
* iOS HealthKit

---

# 🔧 Architecture (Prototype)

```
[Simulated HR Input (Web/App)]
            ↓
        MCP Server
      (/ingest_hr)
            ↓
      Letta Agent
   (memory + reasoning)
            ↓
 MCP Tool: set_discreet_alert
```

Later → Replace simulated HR input with **real wearable sensor**.

---

# 🧩 Tech Stack

* Python
* Letta SDK (local agent, no cloud key required)
* MCP Server (FastAPI / Express / your choice)
* Simple frontend for entering HR (simulated wearable)
Should I generate the full repo scaffold now?

