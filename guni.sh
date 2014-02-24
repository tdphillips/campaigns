#!/bin/bash
set -e
LOGDIR=/home/tdphillips/projects/campaigns/logs
NUM_WORKERS=3

PATH=$PATH:/home/tdphillips/.virtualenvs/campaigns/bin

PROJECT_DIR=/home/tdphillips/projects/campaigns
USER=tdphillips
GROUP=tdphillips
ADDRESS=127.0.0.1:8001
cd $PROJECT_DIR
source /home/tdphillips/.virtualenvs/campaigns/bin/activate
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn campaigns:app -w $NUM_WORKERS --bind=$ADDRESS --user=$USER --group=$GROUP --log-level=debug --log-file=$LOGDIR/access.log 2>>$LOGDIR/error.log
