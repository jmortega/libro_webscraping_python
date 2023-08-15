# Starbelly: Docker

This repository contains Dockerfiles and Docker Compose files for [the Starbelly
crawler](https://gitlab.com/hyperion-gray/starbelly). This README explains how
to build Docker images. For information on running Docker containers, see the
[Starbelly documentation](https://starbelly.readthedocs.io).

## Building Images

This repo contains the Dockerfiles to build two production images (`app` and
`web`) as well as a Docker Compose file to run a standard production setup. In
practice, production images are published to Docker Hub, so you shouldn't need
to build your own images.

You need some dependencies to build Docker images. This assumes that you have
the `starbelly` and `starbelly-web-client` repos checked out in the same
directory as `starbelly-docker`. `$STARBELLY_ROOT` must point to the path that
contains all of these repos. Perform this intial setup:

    $ cd $STARBELLY_ROOT/starbelly-docker/app/dependencies
    $ git clone ../../../starbelly
    $ cd $STARBELLY_ROOT/starbelly-docker/web/dependencies
    $ git clone ../../../starbelly-web-client

When you want to update the Docker images to match your local repos, you can run
`git pull` in each of these repos, but when you want to produce official release
images, you should `git clean -fx && git checkout $STARBELLY_TAG`, where the tag
variable contains the version tag that is being released, e.g. `1.0.0`.

Next, then run these commands from the project root:

    $ docker build -t starbelly-app app
    $ docker build -t starbelly-web web

## Publishing Images

To upload release images to Docker Hub, you need to tag them and push them:

    $ docker tag starbelly-app hyperiongray/starbelly-app:$STARBELLY_TAG
    $ docker tag starbelly-web hyperiongray/starbelly-web:$STARBELLY_TAG
    $ docker push hyperiongray/starbelly-app:$STARBELLY_TAG
    $ docker push hyperiongray/starbelly-web:$STARBELLY_TAG

Note that `$STARBELLY_TAG` should be the version number that you want to
release. You should update `docker-compose.yml` with these new version numbers
after pushing.

## Running containers

Run the containers with Docker Compose:

    $ docker-compose up

Now you can connect to Starbelly using a browser. The default username and password are
`admin` and `admin`.
