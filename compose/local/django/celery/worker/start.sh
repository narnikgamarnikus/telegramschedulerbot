#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A telegramschedulerbot.taskapp worker -l INFO
