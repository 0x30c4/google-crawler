
build-dev:
	docker build -t google-sc .
	docker build -t api_revers_proxy -f ./configs/nginx/Dockerfile ./configs/nginx/

build-prod:
	docker build -t google-sc-prod .
	docker build -t api_revers_proxy -f ./configs/nginx/Dockerfile ./configs/nginx/

run-dev:
	./scripts/chmod-666-to-log-files.sh
	docker-compose --env-file env/.env.dev -f docker-compose.dev.yml up

run:
	./scripts/chmod-666-to-log-files.sh
	docker-compose --env-file env/.env.prod -f docker-compose.prod.yml up -d

restart-dev:
	docker-compose --env-file env/.env.dev -f docker-compose.dev.yml down
	docker-compose --env-file env/.env.dev -f docker-compose.dev.yml up

restart-prod:
	docker-compose --env-file env/.env.dev -f docker-compose.prod.yml down
	docker-compose --env-file env/.env.dev -f docker-compose.prod.yml up -d

stop-dev:
	docker-compose --env-file env/.env.dev -f docker-compose.dev.yml down

stop-prod:
	docker-compose --env-file env/.env.prod -f docker-compose.prod.yml down


push-pull:
	git add .
	git commit -m "pushed from make"
	git push
	ssh google_parser -t "cd google-crawler;git pull"
