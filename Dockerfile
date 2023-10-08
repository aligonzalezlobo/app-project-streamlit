# app_project_alicia/Dockerfile

FROM python:3.9-slim

WORKDIR /app_project_alicia

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "airbnb_app.py", "--server.port=8501", "--server.address=0.0.0.0"]


