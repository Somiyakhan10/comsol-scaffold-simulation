# ScaffoldSim — COMSOL Bone Scaffold Stress Simulation
## Computational Prediction of Stem Cell Differentiation · By Somiya Khan

**COMSOL** · **Python** · **MPh** · **NumPy** · **Matplotlib**

> ⚠️ **Note:** This simulation is designed for research and educational purposes only. Not intended for clinical diagnosis.

---

## 📌 Table of Contents
- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Screenshots](#screenshots)
- [Simulation Results](#simulation-results)
- [How It Works](#how-it-works)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Author](#author)

---

## 🔬 Overview

This project simulates mechanical stress distribution in a porous bone scaffold using **COMSOL Multiphysics**. The von Mises stress analysis predicts where stem cells will differentiate into **bone cells (osteogenic)** vs **fat cells (adipogenic)** based on local stiffness variations.

**Key Finding:** The scaffold design shows **70.8% bone formation potential**, with stress concentrations around pore edges promoting osteogenesis.

---

## 🧠 Problem Statement

**The Problem:**  
Bone scaffolds need high porosity for cell growth. However, local stiffness variations misdirect stem cells:
- **Stiff areas** → Become bone cells 
- **Soft areas** → Become fat cells 

**The Question:**  
Where will stem cells become bone vs fat inside a porous scaffold?

**The Solution:**  
Simulate mechanical compression and map von Mises stress distribution.

---

## 📸 Screenshots

### Stress Distribution on Scaffold
<img width="1498" height="761" alt="image" src="https://github.com/user-attachments/assets/7b77b0d8-247c-49f5-a997-4c5cc52b3b2d" />


*Contour plot: Red = high stress (bone formation), Blue = low stress (fat formation)*

### Bone vs Fat Percentage
<img width="752" height="475" alt="image" src="https://github.com/user-attachments/assets/0f4f2bc7-3a77-477d-8410-f9aa8e72a8c3" />


*Bar chart showing predicted bone (90.7%), mixed (8.4%), and fat (0.9%) regions*

---

## 📊 Simulation Results

| Metric | Value |
|--------|-------|
| **Bone Formation** | 70.8% |
| **Mixed Region** | 4.2% |
| **Fat Formation** | 25.0% |
| Maximum Stress | 1,019.91 N/m² |
| Minimum Stress | 57.14 N/m² |
| Average Stress | 345.67 N/m² |

### Biological Interpretation

| Stress Level | Predicted Outcome |
|--------------|-------------------|
| High (Red) | Bone Formation |
| Medium (Yellow/Green) | Mixed Region |
| Low (Blue) | Fat Formation |

---

## ⚙️ How It Works

| Step | Description |
|------|-------------|
| 1 | Create 3D scaffold (1×1×1 mm cube with 4 pores of 0.2 mm) |
| 2 | Assign PLA material (E = 3.5 GPa, ν = 0.36) |
| 3 | Fix bottom face of scaffold |
| 4 | Apply 1 N compressive load on top face |
| 5 | Run stationary study for von Mises stress |
| 6 | Python script automates and extracts results |

---

## 🛠️ Technology Stack

| Tool | Purpose |
|------|---------|
| COMSOL Multiphysics 6.1 | Finite element simulation |
| Python 3.14 | Automation & data analysis |
| MPh library | COMSOL-Python integration |
| NumPy | Numerical processing |
| Matplotlib | Visualization |

---

