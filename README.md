# ✈️ Glide Simulator – Constant Angle Optimization

## 📌 Overview

This project simulates aircraft glide motion using a simplified aerodynamic model and finds the **optimal constant angle of attack (α)** for maximum glide range.

---

## 🎯 Goal

* Simulate glide trajectory using lift and drag forces
* Optimize angle of attack for maximum horizontal range
* Compare simulation results with theoretical lift-to-drag ratio

---

## 🧠 Model

* Lift: ( C_L = C_{Lα} (α - α_0) )
* Drag: ( C_D = C_{D0} + K C_L^2 )
* Motion solved using numerical integration (Euler method)

---

## 📊 Features

* Glide simulation with constant α
* Optimization using `scipy.optimize.minimize_scalar`
* Range vs α analysis
* Physics-based performance comparison

---

## 🛠️ Tech Stack

Python · NumPy · SciPy · Matplotlib

---

## ▶️ Run

```bash id="r1"
python main.py
```

---

## 📌 Result

Outputs optimal α and maximum glide range with performance plot.
