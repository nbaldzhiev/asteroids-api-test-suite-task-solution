# Asteroids API Test Suite

A repository containing a Asteroids API Test Suite.

## Usage

**tldr:**

```
$ git clone git@github.com:nbaldzhiev/asteroids-api-test-suite-task-solution.git && cd asteroids-api-test-suite-task-solution`
$ ./runner.sh
```

* The tests are ran via the `runner.sh` script.
* The `Dockerfile` contains the image build information.
* The script `run_tests.sh` is inserted in the container and is ran there.
* The results of the tests are copied from the docker container to the repository directory.
* By default, an Allure web server is started with the report from the test suite execution. This is configurable.
* By default, the docker image is built first, i.e. it is not implied that it already exists. This is configurable.

It's recommended to create a python virtual environment using Python 3.8+ and install the dependencies in the file requirements.txt to ensure that all required packages are available.

## Examples

The script accepts two optional arguments:
1. The first one controls whether the container image is first built or not. Set it to False in order not to
build an image, i.e. ./runner.sh False. Otherwise, an image would be built first.
2. The second one controls whether the allure report is opened as a web server. Set it to False in order not to
start an allure server with the report, i.e. ./runner.sh False False

`$ ./runner.sh - Default. Builds the docker image and opens an Allure server with the report.`

`$ ./runner.sh False - Don't build an image, start the Allure server.`

`$ ./runner.sh False False - Don't build an image, don't start the Allure server.`

`$ ./runner.sh True False - Build an image, don't start the Allure server.`

`$ ./runner.sh True True - same as default ./runner.sh - builds a docker image and opens an Allure server.`
