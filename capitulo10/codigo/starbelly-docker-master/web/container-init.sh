#!/bin/bash

if [ ! -e /etc/nginx/tls/server.key ]; then
  echo "*****************************************"
  echo "* WARNING!!!                            *"
  echo "*                                       *"
  echo "* Generating a self-signed certificate. *"
  echo "*****************************************"
  cd /tmp && \
      openssl req -x509 -newkey rsa:2048 \
                  -keyout server.key -out server.crt \
                  -days 365 -nodes -subj '/CN=starbelly' && \
      mv server.key server.crt /etc/nginx/tls
fi

if [ ! -e /etc/nginx/tls/starbelly_htpasswd ]; then
  echo "*****************************************"
  echo "* WARNING!!!                            *"
  echo "*                                       *"
  echo "* Creating default admin account.       *"
  echo "*****************************************"
  htpasswd -bc /etc/nginx/tls/passwd admin admin
fi

echo "Starting nginx..."
exec nginx -g "daemon off;"
