#!/usr/bin/env bash
# Prepare your web servers

# install nginx
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo sh -c 'echo "this is solve for first task"> /data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sh -c 'echo "server {
    listen 80;
    listen [::]:80 default_server;
    server_name realemildawood.tech;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default'
sudo nginx -s reload
sudo service nginx start
