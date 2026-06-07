#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT_DIR}"

echo "Stopping GNU Health..."
docker compose down

echo "GNU Health stopped. Database data is kept in the db-data Docker volume."
