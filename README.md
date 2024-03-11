# claim-process-test

Take home coding test.

Trying something new by adapting a
[quasi-standard four layer architecture](https://github.com/nludban/pyramids-python-architecture)
to FastAPI based microservices using docker compose...

## Build

```docker build . -f backend_exe/Dockerfile -t takehome/claims_process:0.0.1```


## Run

```docker-compose  -f docker-compose.yml up```


## Web Access

http://localhost:8080/ -- claim_process API

http://localhost:8081/ -- adminer DB UI (see settings below)

![adminer credentials](adminer-login.png)
