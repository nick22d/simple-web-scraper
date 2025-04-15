User-agent: *
Disallow: /private/
Allow: /public/

add the robots.txt file into /var/www/html path


/etc/nginx/sites-available/default
server {
    listen 80;
    server_name your-website.com;

    root /var/www/html;

    location / {
        try_files $uri $uri/ =404;
    }

    # Add a location block specifically for serving robots.txt
    location = /robots.txt {
        try_files $uri =404;
    }

    # Other existing location blocks...
}

sudo systemctl reload nginx

curl localhost/robots.txt