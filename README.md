<div align="center">

# ⚡ RudraX

**Your terminal has a brain now.**

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-f55036?style=flat-square)](https://groq.com)
[![Whisper](https://img.shields.io/badge/Voice-Whisper%20v3-22c55e?style=flat-square)](https://groq.com)

</div>

---
```
  You: what's the weather in Surat?
  RudraX: Weather in Surat: 34°C, clear sky, wind 12 km/h

  You: solve what is the integral of x^2
  RudraX: Step 1: Apply the power rule...

  You: open vscode
  RudraX: Opening vscode...

  You: [speaks into mic] search python tutorials
  RudraX: Searching Google for: python tutorials
```

---

## ❯ What is RudraX?

RudraX is a CLI-based AI agent that lives in your terminal.
You talk to it — by typing or by voice — and it actually does things.

Not just answers questions. **Does things.**

Opens apps. Fetches weather. Searches Google. Solves problems step by step.
Looks at images and explains them. And when it doesn't know what you want —
it falls back to a full LLM conversation powered by **Llama 3.3 on Groq**.

Built from scratch. No bloat. No GUI. Just you and your terminal.

---

## ❯ What it can do
```
  ┌──────────────────────────────────────────────────────────────┐
  │                                                              │
  │   say  →  "what time is it"       get current time          │
  │   say  →  "what's the date"       get today's date          │
  │   say  →  "weather in Mumbai"     live weather report        │
  │   say  →  "open firefox"          launches the app           │
  │   say  →  "search rust tutorial"  opens Google search        │
  │   say  →  "solve [any problem]"   step-by-step solution      │
  │   say  →  "solve image /path..."  reads and solves an image  │
  │   say  →  anything else           full AI conversation        │
  │                                                              │
  │   + voice mode  →  speak instead of typing                   │
  │                                                              │
  └──────────────────────────────────────────────────────────────┘
```

---

## ❯ Tech Stack

| Layer | What is used | Why |
|---|---|---|
| AI brain | Groq + Llama 3.3 70B | Fast, free, powerful |
| Voice input | Groq Whisper v3 Turbo | Accurate speech-to-text |
| Vision | Llama 4 Scout via Groq | Read and solve images |
| Weather | Open-Meteo API | Completely free, no key needed |
| Terminal UI | Python built-ins | Zero overhead |

100% free to run. No paid APIs. No credit card. Ever.

---

## ❯ Project Structure
```
rudrax/
│
├── main.py                  ← entry point, command router
│
├── modules/
│   ├── ai_chat.py           ← LLM conversation 
│   ├── problem_solver.py    ← step-by-step solver 
│   ├── vision_solver.py     ← image understanding
│   ├── voice_input.py       ← mic → Whisper → text
│   ├── weather.py           ← live weather (Open-Meteo)
│   ├── search.py            ← Google search via browser
│   ├── app_launcher.py      ← opens desktop apps
│   └── datetime_util.py     ← time and date
│
├── .env                     ← your API keys (never commit this)
├── requirements.txt
└── README.md
```
---

## ❯ License

Built by [Akhil](https://github.com/AKHIL-GIT-ARC) 

---

<div align="center">
<sub>Built different. Runs in your terminal.</sub>
</div>
