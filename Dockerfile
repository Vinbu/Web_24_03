FROM python:3.9-slim

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD ["python3", "validar.py"]