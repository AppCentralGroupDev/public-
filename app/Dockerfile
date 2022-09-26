FROM python:3.8.4

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY serve_completed.py /app/serve_completed.py

ENV FLASK_APP serve_completed.py

ENV FLASK_RUN_PORT 5050

CMD ["flask", "run", "--host=0.0.0.0"]

EXPOSE 5050