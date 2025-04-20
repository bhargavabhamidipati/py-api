FROM python:3.11-slim

RUN pip install --upgrade pip

WORKDIR /app
COPY . /app

# Install OS-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]

