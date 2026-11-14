# Complete Observability System

An end-to-end DevOps observability project that monitors a containerized Flask application using metrics, logs, and distributed tracing.

## Tech Stack

- Docker and Docker Compose
- Python and Flask
- Prometheus – metrics collection
- Grafana – dashboards and visualization
- Loki – log aggregation
- Grafana Alloy – log collection
- Jaeger – distributed tracing

## Architecture

The Flask application runs in a Docker container.

- Prometheus collects application metrics from `/metrics`.
- Grafana visualizes metrics through dashboards.
- Alloy collects Docker container logs and forwards them to Loki.
- Jaeger receives and displays distributed traces.

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Application welcome message |
| `/health` | Health check |
| `/hello` | Hello response |
| `/slow` | Simulates a slow request |
| `/metrics` | Prometheus metrics |

## Access Services

| Service | URL |
|---|---|
| Flask Application | http://localhost:5001 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Jaeger | http://localhost:16686 |
| Loki | http://localhost:3100 |

## Docker Compose

Docker Compose manages the Flask application and connects it to the existing monitoring network.

The monitoring services are currently running as separate Docker containers.

## Key Learnings

- Containerizing a Python Flask application.
- Collecting application metrics using Prometheus.
- Creating monitoring dashboards in Grafana.
- Collecting container logs using Alloy and Loki.
- Implementing distributed tracing with OpenTelemetry and Jaeger.
- Connecting services through a Docker network.
- Managing an application using Docker Compose.

## Project Status

Metrics, dashboards, logs, and distributed tracing have been integrated and tested.
