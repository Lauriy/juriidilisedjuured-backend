#!/bin/bash
export HOME=/home/juriidilisedjuured
cd $HOME/juriidilisedjuured-backend/
workon juriidilisedjuured-prod
uwsgi --socket /home/juriidilisedjuured/juriidilisedjuured-backend/jj.sock --module juriidilisedjuured.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?