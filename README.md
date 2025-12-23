

---

# Flask GitOps: Automated CI/CD Pipeline

This project demonstrates a full **End-to-End DevOps Lifecycle**. It automates the testing, building, and deployment preparation of a Flask web application using GitHub Actions, Docker, and GitOps principles.

## Project Overview

The goal of this project is to ensure that every code change is verified and packaged without manual intervention. The pipeline follows these steps:

1. **Continuous Integration (CI):** Python tests and linting check the code quality.
2. **Containerization:** A Docker image is built and pushed to Docker Hub with a unique version tag.
3. **Continuous Deployment (CD) Trigger:** The pipeline automatically updates the Kubernetes `deployment.yaml` with the new image version, which triggers **ArgoCD** to sync the cluster.

---

## 🛠 Tech Stack

* **Language:** Python (Flask)
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **GitOps:** ArgoCD (ready for K8s deployment)

---

##  Project Structure

```text
├── .github/workflows/
│   └── docker-image.yml            # This is entire CI/CD pipeline
├── k8s/
│   └── deployment.yaml     # Kubernetes manifest (tracked by ArgoCD)
├── app.py                  # Flask Application
├── Dockerfile              # Container instructions
├── requirements.txt        # Python dependencies
└── README.md

```

---

## How the Pipeline Works

### 1. The Build Stage (CI)

On every push to the `main` branch, GitHub Actions:

* Logs into **Docker Hub** using encrypted secrets.
* Builds a new image tagged with the GitHub Run Number (e.g., `v10`).
* Pushes the image to the registry.

### 3. The Manifest Update (GitOps Trigger)

* Uses `sed` to find and replace the old image tag in `k8s/deployment.yaml`.
* Commits and pushes the change back to the repository with a `[skip ci]` tag to prevent infinite loops.

---

##  Setup Instructions

### Prerequisites

* A Docker Hub account.
* GitHub Repository Secrets:
* `DOCKERHUB_USERNAME`   #docker hub account user name
* `DOCKERHUB_TOKEN`    # docker hub auth token 


* GitHub Repository Variables:
* `GIT_Acc`  # this you personal gthub account 
* `GIT_Mail`  # this you personal github mail id



### Installation

1. Clone the repository.
2. Ensure **Workflow Permissions** in GitHub Settings are set to **Read and Write**.
3. Make a change to `app.py` and push!

---

##  Automated Messages

You will see commits labeled as `chore: update image tag to vXX`. This indicates the automation has successfully signaled the deployment controller (ArgoCD) that a new version is ready for the cluster.

---
