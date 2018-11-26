# Template micro-API

This is a template Python microservice that uses Docker, docker-compose, Python, Flask, gunicorn, and gevent. It has a set of boilerplate that I like to use for running the server and running tests.

## Set up

Run `docker-compose up` to start the server. Run `make test` in another terminal to run tests.

The server code is in `src/server.py`.

`Dockerfile` will run the server with Alpine and Python 3.7 on port 5000.

## Howto

- Add new pip requirements: add them to `requirements.txt` or `dev-requirements.txt`
- Add new API endpoints: add them to `src/server.py`
- Change how the server boots: modify `scripts/start_server.sh`
- Change how the tests run: modify `scripts/run_tests.sh`
- Add extra services for testing: add them to `docker-compose.yaml`
- Automatically deploy to docker hub using `hooks/build`: enable integration from docker hub
- Enable CI tests: enable the integration from the Travis dashboard for your repo (see `./.travis.yml`)
