# GNU Health — Local Setup Guide

This project runs **GNU Health 5.x** locally using Docker. It includes:

- **PostgreSQL** — database server
- **GNU Health app** — Tryton server + SAO web client
- **Nginx** — reverse proxy for the web UI

## Prerequisites

1. **Docker Desktop** installed and running on macOS
2. At least **8 GB RAM** allocated to Docker (Settings → Resources)
3. **~5 GB free disk space** for images and database volumes

Verify Docker is running:

```bash
docker info
```

## Quick Start

From the project root (`/Users/mac/Documents/gnu-heath`):

```bash
./scripts/start.sh
```

First run builds images and initializes databases. This can take **20–40 minutes**.

When ready, open:

**http://localhost:8090**

## Login Credentials

| Field    | Value          |
|----------|----------------|
| Database | `health`       |
| Username | `admin`        |
| Password | `gnusolidario` |

> **Note:** The `ghdemo44` demo database is not used with this setup. It was built for GNU Health 4.4 and is incompatible with the GNU Health 5.x server installed here.

## Start and Stop

### Start

```bash
./scripts/start.sh
```

Or manually:

```bash
docker compose up -d --build   # first time or after code changes
docker compose up -d           # subsequent starts
```

### Stop (keeps data)

```bash
./scripts/stop.sh
```

Or manually:

```bash
docker compose down
```

Database and attachments are stored in Docker volumes (`db-data`, `app-data`) and persist across restarts.

### Stop and delete all data

```bash
docker compose down -v
```

This removes volumes and resets both databases. You will need to wait for re-initialization on the next start.

## Helper Scripts

| Script              | Purpose                              |
|---------------------|--------------------------------------|
| `scripts/start.sh`  | Build (if needed) and start services |
| `scripts/stop.sh`   | Stop all containers                  |
| `scripts/status.sh` | Show container status                |
| `scripts/logs.sh`   | Follow logs (`app` by default)       |

Examples:

```bash
./scripts/status.sh
./scripts/logs.sh          # app logs
./scripts/logs.sh db       # database logs
./scripts/logs.sh web      # nginx logs
```

## Configuration

Environment variables are in `.env`:

```env
GNUHEALTH_DB_HOST="db"
GNUHEALTH_DB_PORT=5432
GNUHEALTH_DB_USERNAME=gnuhealth
GNUHEALTH_DB_PW=gnusolidario
GNUHEALTH_DB_NAME=health
GNUHEALTH_ADMIN_MAIL=example@example.com
GNUHEALTH_ADMIN_PW=gnusolidario
GNUHEALTH_DEMO_DB=true
```

To change the web port, edit `docker-compose.yml`:

```yaml
ports:
  - "8090:80"   # change 8090 to your preferred port
```

Port **8080** is avoided by default because it is commonly used by other local services.

## Architecture

```
Browser  →  Nginx (:8090)  →  GNU Health app (:8000)  →  PostgreSQL (:5432)
```

Services:

| Container       | Image / build   | Role                    |
|-----------------|-----------------|-------------------------|
| `gnu-heath-db-1`  | postgres:16.2   | Database                |
| `gnu-heath-app-1` | gnu-heath-app   | GNU Health + uWSGI      |
| `gnu-heath-web-1` | nginx:1.25.4    | Web reverse proxy       |

## Troubleshooting

### "Docker is not running"

Start Docker Desktop, wait until the whale icon is steady, then retry.

### Port already in use

```bash
lsof -i :8090
```

Change the host port in `docker-compose.yml` if needed.

### FORBIDDEN / Bad Gateway on login

This usually means the browser Origin header did not match what Tryton expected behind the nginx proxy. The nginx config strips `Origin` for local development to prevent this.

If you still see it:

1. Use **http://localhost:8090** (not `127.0.0.1` unless both are in cors config).
2. Hard-refresh the page: **Cmd+Shift+R** (Mac) or **Ctrl+Shift+R** (Windows/Linux).
3. Clear site data for `localhost:8090` in browser settings.
4. Use database **`health`** (not `ghdemo44`).
5. Restart: `./scripts/stop.sh && ./scripts/start.sh`

### 502 Bad Gateway after start

The app is still initializing databases. Watch progress:

```bash
./scripts/logs.sh app
```

First startup imports the demo database and can take **5–15 minutes**.

### Rebuild after changes

```bash
docker compose down
docker compose up -d --build
```

### Desktop client (optional)

You can also use the native GNU Health client instead of the web UI:

```bash
pip3 install --user gnuhealth-client
gnuhealth-client
```

Connect to `localhost:8000` (the app port inside Docker; not exposed to the host by default). To expose it, add to the `app` service in `docker-compose.yml`:

```yaml
ports:
  - "8000:8000"
```

## What Was Set Up

This workspace uses the Docker setup from [csvl/lims](https://github.com/csvl/lims), which installs GNU Health via `gnuhealth-all-modules` (pip) rather than compiling from source. The original `docker-compose/gnuhealth` setup in this repo is kept for reference but is not used for local development due to upstream build issues with GNU Health 4.4+.

## References

- [GNU Health documentation](https://docs.gnuhealth.org/his)
- [Demo database guide](https://docs.gnuhealth.org/his/techguide/demodb.html)
- [GNU Health project](https://www.gnuhealth.org/)
