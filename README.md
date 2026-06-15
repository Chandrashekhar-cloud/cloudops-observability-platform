# CloudOps Observability Platform

A containerized observability platform built using Prometheus, Grafana, Loki, Promtail, Alertmanager, and Node Exporter to monitor and analyze a Flask application.

---

## Project Overview

This project demonstrates a complete monitoring and logging stack for a containerized application.

The platform collects application and system metrics, visualizes them through Grafana dashboards, centralizes logs using Loki, and manages alerts using Prometheus Alertmanager.

---

## Architecture

```text
                +------------------+
                |    Flask App     |
                +--------+---------+
                         |
                         |
          +--------------+--------------+
          |                             |
          v                             v

+------------------+          +------------------+
|   Prometheus     |          |    Promtail      |
| Metrics Scraping |          |  Log Collection  |
+--------+---------+          +--------+---------+
         |                             |
         v                             v

+------------------+          +------------------+
|   Alertmanager   |          |      Loki        |
| Alert Handling   |          | Centralized Logs |
+------------------+          +--------+---------+
                                       |
                                       v

                             +------------------+
                             |     Grafana      |
                             | Dashboards & Logs|
                             +------------------+

                     +------------------+
                     |  Node Exporter   |
                     | System Metrics   |
                     +------------------+
```

---

## Features

### Monitoring

- Application metrics collection using Prometheus
- Infrastructure monitoring using Node Exporter
- Target health monitoring
- Custom alert rules

### Logging

- Centralized log aggregation using Loki
- Log collection through Promtail
- Log exploration inside Grafana

### Visualization

- Grafana dashboards for:
  - Flask application status
  - Node Exporter status
  - CPU usage monitoring

### Alerting

- Prometheus alert rules
- Alertmanager integration
- Application availability monitoring

---

## Technology Stack

| Component | Purpose |
|------------|----------|
| Flask | Sample Application |
| Docker Compose | Container Orchestration |
| Prometheus | Metrics Collection |
| Grafana | Visualization |
| Loki | Log Aggregation |
| Promtail | Log Collection |
| Alertmanager | Alert Management |
| Node Exporter | System Metrics |

---

## Services

| Service | Port |
|----------|------|
| Flask App | 5000 |
| Prometheus | 9090 |
| Grafana | 3000 |
| Alertmanager | 9093 |
| Loki | 3100 |
| Node Exporter | 9100 |

---

## Screenshots

### Docker Containers

![Docker Containers](docs/docker-containers.png)

### Prometheus Targets

![Prometheus Targets](docs/prometheus-targets.png)

### Prometheus Rules

![Prometheus Rules](docs/prometheus-rules.png)

### Grafana Dashboard

![Grafana Dashboard](docs/grafana-dashboard-final.png)

### Alertmanager

![Alertmanager](docs/alertmanager-ui.png)

---

## Running the Project

Clone the repository:

```bash
git clone https://github.com/Chandrashekhar-cloud/cloudops-observability-platform.git
cd cloudops-observability-platform
```

Start all services:

```bash
docker compose up -d
```

Verify running containers:

```bash
docker ps
```

Stop all services:

```bash
docker compose down
```

---

## Implemented Monitoring

### Flask Application Monitoring

Prometheus scrapes metrics exposed by the Flask application and tracks application availability.

### Infrastructure Monitoring

Node Exporter provides CPU and system-level metrics that are visualized through Grafana dashboards.

### Log Monitoring

Promtail collects log files and forwards them to Loki for centralized storage and querying.

### Alerting

Prometheus evaluates alert rules and forwards triggered alerts to Alertmanager.

---

## Repository Structure

```text
cloudops-observability-platform/
│
├── app/
├── prometheus/
│   ├── prometheus.yml
│   └── alert_rules.yml
│
├── alertmanager/
│   └── alertmanager.yml
│
├── loki/
│   └── loki-config.yml
│
├── promtail/
│   └── promtail-config.yml
│
├── docs/
│   ├── docker-containers.png
│   ├── prometheus-targets.png
│   ├── prometheus-rules.png
│   ├── grafana-dashboard.png
│   └── alertmanager-ui.png
│
└── docker-compose.yml
```

---

## Learning Outcomes

Through this project, I gained hands-on experience with:

- Containerized monitoring stacks
- Metrics collection and visualization
- Log aggregation and analysis
- Alert configuration and management
- Docker Compose orchestration
- Observability fundamentals

---

## Author

**Chandrashekhar H S**

Aspiring DevOps / SRE Engineer
