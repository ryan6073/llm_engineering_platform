#!/bin/bash
# Development server startup script for FastAPI application, uv-aware

# Default values
HOST=${FASTAPI_HOST:-0.0.0.0}
PORT=${FASTAPI_PORT:-8000}
LOG_LEVEL=${LOG_LEVEL:-info}
RELOAD_FLAG="--reload"
USE_UV_RUN=true # Set to false to use manual venv activation

# Check for .env file and load it if it exists
if [ -f .env ]; then
  # Source .env to make variables available to this script
  set -o allexport
  source .env
  set +o allexport
fi

# Update HOST and PORT if they are set in .env, overriding defaults
HOST=${FASTAPI_HOST:-$HOST}
PORT=${FASTAPI_PORT:-$PORT}
LOG_LEVEL=${LOG_LEVEL:-$LOG_LEVEL}

echo "Starting FastAPI development server..."
echo "Host: $HOST"
echo "Port: $PORT"
echo "Log Level: $LOG_LEVEL"
echo "Reload: Enabled"

# Check if uv is installed
if ! command -v uv &> /dev/null
then
    echo "uv could not be found. Please install uv: https://github.com/astral-sh/uv"
    USE_UV_RUN=false # Fallback to standard venv if uv is not found
fi

if [ "$USE_UV_RUN" = true ] && command -v uv &> /dev/null; then
  echo "Using 'uv run' to start Uvicorn..."
  uv run uvicorn app.main:app --host "$HOST" --port "$PORT" --log-level "$LOG_LEVEL" $RELOAD_FLAG
else
  echo "Attempting to use standard virtual environment..."
  # Activate virtual environment if it exists and is not already active
  if [ -d ".venv" ] && [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment '.venv'..."
    source .venv/bin/activate
  elif [ -n "$VIRTUAL_ENV" ]; then
    echo "Already in a virtual environment: $VIRTUAL_ENV"
  else
    echo "Warning: Not in a virtual environment and '.venv' not found. Dependencies might not be correctly resolved."
  fi

  if ! command -v uvicorn &> /dev/null
  then
      echo "Uvicorn could not be found. Please ensure it is installed in your environment."
      echo "Try: uv pip install uvicorn[standard] or pip install uvicorn[standard]"
      exit 1
  fi
  uvicorn app.main:app --host "$HOST" --port "$PORT" --log-level "$LOG_LEVEL" $RELOAD_FLAG
fi
