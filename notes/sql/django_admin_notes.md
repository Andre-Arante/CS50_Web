# Django-Admin

Create a super user
```
python manage.py createsuperuser
```

Add models to the admin.py folder

```
from .models import Flight, Airport

# Register your models here
admin.site.register(Airport)
admin.site.register(Flight)
```

Run the server and navigate to the /admin path -> enter credentials