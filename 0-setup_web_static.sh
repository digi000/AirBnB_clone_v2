#!/usr/bin/env bash

if ! command -v nginx >/dev/null 2>&1; then
        sudo apt install nginx -y
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "Hello Niarobi" | sudo tee /data/web_static/releases/test/index.html
sudo rm /data/web_static/current > /dev/null 2>&1
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed "/listen *:80;/a \nlocation /hbnb_static/ {\n  alias /data/web_static/current/\n};" /etc/nginx/sites-available/default
sudo systemctl restart nginx
