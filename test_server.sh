#!/usr/bin/env bash

for i in $(seq 10);
do
	echo $(curl -X 'GET' C  'https://crawler.0x30c4.dev/v1/?search_query=google.com&limit=5' -s  -H 'accept: application/json' ) &
done
