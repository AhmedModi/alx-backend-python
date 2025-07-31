from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def delete_user(request):
    user = request.user
    logout(request)  # Log user out before deleting
    user.delete()
    return redirect('home')  # Replace with your actual redirect URL
