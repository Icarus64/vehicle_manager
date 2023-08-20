from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy

class CreateMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='Super Admin').exists():
            return True
        raise PermissionDenied
    
    def handle_no_permission(self):
        return reverse_lazy('forbidden')
    
class DeleteMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='Super Admin').exists():
            return True
        raise PermissionDenied
    
    def handle_no_permission(self):
        return reverse_lazy('forbidden')

class EditMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='Admin').exists():
            return True
        elif self.request.user.groups.filter(name='Super Admin').exists():
            return True
        raise PermissionDenied
    
    def handle_no_permission(self):
        return reverse_lazy('forbidden')

class ViewMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user.groups.filter(name='User').exists():
            return True
        elif self.request.user.groups.filter(name='Admin').exists():
            return True
        elif self.request.user.groups.filter(name='Super Admin').exists():
            return True
        raise PermissionDenied
    
    def handle_no_permission(self):
        return reverse_lazy('forbidden')
