🚀 DevOps Monitoring Dashboard

Un système complet de monitoring temps réel construit avec FastAPI + Streamlit, containerisé avec Docker et conçu selon des pratiques DevOps modernes (CI/CD, tests, observabilité, sécurité).

📌 Objectif du projet :

Ce projet simule une plateforme de monitoring DevOps permettant :

📊 La surveillance des métriques système (CPU, RAM, disque)
🖥️ Le suivi de serveurs via healthchecks
🔄 Un streaming temps réel via WebSocket
🔐 Une API sécurisée par clé
📈 Un dashboard interactif Streamlit
🐳 Une architecture 100% containerisée

🧱 Architecture
                GitHub
                  │
                  ▼
         GitHub Actions (CI)
     ┌────────────┬────────────┐
     │ lint flake8│ pytest     │
     │ coverage ≥75%            │
     └────────────┴────────────┘
                  │
                  ▼
          Docker Build Images
     ┌─────────────────────────┐
     │ API (FastAPI :8000)     │
     │ Dashboard (Streamlit)   │
     └─────────────────────────┘
                  │
          (local / cloud ready)
          
🧰 Stack technique :
Couche	Technologie
Backend API	FastAPI
Frontend	Streamlit
Monitoring	psutil
HTTP async	httpx
Tests	pytest + pytest-cov
Containerisation	Docker
CI/CD	GitHub Actions
Qualité code	flake8
Sécurité images	Trivy

📦 Installation locale :
1. Cloner le projet
git clone https://github.com/<your-repo>/devops-monitor.git
cd devops-monitor
2. Configuration environnement
cp .env.example .env

Modifier .env :
API_KEY=your_secret_key
API_BASE_URL=http://api:8000

🐳 Lancer le projet (Docker) :
make up
ou :
docker compose up --build -d

🌐 Accès aux services :
Service	URL
API	http://localhost:8000/docs
Metrics API	http://localhost:8000/metrics
Healthcheck	http://localhost:8000/health
Dashboard	http://localhost:8501

🧪 Tests :
Lancer tous les tests
make test
Couverture attendue
≥ 75% coverage obligatoire
Tests API + metrics inclus

🧹 Qualité du code :
Lint
make lint
Utilise flake8 pour garantir un code propre et standardisé.

📊 Fonctionnalités principales :

🔹 API FastAPI
GET /health → état du service
GET /metrics → CPU / RAM / disque
GET /servers → liste des serveurs
POST /servers → ajout serveur (API Key requise)
DELETE /servers/{id} → suppression serveur
POST /servers/{id}/check → healthcheck manuel
WS /ws/metrics → stream temps réel

🔹 Dashboard Streamlit :
📈 KPIs système en temps réel
📊 Graphiques dynamiques
🖥️ Tableau des serveurs coloré (UP / DEGRADED / DOWN)
➕ Formulaire d’ajout de serveur
🔹 Sécurité API

Toutes les routes sensibles utilisent :
X-API-Key: <your_key>

🐳 Docker :
Services
api → FastAPI (port 8000)
dashboard → Streamlit (port 8501)

⚙️ Makefile :
Commande	Action
make up	Lance les containers
make down	Stop et clean
make logs	Logs en live
make test	Tests + coverage
make lint	Analyse code
make dev	Mode local sans Docker

🔁 CI/CD (GitHub Actions) :
Le pipeline CI exécute :
1. Lint
flake8 sur tout le code
2. Tests
pytest + coverage ≥ 75%
3. Build Docker
build API image
build dashboard image
4. Security Scan
Trivy (détection CVE HIGH / CRITICAL)

🧪 Exemple de test API :
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
   
🔐 Sécurité :
Aucun secret dans le repo
Variables via .env
API Key obligatoire pour actions sensibles
Scan des images Docker avec Trivy


📁 Structure du projet :
api/            FastAPI backend
dashboard/     Streamlit UI
tests/         pytest suite
.github/       CI pipeline
docker-compose Production stack
Makefile       automation

🚀 Objectif DevOps :
Ce projet démontre :
Architecture microservices simple
Observabilité (metrics + healthchecks)
CI/CD automatisé
Containerisation complète
Sécurité de base (API key + scan images)

📌 Lancer en 5 minutes :
git clone <repo>
cd devops-monitor
cp .env.example .env
make up

📈 Améliorations possibles :
Redis cache pour métriques
Auth JWT
Kubernetes deployment
Prometheus + Grafana
Logs centralisés (ELK stack)
Projet réalisé dans un cadre pédagogique DevOps :

FastAPI • Docker • CI/CD • Monitoring • Streamlit
