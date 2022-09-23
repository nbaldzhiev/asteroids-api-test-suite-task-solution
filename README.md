# Asteroids API Test Suite

A repository containing a Asteroids API Test Suite.

> **_NOTE:_** The bash scripts were developed on MacOS Monterey 12.6, so there could be some command differences with the shells of other OSs.

## Usage

**tldr:**

```
$ git clone git@github.com:nbaldzhiev/asteroids-api-test-suite-task-solution.git && cd asteroids-api-test-suite-task-solution
$ ./runner.sh
```

What happens:
1. A docker image gets built based on Dockerfile.
  * By default, the docker image is built first, i.e. it is not implied that it already exists. This is configurable.
2. A container gets started with the image.
3. The tests are ran inside the container.
4. An allure report server is started on the localhost based on the results copied from the container.
  * By default, an Allure web server is started with the report from the test suite execution. This is configurable.
5. The container is stopped and removed.

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
