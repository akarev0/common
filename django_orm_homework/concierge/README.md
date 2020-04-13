Build docker images
$ uid=$(id -u) gid=$(id -g) docker-compose build


Start compose
$ uid=$(id -u) gid=$(id -g) docker-compose up


Connect to the container
$ uid=$(id -u) gid=$(id -g) docker exec -ti concierge_app_1 bash


Load fixtures from file (in container)
# concierge/manage.py loaddata --format=json concierge/fixtures/staff_initial_data.json


Collect staticfiles
# concierge/manage.py collectstatic --noinput


Create super user
# concierge/manage.py createsuperuser


Apply migrations
# concierge/manage.py migrate

Add working form:
hint: date format '2006-10-25'

homework middleware:

1. Add cache (redis) to my project. Set cache "Tenant List" page (TTL=5 min)
2.Add middleware, that calculates and logs to console 'generation' time(1 sec) for each requested page.
3. Add user "tenant", password '686775gJ' with permission:
    - can view tenant;
    - can view journal.
4. Add user "Concierge", password '686775gJ' with permission:
    - can view journal;
    - can add journal;
    - can change journal;
    - can delete journal;