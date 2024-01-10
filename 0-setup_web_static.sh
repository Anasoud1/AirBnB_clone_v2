#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static.

#sudo apt-get update
#sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
echo "Holberton School" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data/
chgrp -R ubuntu /data/
string_replacement="location \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\tindex index.html index.htm;\n\t}\n\tservice_name _;"
sed -i "s/service_name _;/$string_replacement/" /etc/nginx/sites-enabled/default

sudo service nginx restart
