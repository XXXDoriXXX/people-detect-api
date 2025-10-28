# Dockerfile

FROM python:3.10-slim

WORKDIR /app

# --- ПОЧАТОК ЗМІН ---
# Додаємо libglib2.0-0, ще одну залежність для OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*
# --- КІНЕЦЬ ЗМІН ---

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]