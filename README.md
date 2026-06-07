# GNU Health — Local Development

Run GNU Health locally with Docker.

## Quick start

```bash
./scripts/start.sh
```

Open **http://localhost:8090** and log in with database `health`, user `admin`, password `gnusolidario`.

## Stop

```bash
./scripts/stop.sh
```

## Full guide

See [docs/LOCAL_SETUP.md](docs/LOCAL_SETUP.md) for prerequisites, configuration, troubleshooting, and architecture details.

## Project layout

```
gnu-heath/
├── docker-compose.yml    # Main stack (db + app + nginx)
├── gnuhealth/            # App Docker image (GNU Health 5.x)
├── web-site/             # Nginx reverse proxy config
├── scripts/              # start.sh, stop.sh, status.sh, logs.sh
├── docs/LOCAL_SETUP.md   # Setup and operations guide
└── docker-compose/       # Legacy setup (not used locally)
```
