from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View


class UserAdminView(View):

    def get(self, request):
        if self.request.user.is_authenticated():
            return render(request, 'useradmin/admin.html')
        else:
            return redirect('account_login')

