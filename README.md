# k8s-misconfig-mvp
MVP for detecting Kubernetes security misconfigurations.



cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload



docker run -d \
  --name k8s-mvp-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=k8s_mvp \
  -p 5432:5432 postgres:18


```
GET /	Health check
GET /k8s/namespaces	List namespaces
GET /k8s/deployments	List deployments
GET /k8s/pods	List pods

Step 1: Scan pods into DB
POST /pods/scan/{cluster_id}

Step 2: Run detection
POST /detect/pods/{cluster_id}

```

```
Kubernetes
 ↓
Collection
 ↓
Normalization
 ↓
Storage
 ↓
Detection
 ↓
Scoring
 ↓
Presentation

```