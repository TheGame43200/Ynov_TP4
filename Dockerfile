FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pylint

CMD ["python", "-m", "unittest", "test_simple_math.py"]