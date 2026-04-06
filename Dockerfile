FROM python:3.12-slim

WORKDIR /app

# Install Python deps (cached unless requirements.txt changes)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy pre-built frontend + backend
COPY frontend/dist/ frontend/dist/
COPY backend/ backend/

# Copy static frontend into backend serving directory
RUN mkdir -p backend/static && cp -r frontend/dist/* backend/static/

ENV PORT=8000
EXPOSE ${PORT}

WORKDIR /app/backend
CMD python -m uvicorn main:app --host 0.0.0.0 --port ${PORT}
