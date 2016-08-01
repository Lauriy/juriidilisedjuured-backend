#!/bin/bash
export HOME=/home/juriidilisedjuured
cd $HOME
source .virtualenvs/juriidilisedjuured-prod/bin/activate
cd $HOME/juriidilisedjuured-backend/
python manage.py collectstatic --noinput
uwsgi --socket /home/juriidilisedjuured/juriidilisedjuured-backend/jj.sock --module juriidilisedjuured.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?