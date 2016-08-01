#!/bin/bash
export HOME=/home/juriidilisedjuured
cd $HOME/juriidilisedjuured-backend/
source ~/.bashrc
workon juriidilisedjuured-prod
python manage.py collectstatic
uwsgi --socket /home/juriidilisedjuured/juriidilisedjuured-backend/jj.sock --module juriidilisedjuured.wsgi --chmod-socket=777 --env=LANG="en_US.utf8"
exit $?