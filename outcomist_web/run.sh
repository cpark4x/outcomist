#!/bin/bash

set -e

cd "$(dirname "$0")"

if [ ! -f .env ]; then
    echo "Error: .env file not found!"
    echo "Please copy .env.example to .env and add your ANTHROPIC_API_KEY"
    exit 1
fi

export $(grep -v '^#' .env | xargs)

if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "Error: ANTHROPIC_API_KEY not set in .env file"
    exit 1
fi

echo "Starting Outcomist Web..."
echo "Open http://localhost:8000 in your browser"
echo ""

uv run uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
