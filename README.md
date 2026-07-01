🚀 DevOps Monitoring Dashboard

Un système complet de monitoring temps réel construit avec FastAPI + Streamlit, containerisé avec Docker et conçu selon des pratiques DevOps modernes (CI/CD, tests, observabilité, sécurité).

📌 Objectif du projet :
Ce projet simule une plateforme de monitoring DevOps permettant :
📊 Surveillance des métriques système (CPU, RAM, disque)
🖥️ Suivi de serveurs via healthchecks
🔄 Streaming temps réel via WebSocket
🔐 API sécurisée par clé
📈 Dashboard interactif Streamlit
🐳 Architecture 100% containerisée

🧱 Architecture :
                          ┌──────────────────────────┐
                          │        Developer         │
                          │   (push / PR GitHub)     │
                          └────────────┬─────────────┘
                                       │
                                       ▼
                          ┌──────────────────────────┐
                          │         GitHub           │
                          │  Source Code Repository  │
                          └────────────┬─────────────┘
                                       │
                                       ▼
                ┌─────────────────────────────────────────┐
                │          GitHub Actions (CI/CD)         │
                ├─────────────────────────────────────────┤
                │ ✔ Lint (flake8)                        │
                │ ✔ Unit Tests (pytest)                  │
                │ ✔ Coverage ≥ 75%                       │
                │ ✔ Security Scan (Trivy)               │
                └───────────────┬─────────────────────────┘
                                │
                                ▼
                ┌─────────────────────────────────────────┐
                │         Docker Image Build              │
                ├─────────────────────────────────────────┤
                │ 🐳 FastAPI Backend Image               │
                │ 🐳 Streamlit Dashboard Image           │
                └───────────────┬─────────────────────────┘
                                │
                                ▼
                ┌─────────────────────────────────────────┐
                │      Docker Compose Runtime            │
                ├─────────────────────────────────────────┤
                │ API Service (FastAPI :8000)            │
                │ Dashboard (Streamlit :8501)            │
                │ Internal Network Communication         │
                └───────────────┬─────────────────────────┘
                                │
                                ▼
                ┌─────────────────────────────────────────┐
                │     Local / Cloud Deployment Ready     │
                │  (Docker / VM / Kubernetes future)     │
                └─────────────────────────────────────────┘

🧰 Stack technique :
Backend API : FastAPI
Frontend : Streamlit
Monitoring : psutil
HTTP async : httpx
Tests : pytest + pytest-cov
Containerisation : Docker
CI/CD : GitHub Actions
Qualité code : flake8
Sécurité images : Trivy

📦 Installation locale :
git clone https://github.com//devops-monitor.git
cd devops-monitor

cp .env.example .env

API_KEY=your_secret_key
API_BASE_URL=http://api:8000

🐳 Lancer le projet :
make up
ou
docker compose up --build -d

🌐 Accès :
API → http://localhost:8000/docs
Metrics → http://localhost:8000/metrics
Health → http://localhost:8000/health
Dashboard → http://localhost:8501

🧪 Tests :
make test
Coverage ≥ 75%
Tests API + metrics inclus

🧹 Qualité code :
make lint
(flake8)

📊 API FastAPI :
GET /health → état du service
GET /metrics → CPU / RAM / disque
GET /servers → liste serveurs
POST /servers → ajout serveur (API Key)
DELETE /servers/{id} → suppression serveur
POST /servers/{id}/check → healthcheck manuel
WS /ws/metrics → streaming temps réel

📈 Dashboard Streamlit :
KPIs système en temps réel
Graphiques dynamiques
Tableau serveurs (UP / DEGRADED / DOWN)
Formulaire ajout serveur

🔐 Sécurité :
X-API-Key obligatoire pour routes sensibles
Aucun secret dans le repo
Variables via .env
Scan Docker avec Trivy

🐳 Docker :
api → FastAPI (8000)
dashboard → Streamlit (8501)

⚙️ Makefile :
make up → lance containers
make down → stop + clean
make logs → logs live
make test → tests + coverage
make lint → analyse code
make dev → mode local

🔁 CI/CD :
Lint flake8
Tests pytest + coverage ≥ 75%
Build Docker images (API + Dashboard)
Scan sécurité Trivy (CVE HIGH / CRITICAL)

🧪 Exemple test :
def test_health():
    response = client.get("/health")
    assert response.status_code == 200

📁 Structure :
api/ backend FastAPI
dashboard/ UI Streamlit
tests/ pytest
.github/ CI pipeline
docker-compose stack
Makefile automation

🚀 Objectif DevOps :
Architecture microservices
Observabilité (metrics + healthchecks)
CI/CD automatisé
Containerisation complète
Sécurité API key + scan images

📌 Lancer en 5 min :
git clone ...
cd devops-monitor
cp .env.example .env
make up

📈 Améliorations :
Redis cache
JWT auth
Kubernetes
Prometheus + Grafana
ELK stack

FastAPI • Docker • CI/CD • Monitoring • Streamlit
