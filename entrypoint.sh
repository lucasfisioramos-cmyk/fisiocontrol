#!/bin/sh
set -e

echo "Starting entrypoint: waiting for DB and running migrations..."

MAX_RETRIES=15
RETRY_COUNT=0
SLEEP_SECONDS=3

until flask db upgrade; do
  RETRY_COUNT=$((RETRY_COUNT+1))
  if [ "$RETRY_COUNT" -ge "$MAX_RETRIES" ]; then
    echo "Could not run migrations after $RETRY_COUNT attempts, exiting."
    exit 1
  fi
  echo "Migration failed, retrying in $SLEEP_SECONDS seconds... ($RETRY_COUNT/$MAX_RETRIES)"
  sleep $SLEEP_SECONDS
done

echo "Migrations applied. Starting application..."

exec "$@"
