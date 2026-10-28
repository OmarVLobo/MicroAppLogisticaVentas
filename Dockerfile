FROM python:3.12.3-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || echo "MicroApp LogVent"
COPY . .
VOLUME /app/Data
CMD ["python", "MainMicroAppLogisticaVentas.py"] 
