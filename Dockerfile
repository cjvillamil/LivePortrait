FROM runpod/pytorch:2.1.0-py3.10-cuda11.8.0-devel-ubuntu22.04

# Dependencias de sistema requeridas para procesamiento de video y visión
RUN apt-get update && apt-get install -y ffmpeg libsm6 libxext6 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar dependencias de Python y el SDK de RunPod
COPY requirements*.txt ./
RUN pip install --no-cache-dir -r requirements.txt runpod

# Copiar código fuente y pesos del modelo
COPY . .

# Comando de ejecución del worker
CMD ["python", "-u", "handler.py"]