#!/bin/bash
set -e

echo "🎯 Qudra Academy - Railway Deployment"
echo "======================================"

# Install Node.js dependencies and build frontend
echo "📦 Building frontend..."
cd frontend
npm install
npm run build
cd ..

# Move frontend build to backend static folder
echo "📁 Setting up static files..."
mkdir -p backend/static
cp -r frontend/dist/* backend/static/

export PORT=${PORT:-8000}

echo "🚀 Starting server on port $PORT..."
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port $PORT
