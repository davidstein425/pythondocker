FROM tutum/nginx
RUN rm /etc/nginx/sites-enabled/default
Add pytest.conf /etc/nginx/sites-enabled

# pytest.conf is an nginx config file that knows how to talk to the python service on port 8080
# This file tells Nginx to listen on port 80 and pass everything through to whatever is running inside container on port 8080, returing the result to the user