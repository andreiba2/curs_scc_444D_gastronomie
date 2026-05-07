FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create non-root user
RUN adduser --disabled-password --gecos "" baklava

# Set working directory
WORKDIR /home/baklava

# Switch to non-root user
USER baklava

# Copy requirements
COPY --chown=baklava:baklava requirements.txt .

# Create and activate virtual environment
RUN python3 -m venv .venv && \
    .venv/bin/pip install --no-cache-dir --upgrade pip && \
    .venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY --chown=baklava:baklava app app
COPY --chown=baklava:baklava dockerstart.sh dockerstart.sh
COPY --chown=baklava:baklava pytest.ini pytest.ini

# Make script executable
RUN chmod +x dockerstart.sh

# Expose port
EXPOSE 8000

# Start application
ENTRYPOINT ["./dockerstart.sh"]