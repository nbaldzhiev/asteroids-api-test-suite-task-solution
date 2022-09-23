#!/bin/bash

#
# The script has been developed and tested on MacOS Monterey 12.6, so there could be some differences with other OSs
# Usage:
#
# The script accepts two optional arguments:
#   1) the first one controls whether the container image is first built or not. Set it to False in order not to
#      build an image, i.e. ./runner.sh False. Otherwise, an image would be built first.
#   2) the second one controls whether the allure report is opened as a web server. Set it to False in order not to
#      start an allure server with the report, i.e. ./runner.sh False False
#
# Examples:
#
# $ ./runner.sh - Default. Builds the docker image and opens an Allure server with the report.
# $ ./runner.sh False - Don't build an image, start the Allure server.
# $ ./runner.sh False False - Don't build an image, don't start the Allure server.
# $ ./runner.sh True False - Build an image, don't start the Allure server.
# # ./runner.sh True True - same as default ./runner.sh - builds a docker image and opens an Allure server.
#
# TODO: improve the script to accept keyword arguments, i.e. --build-image=False --start-allure=False
#

IMAGE_NAME='sbdb-api-tests-image'
APP_NAME='sbdb-api-tests-app'
DEFAULT_INTERVAL_SEC=0.5

if docker info ; then
  if [[ $1 != 'False' ]] ; then
    echo 'Starting the process of building a new docker image with the tests app...'
    docker build --tag $IMAGE_NAME .
    echo 'Successfully built the docker image!'
  fi
  docker run -d $IMAGE_NAME
  echo 'Ran the container in detached mode.'
  CONTAINER_ID=$(docker ps | grep $IMAGE_NAME | awk '{print $1}')
  while [ $(docker top $CONTAINER_ID | grep pytest | awk '{print $1}') ]
  do
    echo 'Waiting for pytest to complete...'
    sleep $DEFAULT_INTERVAL_SEC
  done
  echo 'pytest has completed!'
  rm -rf results/
  echo 'Cleaned any existing results/ folders...'
  docker cp $CONTAINER_ID:/$APP_NAME/results .
  echo 'Copied the results/ folder from the container to the localhost directory of the repo!'
  docker rm --force $CONTAINER_ID
  echo 'Forcefully removed the container.'
  if [[ $2 != 'False' ]] ; then
    if allure --version ; then
      rm -rf allure-report/
      echo 'Cleaned any existing allure-report/ folders...'
      allure generate results/
      echo 'Generated the allure report.'
      echo 'Starting a web server to open the allure report...'
      allure open allure-report/
    else
      echo 'Allure seems to be not installed/not working! Please either start or install Allure.'
    fi
  fi
else
  echo 'The command "docker info" was unsuccessful! Please either start or install Docker.'
fi
