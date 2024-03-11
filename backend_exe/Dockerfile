# Base python
FROM python:3.12

WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Requirements layer
COPY backend_exe/requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Component layer
COPY ./bin /code/bin
COPY ./backend_exe /code/backend_exe
COPY ./libdb /code/libdb
COPY ./claimprocess /code/claimprocess
COPY ./payments /code/payments

# Run the service
CMD ["bin/backend", "--host", "0.0.0.0", "--port", "8001"]
