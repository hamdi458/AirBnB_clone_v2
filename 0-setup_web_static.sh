#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get update
sudo apt-get install nginx
mkdir -p /data/
mkdir -p /data/web_static/ 
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu: /data/
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /usr/share/nginx/html;
    index  index.html index.htm;
    
    }
    location /hbnb_static{
    alias /data/web_static/current/;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx start