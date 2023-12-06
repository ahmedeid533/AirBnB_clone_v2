#!/usr/bin/env bash
# create some folders and files to connect by nginx
sudo apt-get -y update
sudo apt-get install -y nginx
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo 'this is solve for task number 0 in airbnb V_2' > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown ubuntu:ubuntu /data/
echo 'server  {
    listen 80
    listen 80[::] dafualt
    server_name realemildawood.tech
    location /hbnb_static {
        alias /data/web_static/current/;
    }
}' > /etc/nginx/sites-available/default
sudo nginx -s reload
