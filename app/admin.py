from django.contrib import admin

from .models import User
from .models import Product
from .models import Comments
from .models import Creator
from .models import Order

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Creator)
admin.site.register(Order)


