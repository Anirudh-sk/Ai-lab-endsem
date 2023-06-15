FROM python:3.9.5
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_SECRET_KEY="anirudh"
CMD ["flask", "run", "--host=0.0.0.0"]