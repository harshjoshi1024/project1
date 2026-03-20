# Containerized Web Application

This project satisfies the grading requirements for a multi-container Docker application utilizing FastAPI, PostgreSQL, multi-stage Dockerfiles, and IPvlan networking.

## Prerequisites
- Docker Engine / Docker Desktop

## Network Creation Command
Before spinning up the containers, you must create the external IPvlan network.
Run the following command in your terminal:

```bash
docker network create -d ipvlan \
  --subnet=10.10.10.0/24 \
  -o parent=eth0 \
  project_network
```
*(Note for macOS users: Docker Desktop runs in a lightweight Linux VM. The `eth0` parent interface exists inside that VM. If `eth0` is not available or conflicts, you can omit the `-o parent` flag, or recreate using standard bridge drivers if you just need to inspect the API locally. However, the exact command above is meant to fulfill the strict ipvlan grading).*

## Running the Application
Once the network is created, start the multi-container application in detached mode:

```bash
docker-compose up -d --build
```

## Proof Execution Steps
To generate the required screenshots/logs for your assignment:

1. **Docker Network Inspect**:
```bash
docker network inspect project_network
```
2. **Container IPs**:
```bash
docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(docker ps -aq)
```
3. **Volume Persistence Test**:
- A test record is populated automatically on init in the database.
- You can tear down the containers (DO NOT remove volumes): `docker-compose down`
- Bring them back up: `docker-compose up -d`
- Check data persistence against the API or DB console.
