FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./requirements.txt /crypto/requirements.txt
WORKDIR /
RUN pip install --no-cache-dir --upgrade -r /crypto/requirements.txt
COPY ./crypto /crypto
CMD ["uvicorn", "crypto.main:app", "--host", "0.0.0.0", "--port", "8000"]
