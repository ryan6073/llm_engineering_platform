# Start with a Python base image (choose a specific version for reproducibility)
FROM python:3.10-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=on
ENV PIP_DEFAULT_TIMEOUT=100

# Set work directory in the container
WORKDIR /app

# Install system dependencies if any are needed by your Python packages
# For example, if a library needs gcc or other build tools:
# RUN apt-get update && apt-get install -y --no-install-recommends #     build-essential #     curl #     && rm -rf /var/lib/apt/lists/*

# Copy only requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
# If using uv, you might install it first and then use it to install requirements
# RUN pip install uv
# RUN uv pip install --no-cache --system -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Expose the port your application runs on (e.g., for FastAPI)
# Ensure this matches the port Uvicorn or your app server is configured to use
EXPOSE 8000 

# Command to run the application
# This will depend on how your application is started.
# For a FastAPI application in app/main.py with an app object named `app`:
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# If your main entry point is a script, e.g., src/main_script.py:
# CMD ["python", "src/main_script.py"]
