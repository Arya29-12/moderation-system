# 🛡️ AI-Powered Content Moderation System
🔗 **Live Demo:** [https://moderation-system.onrender.com/docs](https://moderation-system.onrender.com/docs)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![ML](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

**An end-to-end ML-driven backend system for detecting, analyzing, and explaining toxic content in real-time.**

---
 ## ⚡Overview
A scalable backend system that detects, classifies, and explains toxic content using Machine Learning and Explainable AI (SHAP).
Built with a production-oriented architecture using FastAPI, MongoDB, and modular ML services.

---

## ✨ Key Features

* 🔍 **Multi-Class Detection:** Classifies text into specific categories (Toxic, Sexual, Insult, etc.) with confidence scores.
* 🧠 **Explainable AI (SHAP):** Breaks down predictions into word-level contributions, identifying exactly which terms triggered the model.
* 📊 **Behavioral Analytics:** Tracks user-specific metrics, including average toxicity scores and sudden spikes in harmful behavior.
* ⚡ **High Performance:** Built with **FastAPI** for asynchronous, non-blocking API operations.
* 🗄️ **Persistent Storage:** Integrated with **MongoDB** for scalable user and content logging.

---
## 🔄 System Workflow: The Lifecycle of a Request

To ensure data integrity and behavioral context, every submission undergoes a multi-stage pipeline:

1. **Deduplication & Ingestion:** Syncs incoming content with existing user profiles to maintain a continuous historical data trail.
2. **Analysis & XAI:** Executes ML classification while simultaneously generating word-level impact scores via **SHAP**.
3. **Stateful Updates:** Persists results to **MongoDB** and instantly recalculates user-specific global toxicity averages.
4. **Spike Detection:** Compares real-time scores against historical norms to trigger `last_spike` flags for abnormal behavior.
5. **Unified Output:** Returns a single JSON containing the prediction, the explanation, and the updated user risk profile.

## 🏗️ Architecture & Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | FastAPI (Python) |
| **Database** | MongoDB (NoSQL) |
| **Machine Learning** | Scikit-learn (TF-IDF Vectorization) |
| **Model Interpretation** | SHAP  |
| **Deployment** | Render / Docker-ready |

---

## 📂 Project Structure

```text
moderation-system/
├── app/
│   ├── db/          # Database connection & configurations
│   ├── models/      # Pydantic schemas & MongoDB models
│   ├── routes/      # API endpoints (Users, Content)
│   ├── services/    # ML Inference & SHAP explanations
│   └── main.py      # FastAPI entry point
├── requirements.txt # Python dependencies
└── README.md
```
## ⚙️ Getting Started

### 1. Prerequisites
* **Python 3.9+**
* **MongoDB Atlas** account or a local MongoDB instance

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/Arya29-12/moderation-system.git

cd moderation-system

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```
### 3. Environment Configuration
Create a .env file in the root directory and add:
```
MONGO_URI=your_mongodb_connection_string
PORT=8000
```
### 4. Run the Server
```
uvicorn app.main:app --reload
```
The interactive API documentation will be available at: http://127.0.0.1:8000/docs

## 📡 API Reference
#### 1. Create / Sync User
`POST /users`
Initializes a new user profile or verifies an existing one to prevent duplication serves as foundation for stateful tracking.

**Request Body:**
```json
{
  "username": "dev_user_01",
  "email": "user@example.com"
}
```
#### 2. Get User Statistics
`GET /users/{user_id}/stats`

Retrieves the processed behavioral profile of a user. This includes cumulative data and identifies if the user's recent activity constitutes a "toxicity spike."

**Example Response:**
```json
{
  "user_id": "64f1a2b3c4d5e6f7g8h9i0",
  "total_posts_analyzed": 142,
  "global_avg_toxicity": 0.12,
  "recent_activity_score": 0.65,
  "spike_detected": true,
  "risk_category": "High Monitoring"
}
```
### 3. Get User Content History
`GET /users/{user_id}/content`

Fetches all historical text submissions mapped to a specific user ID. This allows moderators to review the exact content that contributed to a high toxicity average or a behavioral spike.

**Query Parameters:**

* `limit`: (Optional) Number of recent posts to return.

* `sort`: (Optional) Sort by `timestamp` or `toxicity_score`.

**Example Response:**
```json
[
  {
    "content_id": "99821",
    "text": "User submitted text here...",
    "toxicity_score": 0.88,
    "timestamp": "2023-10-27T10:30:00Z"
  }
]
```
## 🎯 Future Roadmap
* **🤖 Transformer Upgrade**: Transition from TF-IDF to BERT/RoBERTa models for superior semantic understanding and context awareness.

* **⚡ Real-time Buffering**: Integrate Redis to cache frequent analysis results and reduce latency for repetitive content.

* **📊 Admin Dashboard**: Build a React-based UI for moderators to visualize global toxicity trends and user risk scores.

* **🗄️ Auto-Banning Logic**: Implement configurable webhooks to trigger automated account restrictions based on toxicity spikes.

* **🌍 Multilingual Support**: Expand moderation capabilities to support non-English text using multilingual LLMs.

* **🔄 Human-in-the-Loop**: Create a verification workflow where low-confidence AI predictions are flagged for manual review.