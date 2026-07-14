# vs-continuous-verification-sandboxing
# CVS: Continuous Verification and Sandboxing Reference Architecture

This repository contains the official prototype implementation, configuration blueprints, and evaluation materials for the CVS reference architecture proposed in the paper:

**"Human in the Loop, Machine in the Pipeline: An Evidence Synthesis of Generative AI Productivity, Verification Overhead, and Repository-Scale Risk in Software Engineering"**
*Author: Md. Nimur Rahman Durjoy*

---

## 📌 Project Overview
This project provides a working implementation of the Continuous Verification and Sandboxing (CVS) pipeline. The architecture introduces an automated evaluation gate between machine-generated AI code (LLM outputs) and human peer review to reduce verification overhead and intercept repository-scale security risks before manual audit.

## 📂 Repository Structure
* **`cvs_scanner.py`**: The core static analysis engine designed to detect common code vulnerabilities (e.g., hardcoded secrets, SQL injection vectors).
* **`Dockerfile`**: Containerized configuration blueprint for creating the Ephemeral Sandbox execution boundary.
* **`.github/workflows/cvs-scan.yml`**: CI/CD integration script executing automated gated filtration on every patch submission.
* **`vulnerable_code.py`**: A simulation script injected with security flaws to test and demonstrate the pipeline's interception rate.

## ⚙️ Core Architecture Workflow
1. **AI Draft Submission**: Candidate patches are treated as unverified.
2. **Static Validation**: Code is parsed for high-risk vulnerabilities via `cvs_scanner.py`.
3. **Dynamic Sandbox Evaluation**: The patch is safely built inside the isolated Docker container.
4. **Evaluation Gate**: Fails the build and blocks the pull request if issues are detected, protecting the developer review queue from cognitive overload.

## 🚀 How to Run Locally

### 1. Prerequisite
Ensure you have **Docker** and **Python 3.10+** installed on your system.

### 2. Standard Local Scan
Run the static analysis engine directly from your terminal:
```bash
python cvs_scanner.py
