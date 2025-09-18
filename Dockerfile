FROM python:3.11-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT ["python", "-m", "src.main"]
CMD ["--files", "data/students1.csv", "data/students2.csv", "--report", "student-performance"]