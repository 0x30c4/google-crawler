#!/usr/bin/env bash


LOG_DIR=$(grep "NGINX_LOG_DIR_HOST" env/.env.dev | cut -d = -f 2 | xargs -I{} echo {})

for i in $(grep "NGINX_..._LOG_FILE" env/.env.dev | cut -d "/" -f 3 | xargs -I{} echo {});
do
	touch $LOG_DIR/$i
	chmod 666 $LOG_DIR/$i
done

LOG_DIR=$(grep "^LOG_DIR_HOST" env/.env.dev | cut -d = -f 2 | xargs -I{} echo {})

for i in $(grep "APP_LOG_FILE" env/.env.dev | cut -d "/" -f 3 | xargs -I{} echo {});
do
	touch $LOG_DIR/$i
	chmod 666 $LOG_DIR/$i
done
