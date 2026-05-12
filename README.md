# 🌬️ Apache Airflow — Astronomer (Astro) Method

![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![Astronomer](https://img.shields.io/badge/Astronomer-Runtime%203.1--5-00A1E0?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-99.7%25-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![TaskFlow API](https://img.shields.io/badge/TaskFlow%20API-Airflow%20DAGs-green?style=for-the-badge)

---

## 📌 Overview

This project demonstrates how to set up and run **Apache Airflow** locally using the **Astronomer CLI (Astro)** method — the modern, opinionated way to develop and deploy Airflow DAGs. It uses the **Astro Runtime Docker image** (based on Apache Airflow) and spins up a full local Airflow environment with five containerized services using a single command.

The included example DAG (`example_astronauts`) demonstrates a real ETL pipeline using the **TaskFlow API** and **dynamic task mapping** — making it a great starting point for building production-ready DAGs.

---

## ✨ Features

- 🚀 **One-command Local Setup** — `astro dev start` spins up the full Airflow stack instantly
- 🐳 **Astro Runtime Docker Image** — Uses `astrocrpublic.azurecr.io/runtime:3.1-5`, Astronomer's hardened Airflow image
- 🔁 **TaskFlow API DAG** — Demonstrates modern Python decorator-based DAG authoring (`@task`)
- 🗂️ **Dynamic Task Mapping** — Scales tasks dynamically based on runtime data (e.g., one task per astronaut)
- 🌐 **Live API Integration** — `example_astronauts` DAG fetches real-time data from the Open Notify API
- 🧪 **DAG Testing** — Includes a `tests/dags/` directory for validating DAG integrity
- ⚙️ **Docker Compose Override** — `docker-compose.override.yml` for custom port mappings (e.g., Postgres port conflict fix)
- 🔌 **Extendable** — Add OS packages via `packages.txt`, Python packages via `requirements.txt`, and plugins via `plugins/`

---

## 🗂️ Project Structure

```
Apache-airflow-astro-Method/
├── .astro/                         # Astronomer CLI project config
├── dags/                           # Airflow DAG files
│   └── example_astronauts.py       # Example ETL DAG using TaskFlow API
├── tests/
│   └── dags/                       # DAG integrity tests
├── include/                        # Additional files (empty by default)
├── plugins/                        # Custom Airflow plugins (empty by default)
├── Dockerfile                      # Astro Runtime base image (runtime:3.1-5)
├── docker-compose.override.yml     # Port override for local Postgres conflicts
├── packages.txt                    # OS-level packages to install
├── requirements.txt                # Python packages to install
├── airflow_settings.yaml           # Local Airflow Connections, Variables & Pools
└── .gitignore / .dockerignore
```

---

## 🐳 Airflow Services (Docker Containers)

When you run `astro dev start`, five Docker containers spin up automatically:

| Container | Role |
|---|---|
| **Postgres** | Airflow's metadata database (port `5432`) |
| **Scheduler** | Monitors DAGs and triggers tasks on schedule |
| **DAG Processor** | Parses and compiles DAG files |
| **API Server** | Serves the Airflow Web UI and REST API |
| **Triggerer** | Handles deferred (async) tasks |

---

## 🧩 Example DAG — `example_astronauts`

The included DAG demonstrates key Airflow concepts using real-world data:

```
Open Notify API
     │
     ▼
┌──────────────────────────┐
│  @task: get_astronauts() │  ← Fetches current astronauts in space
└──────────┬───────────────┘
           │  Dynamic Task Mapping
           ▼
┌──────────────────────────┐
│  @task: print_astronaut()│  ← One task instance per astronaut (parallel)
│  (mapped for each person)│
└──────────────────────────┘
```

**Key concepts demonstrated:**
- `@task` decorator (TaskFlow API) for clean Python-native task definitions
- `.expand()` for dynamic task mapping — scales automatically with data
- HTTP operator pattern for external API calls
- Minimal boilerplate, maximum readability

---

## ⚙️ Prerequisites

Make sure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (running)
- [Astronomer CLI](https://www.astronomer.io/docs/astro/cli/install-cli) (`astro`)

### Install the Astronomer CLI

```bash
# macOS / Linux (Homebrew)
brew install astro

# Or via curl
curl -sSL install.astronomer.io | sudo bash -s
```

Verify installation:

```bash
astro version
```

---

## 🚀 Quick Start — Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/PremnathAnbu/Apache-airflow-astro-Method.git
cd Apache-airflow-astro-Method
```

### 2. Start the Local Airflow Environment

```bash
astro dev start
```

This command will:
- Pull the Astro Runtime Docker image
- Build and start all 5 containers
- Automatically open the Airflow UI in your browser

### 3. Access the Airflow UI

```
URL:      http://localhost:8080
Username: admin
Password: admin
```

### 4. Access Postgres (optional)

```
Host:     localhost
Port:     5432
Database: postgres
Username: postgres
Password: postgres
```

> **Port conflict?** If port `5432` is already in use, uncomment the override in `docker-compose.override.yml` to remap Postgres to `5433`:
> ```yaml
> services:
>   postgres:
>     ports:
>       - "5433:5432"
> ```

---

## 🛑 Stop the Local Environment

```bash
astro dev stop
```

To also remove containers and volumes:

```bash
astro dev kill
```

---

## 📦 Adding Dependencies

### Python Packages

Add packages to `requirements.txt`:

```
pandas
requests
scikit-learn
```

Then restart the environment:

```bash
astro dev restart
```

### OS-level Packages

Add system packages to `packages.txt`:

```
gcc
libpq-dev
```

### Airflow Connections & Variables (Local Only)

Use `airflow_settings.yaml` to define connections, variables, and pools without touching the UI — useful for local development and reproducibility.

---

## 🧪 Testing Your DAGs

Run DAG integrity tests from the `tests/dags/` directory:

```bash
astro dev pytest tests/dags/
```

This validates that all DAGs can be imported without errors — a critical check before deployment.

---

## ☁️ Deploy to Astronomer Cloud

If you have an Astronomer account, deploying is a single command:

```bash
astro deploy
```

Refer to the [Astronomer deployment docs](https://www.astronomer.io/docs/astro/deploy-code/) for full instructions on setting up a deployment.

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Workflow Orchestration | Apache Airflow |
| Development Platform | Astronomer (Astro CLI) |
| Runtime Image | Astro Runtime 3.1-5 |
| Containerization | Docker + Docker Compose |
| Language | Python 3.8+ |
| DAG Pattern | TaskFlow API + Dynamic Task Mapping |
| Metadata Database | PostgreSQL |

---

## 📚 Useful Commands

| Command | Description |
|---|---|
| `astro dev start` | Start local Airflow environment |
| `astro dev stop` | Stop all containers |
| `astro dev restart` | Restart (picks up new dependencies) |
| `astro dev kill` | Remove all containers and volumes |
| `astro dev logs` | View container logs |
| `astro dev pytest` | Run DAG tests |
| `astro deploy` | Deploy to Astronomer Cloud |

---

## 📖 References

- [Astronomer Getting Started Guide](https://www.astronomer.io/docs/learn/get-started-with-airflow)
- [Astro CLI Documentation](https://www.astronomer.io/docs/astro/cli/overview)
- [Apache Airflow TaskFlow API](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html)
- [Dynamic Task Mapping](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/dynamic-task-mapping.html)
- [Astronomer Deploy Code](https://www.astronomer.io/docs/astro/deploy-code/)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Add your DAG or improvement
4. Commit: `git commit -m 'Add your feature'`
5. Push: `git push origin feature/your-feature`
6. Open a Pull Request

---

## 👤 Author

**Premnath Anbu**
- GitHub: [@PremnathAnbu](https://github.com/PremnathAnbu)

---

> ⭐ If you found this project useful, please give it a star!
