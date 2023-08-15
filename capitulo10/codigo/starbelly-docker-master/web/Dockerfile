FROM nginx:1.11
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV PUB_CACHE=/var/cache/pub

# Install OS packages.
RUN apt-get update && \
    apt-get install -y apt-transport-https curl apache2-utils unzip && \
    rm -fr /var/cache/apt/archives/*

# Install Dart
RUN curl 'https://storage.googleapis.com/dart-archive/channels/stable/release/2.7.1/sdk/dartsdk-linux-x64-release.zip' -o /opt/dartsdk-linux-x64-release.zip
RUN cd /opt && unzip dartsdk-linux-x64-release.zip
ENV PATH=$PATH:/opt/dart-sdk/bin

# Configure nginx.
RUN rm /etc/nginx/conf.d/default.conf && \
    mkdir /etc/nginx/tls
COPY nginx.conf /etc/nginx/conf.d/starbelly.conf

# Get Starbelly source code.
COPY dependencies/starbelly-web-client /starbelly-web-client

# Build the web client code. (The --no-release flag is required because the client
# doesn't work in release mode... not sure why?)
ENV PATH=$PATH:/var/cache/pub/bin
RUN mkdir -p $PUB_CACHE && \
    cd /starbelly-web-client && \
    pub get && \
    pub global activate webdev 2.5.4 && \
    webdev build --no-release

ENV PS1='starbelly-web:$PWD# '

# Container init script.
COPY container-init.sh /container-init.sh
RUN chmod +x /container-init.sh
CMD /container-init.sh
