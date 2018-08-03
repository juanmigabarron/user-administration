from django.contrib.admin import AdminSite


class AdministrationSite(AdminSite):
    site_title = 'Administration Site'
    site_header = 'User Administration'
    index_title = 'Administration Site'
    login_template = 'administration/login.html'

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        *at least one* page in the admin site.
        """
        return request.user.is_active

admin_site = AdministrationSite(name='administration')
