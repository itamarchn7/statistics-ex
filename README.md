# statistics-ex

# Python Flask App – DevOps Technical Assignment

## Overview
This repository contains a simple Python Flask web application that is containerized with Docker and deployed to Kubernetes.

The goal is to build a small Python web application, containerize it, and deploy it to Kubernetes.
---

## Step 1 - Application
The application is a lightweight Flask service with the following endpoints:

| Endpoint     | Description |
|--------------|------------|
| `/my-app`    | Main endpoint – returns "Hello, World!" |
| `/about`     | Application description |
| `/ready`     | Readiness probe |
| `/live`      | Liveness probe |
| `/metrics`   | Prometheus metrics |

The app listens on port `8080`.

## Step 2 - Containerization

### Build image & run
```bash
docker build -t my-python-app:1.0.0 .
docker run -p 8081:8080 my-python-app:1.0.0
```

### Verify app in browser
http://127.0.0.1:8081/my-app


## Step 3 - Kubernetes Deployment
See all kubernetes files under k8s folder

### Create statis-app namespace:
```bash
kubectl apply -f .\k8s\namespace.yaml
```

### Deploy to cluster:
```bash
kubectl apply -f .\k8s\deployment.yaml
kubectl apply -f .\k8s\service.yaml
```

## Step 4 - Exposure

### kubectl port-forward
```bash
kubectl port-forward svc/my-python-app 8081:80 -n statis-app
```
verify in browser with: http://127.0.0.1:8081/my-app 

### NodePort
```bash
kubectl get svc -n statis-app
```
verify in browser with: http://127.0.0.1:30525/my-app  (NODE_PORT=30525)

### Ingress (with nginx)
```bash
kubectl apply -f .\k8s\ingress.yaml
```
verify in browser with: http://my-app.local/my-app

## Optional Enhancements

### Basic observability
* I added liveness & readiness probes.
  The liveness probe checks whether the application is still responsive, with /live endpoint.
  If this probe fails repeatedly, Kubernetes automatically restarts the container. 
  The readiness probe determines whether the application is ready to receive traffic, with /ready endpoint.
  If it fails, the pod is temporarily removed from the Service load balancing without restarting it.
* A /metrics endpoint exposes numerical application metrics in a format that monitoring systems (Prometheus) can scrape.

### Configuration management 


### Automation


### Security hardening
See Dockerfile:
* container as non-root:    USER appuser
* minimal base image:       python:3.12-slim

### Packaging tooling

