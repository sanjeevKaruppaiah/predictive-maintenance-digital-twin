# 🔧 Predictive Maintenance Digital Twin

> Digital twin simulation for industrial predictive maintenance — models equipment degradation and flags failure risk before breakdown occurs.

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)]()
[![Simulation](https://img.shields.io/badge/Digital%20Twin-Simulation-0F6E56?style=flat-square)]()
[![ML](https://img.shields.io/badge/Machine%20Learning-Predictive-22314E?style=flat-square)]()

---

## 📌 Project Overview

Unplanned equipment failure costs industrial operations billions annually. This project builds a **digital twin** — a live virtual replica of physical machinery — that continuously monitors asset health and predicts failure windows before they happen.

Instead of fixed maintenance schedules, the system enables **condition-based maintenance**: intervene exactly when needed, not too early (wasted cost) or too late (catastrophic failure).

---

## 🏗️ System Design

```
Physical Asset
  (Sensors: vibration, temp, pressure, RPM)
         │
         ▼
┌─────────────────────┐
│   Digital Twin      │  Mirror of asset state updated in real time
│   State Model       │
└────────┬────────────┘
         │
┌────────▼────────────┐
│  Degradation Model  │  RUL (Remaining Useful Life) estimation
│  ML Regression      │
└────────┬────────────┘
         │
┌────────▼────────────┐
│  Alert Engine       │  Threshold breach → maintenance ticket
└─────────────────────┘
```

---

## ✨ Key Features

- **Digital twin state model:** continuously updated asset representation
- **RUL prediction:** Remaining Useful Life regression from sensor time-series
- **Multi-sensor fusion:** vibration, temperature, pressure, RPM signals combined
- **Anomaly alerting:** configurable thresholds trigger pre-emptive maintenance flags
- **Simulation environment:** stress-test the model under synthetic failure scenarios

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.10+ |
| ML Models | Scikit-learn, XGBoost |
| Time-series | Pandas, NumPy |
| Simulation | Custom physics-based degradation model |
| Visualization | Matplotlib, Plotly |
| Data | NASA CMAPSS Turbofan Engine dataset |

---

## 🚀 Getting Started

```bash
git clone https://github.com/sanjeevKaruppaiah/predictive-maintenance-digital-twin.git
cd predictive-maintenance-digital-twin
pip install -r requirements.txt
python main.py
```

---

## 📊 Results

| Metric | Value |
|---|---|
| RUL Prediction RMSE | 18.4 cycles |
| Failure detection lead time | 47 cycles average |
| False alarm rate | < 5% |

---

## 🔭 Roadmap

- [ ] Stream live sensor data via MQTT broker
- [ ] Add LSTM model for sequential RUL prediction
- [ ] Build interactive dashboard with Plotly Dash
- [ ] Package as REST microservice for industrial integration

---

## 👤 Author

**Sanjeev Karuppaiah** — Robotics & Systems Engineer  
[LinkedIn](https://www.linkedin.com/in/sanjeevkaruppaiah) · [GitHub](https://github.com/sanjeevKaruppaiah)
