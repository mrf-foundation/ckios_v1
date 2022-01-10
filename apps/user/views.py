from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Import User UpdateForm, ProfileUpdatForm
from .forms import UserRegisterForm, UserUpdateForm, EditProfileForm, ProfileForm
from .models import Profile, UpdateProfileForm
from django.views import generic

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# Update it here
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/myprofile")
        else:
            messages.error(request, "Invalid Credentials")
        alert = True
        return render(request, 'login.html', {'alert':alert})
    return render(request, "login.html")
@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('registration/profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)



def myprofile(request):
    if request.method=="POST":
        user = request.user
        profile = Profile(user=user)
        profile.save()
        form = EditProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "registration/profile.html",{'obj':obj})
    else:
        form=EditProfileForm(Profile)
    return render(request, "registration/profile.html", {'form':form})


def edit_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        print = request.POST
        if form.is_valid():

            new_profile = Profile(
                            user = request.user,
                            bio = request.POST['bio'],
                            address = request.POST['address'],
                            age = request.POST['age']
                            )

            new_profile.save()

            return HttpResponseRedirect(reverse('user_public_profile', args=(request.user.username,)))
        return render(request,'registration/edit_profile.html', {'form': form})

    else:
        form = UpdateProfileForm()
        return render(request,'registration/edit_profile.html',
                          {'form': form})

class EditProfilePage(generic.CreateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)