### STEPS

1. `python manage.py startapp job`
` docker-compose run --rm app sh -c "python
 manage.py wait_for_db && python manage.py startapp job"
`
2. delete `models.py` and `migrations` because all DB models 
are defined under `core`

3. delete `tests.py` because we are creating package named `tests`
4. mention `job` application in `app/app/settings.py`
5. define viewset in `job/views.py`
6. define URLs in `job/urls.py`
7. create superuser
`docker-compose run --rm app sh -c "python
 manage.py wait_for_db && python manage.py createsuperuser"`
8. create resource records in DB using following ORM queries in `django shell`
`docker-compose run --rm app sh -c "python
 manage.py wait_for_db && python manage.py shell"`


```python
from core.models import JobTitle, JobDescription, Portal
from django.contrib.auth import get_user_model

jd = JobDescription.objects.create(user=user, role="python developer", description_text="random")
portal = Portal.objects.create(user=user, name="naukri.com", description="indias famous one")
user = get_user_model().objects.get(pk=1)
job_title = JobTitle.objects.create(user=user, title="random title", job_description=jd, portal=portal)
```
9. HTTP GET `localhost:8000/api/job/jobtitle/`