upstream backend {
    server $APP_CONT_DOMAIN:$PORT;
}

server {
    listen $NGINX_LISTEN_PORT;

    add_header Access-Control-Allow-Origin *;

    location / {
        proxy_pass http://backend;
    }
}
