#!/usr/bin/env python3

import logging
import os
from pathlib import Path
import subprocess
import sys

CONTAINER = 'starbelly_web'
CONTAINER_TLS = Path('/etc/nginx/tls')

logging.basicConfig()
logger = logging.getLogger('deploy-certbot')
logger.setLevel(logging.INFO)

try:
    domains_env = os.environ['RENEWED_DOMAINS']
    lineage_env = os.environ['RENEWED_LINEAGE']
except KeyError:
    logger.error('Missing environment variables RENEWED_DOMAIN and/or'
                 ' RENEWED_LINEAGE. Are you running this as a certbot deploy'
                 ' hook?')
    sys.exit(1)

logger.info('Renewed domains: %r', domains_env.split(' '))
src_path = Path(lineage_env)
cert_src = str((src_path / 'fullchain1.pem').resolve())
key_src = str((src_path / 'privkey1.pem').resolve())
cert_dst = '{}:{}'.format(CONTAINER, str(CONTAINER_TLS / 'server.crt'))
key_dst = '{}:{}'.format(CONTAINER, str(CONTAINER_TLS / 'server.key'))

try:
    logger.info('Copying %s to Docker %s', cert_src, cert_dst)
    subprocess.run(['docker', 'cp', cert_src, cert_dst], check=True)
    logger.info('Copying %s to Docker %s', key_src, key_dst)
    subprocess.run(['docker', 'cp', key_src, key_dst], check=True)
    logger.info('Reloading nginx...')
    subprocess.run(['docker', 'exec', CONTAINER, 'nginx', '-s', 'reload'],
        check=True)
except subprocess.CalledProcessError as cpe:
    logger.error('Failed to run command `%s` (exit %d):\n%s', cpe.cmd,
        cpe.returncode, cpe.stderr)
    sys.exit(1)

logger.info('Done')
