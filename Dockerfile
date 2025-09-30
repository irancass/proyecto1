FROM python:3.9-slim
WORKDIR /app
COPY SerApp.py /app
COPY templates/ /app/templates
COPY static/ /app/static
RUN pip install --upgrade pip
RUN pip install --no-cache-dir flask
EXPOSE 5000
CMD ["python3","SerApp.py"]
