#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

if ! docker info >/dev/null 2>&1; then
  echo "Docker is not running. Start Docker Desktop, then run this script again."
  exit 1
fi

mkdir -p db-log app-log web-log

echo "Building and starting GNU Health (first run can take 15-30 minutes)..."
docker compose up -d --build

echo
echo "GNU Health is starting."
echo "  Web UI:  http://localhost:8090"
echo "  Database: health"
echo "  User:    admin"
echo "  Password: gnusolidario"
echo
echo "First startup initializes databases and may take several minutes."
echo "Check progress: docker compose logs -f app"
