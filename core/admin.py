from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from core.models import Customer

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'customers'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (CustomerInline, )

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'cpf', 'date_of_birth', 'created_date', 'modified_date', )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Customer, CustomerAdmin)
