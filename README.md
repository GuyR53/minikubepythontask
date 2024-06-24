# minikube-python-task

## Overview

The purpose of this project is to deploy and test microservices using a CI/CD pipeline on a Kubernetes cluster managed by Minikube. Key objectives and components include:

- **CI/CD Pipeline**: Automate the build, testing, and deployment processes for microservices using GitHub Actions.
  
- **Microservices Deployment**: Deploy microservices (e.g., app-1 and app-2) using Helm charts onto a Kubernetes cluster provisioned by Minikube.
  
- **Testing**: Implement automated tests within the CI/CD pipeline to verify the functionality of deployed microservices. Tests include HTTP requests (curl commands) to endpoints (/odd, /even, /) exposed by the microservices.
  
- **Infrastructure Configuration**: Configure Minikube to enable necessary add-ons (like Ingress) and manage DNS resolution (/etc/hosts entries) for routing requests (app-1.odd.application.com, app-1.even.application.com, and app-2.application.com) to the correct microservices.

## Prerequisites

### Development Environment:

Ensure you have a development machine with sufficient resources to run Minikube and Docker.

### GitHub Secrets:

Set up GitHub secrets for storing sensitive information such as Docker Hub credentials (`DOCKER_USERNAME` and `DOCKER_PASSWORD`).

### Helm Configuration - DockerHub Account:

Adjust the `image.name` and `image.repository` values in the `app-1.yaml` and `app-2.yaml` files to match your DockerHub account.

## Setup Instructions

1. Fork the Repository.
2. Make the necessary changes mentioned above.
3. Run the GitHub Actions workflow.

## Deployment Workflow

### Workflow Overview

This project utilizes a CI/CD pipeline with GitHub Actions to automate the deployment and testing of microservices on a local Kubernetes cluster managed by Minikube. The pipeline includes the following key steps:

1. **Build Docker Image**: Build Docker images for each microservice (app-1 and app-2) with version tagging based on the GitHub Actions run number.

2. **Push to Docker Hub**: Push Docker images to Docker Hub repositories using encrypted credentials from GitHub Secrets.

3. **Deploy with Helm**: Deploy microservices using Helm charts (`app-1.yaml`, `app-2.yaml`) to Minikube. Configure resources, services, and ingress rules as specified.

4. **Test Microservices**: Perform automated tests within the pipeline using curl commands to validate endpoint responses (`/odd`, `/even`) of deployed microservices.

5. **Ingress Configuration**: Enable and configure Minikube's Ingress addon to route external requests based on DNS entries (/etc/hosts) to the appropriate microservices.
