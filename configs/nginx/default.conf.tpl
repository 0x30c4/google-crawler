upstream backend {
    server $APP_CONT_DOMAIN:$PORT;
}

server {
    listen $NGINX_LISTEN_PORT;

    add_header Access-Control-Allow-Origin *;

    location / {
        limit_req zone=limitfordemo burst=1;
        proxy_pass http://backend/;
    }

    location /api/ {
        proxy_pass http://backend/;
    }
}
