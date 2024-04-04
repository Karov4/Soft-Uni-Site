import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Soft_Uni_Site.settings')
django.setup()


from django.contrib.auth.models import Group, Permission


def create_groups():
    # create a renters group
    renters_group, created = Group.objects.get_or_create(name='Renters')

    # add view and rent permissions to the renters group
    view_permission = Permission.objects.get(codename='view_apartment')
    rent_permission = Permission.objects.get(codename='add_rent')
    renters_group.permissions.set([view_permission, rent_permission])

    # create a leasers group
    leasers_group, created = Group.objects.get_or_create(name='Leasers')

    # add all apartment permissions to the leasers group
    apartment_permissions = Permission.objects.filter(content_type__app_label='users', content_type__model='apartment')
    leasers_group.permissions.set(apartment_permissions)

if __name__ == '__main__':
    create_groups()
