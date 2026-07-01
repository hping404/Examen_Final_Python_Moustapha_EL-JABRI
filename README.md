# 🚀 DevOps Monitoring Dashboard

Un système complet de monitoring temps réel construit avec **FastAPI** et **Streamlit**, containerisé avec **Docker** et conçu selon des pratiques DevOps modernes (CI/CD, tests, observabilité, sécurité).

---

## 📌 Objectifs du Projet

Cette plateforme de monitoring DevOps simule et permet :
*   📊 **Surveillance des métriques système** (CPU, RAM, disque).
*   🖥️ **Suivi de serveurs** via des healthchecks réguliers.
*   🔄 **Streaming temps réel** des données via WebSockets.
*   🔐 **API sécurisée** par clé API (`X-API-Key`).
*   📈 **Dashboard interactif** avec Streamlit.
*   🐳 **Architecture 100% containerisée**.

---

## 🧱 Architecture du Système

```mermaid
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/4dcbe960-c972-456f-b61e-5176fa35a438" />
```

---

## 🧰 Stack Technique

*   **Backend API** : FastAPI
*   **Frontend UI** : Streamlit
*   **Monitoring Système** : `psutil`
*   **Client HTTP Asynchrone** : `httpx`
*   **Tests & Qualité** : Pytest, Pytest-Cov, Flake8
*   **Containerisation** : Docker & Docker Compose
*   **CI/CD Pipeline** : GitHub Actions
*   **Sécurité** : Scan d'images Trivy

---

## 📦 Installation & Démarrage Rapide (5 min)

### 1. Cloner le dépôt
```bash
git clone https://github.com/<username>/devops-monitor.git
cd devops-monitor
```

### 2. Configurer les variables d'environnement
Copiez le fichier d'exemple et configurez vos clés :
```bash
cp .env.example .env
```

Dans le fichier `.env` :
```env
API_KEY=your_secret_key
API_BASE_URL=http://api:8000
```

### 3. Lancer l'application avec Docker
```bash
make up
# ou
docker compose up --build -d
```

---

## 🌐 Accès aux Services

Une fois l'application démarrée, vous pouvez y accéder via les adresses suivantes :

| Service | URL | Description |
| :--- | :--- | :--- |
| **API Documentation** | 🌐 [http://localhost:8000/docs](http://localhost:8000/docs) | Swagger interactif de l'API |
| **System Metrics** | 📊 [http://localhost:8000/metrics](http://localhost:8000/metrics) | Données brutes (CPU, RAM, Disque) |
| **Health Status** | 🧪 [http://localhost:8000/health](http://localhost:8000/health) | État de santé de l'API |
| **Dashboard UI** | 📈 [http://localhost:8501](http://localhost:8501) | Interface utilisateur Streamlit |

---

## 📊 Endpoints de l'API FastAPI

| Méthode | Route | Description | Clé API requise |
| :--- | :--- | :--- | :---: |
| `GET` | `/health` | État de santé général du service | ❌ |
| `GET` | `/metrics` | Métriques actuelles (CPU, RAM, Disque) | ❌ |
| `GET` | `/servers` | Liste des serveurs sous surveillance | ❌ |
| `POST` | `/servers` | Ajouter un nouveau serveur à surveiller | ✔ |
| `DELETE`| `/servers/{id}` | Supprimer un serveur de la liste | ✔ |
| `POST` | `/servers/{id}/check` | Déclencher manuellement un healthcheck | ✔ |
| `WS` | `/ws/metrics` | Flux WebSocket temps réel des métriques | ❌ |

---

## 📈 Fonctionnalités du Dashboard Streamlit

*   **KPIs Temps Réel** : Visualisation instantanée de l'utilisation du processeur, de la mémoire RAM et du disque.
*   **Graphiques Dynamiques** : Courbes d'évolution temporelle des ressources système.
*   **Suivi des Serveurs** : Tableau récapitulatif avec statut coloré (`UP`, `DEGRADED`, `DOWN`).
*   **Gestion des Serveurs** : Formulaire d'ajout de nouveaux serveurs directement depuis l'interface utilisateur.

---

## 🧪 Tests & Qualité de code

### Exécuter les tests unitaires et de couverture
Le projet impose une couverture de tests minimale de **75%**.
```bash
make test
```
*Inclus les tests de l'API, des healthchecks et des calculs de métriques.*

#### Exemple de test API (`pytest`) :
```python
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
```

### Analyse statique de code (Linting)
```bash
make lint
```
*Utilise `flake8` pour garantir le respect des standards PEP 8.*

---

## ⚙️ Automatisation (Makefile)

Le projet intègre un `Makefile` pour simplifier les tâches courantes :

*   `make up` : Lance les conteneurs Docker en arrière-plan.
*   `make down` : Arrête les conteneurs et nettoie les volumes/réseaux.
*   `make logs` : Affiche les logs en temps réel.
*   `make test` : Exécute la suite de tests avec calcul de couverture.
*   `make lint` : Lance l'analyse de qualité de code avec `flake8`.
*   `make dev` : Démarre le backend et le frontend en mode développement local (sans Docker).

---

## 🔁 Pipeline CI/CD (GitHub Actions)

À chaque validation de code (`push` ou `Pull Request`) :
1.  **Validation syntaxique** : Linting avec `flake8`.
2.  **Tests unitaires** : Exécution de `pytest` (validation si couverture >= 75%).
3.  **Build des images** : Construction des images Docker pour l'API et le Dashboard.
4.  **Scan de sécurité** : Analyse des vulnérabilités des images Docker avec Trivy (`HIGH` / `CRITICAL`).

---

## 🔐 Sécurité

*   **Authentification** : En-tête `X-API-Key` requis pour les opérations de modification de serveurs.
*   **Gestion des secrets** : Aucun mot de passe ou clé en dur dans le dépôt. Tout passe par le fichier `.env` (exclu de Git).
*   **Sécurisation des conteneurs** : Scan Trivy intégré au pipeline pour bloquer les images contenant des vulnérabilités critiques.

---

## 📁 Structure du Projet

```text
devops-monitor/
├── .github/             # Configuration des workflows GitHub Actions
├── api/                 # Code source du backend FastAPI
├── dashboard/           # Code source de l'interface Streamlit
├── tests/               # Tests unitaires et d'intégration (pytest)
├── .env.example         # Modèle des variables d'environnement
├── docker-compose.yml   # Définition des services Docker
├── Makefile             # Raccourcis de commandes pour le développement
└── README.md            # Ce fichier
```

---

## 📈 Améliorations Futures (Roadmap)

*   [ ] Intégration de **Redis** pour la mise en cache des métriques.
*   [ ] Authentification utilisateur via **JWT (JSON Web Tokens)**.
*   [ ] Déploiement sur un cluster **Kubernetes** (fichiers manifests / Helm Charts).
*   [ ] Exportation des métriques vers **Prometheus** et visualisation dans **Grafana**.
*   [ ] Centralisation des logs avec une stack **ELK** (Elasticsearch, Logstash, Kibana).
