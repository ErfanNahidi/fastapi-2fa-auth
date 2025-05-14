FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY ./streamlit_app.py .
RUN pip install -r requirements.txt
COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]
