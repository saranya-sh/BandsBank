from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def homePage(request):
	return render(request, 'app/home.html')

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('instruments')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user )
				return redirect('login')
		context = {'form': form}
		return render(request, 'app/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('instruments')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('instruments')
			else:
				messages.info(request, 'Username or Password is incorrect')
		context = {}
		return render(request, 'app/login.html')

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def instrumentsPage(request):
	return render(request, 'app/instruments.html')

@login_required(login_url='login')
def takeguitarquizPage(request):
	return render(request, 'app/guitarQuiz.html')

@login_required(login_url='login')
def ginstructionsPage(request):
	return render(request, 'app/ginstructions.html')

@login_required(login_url='login')
def guitartopbandsPage(request):
	return render(request, 'app/guitartopbands.html')

@login_required(login_url='login')
def guitarmediumbandsPage(request):
	return render(request, 'app/guitarmediumbands.html')

@login_required(login_url='login')
def guitarlowbandsPage(request):
	return render(request, 'app/guitarlowbands.html')



@login_required(login_url='login')
def takeviolinquizPage(request):
	return render(request, 'app/violinQuiz.html')

@login_required(login_url='login')
def vinstructionsPage(request):
	return render(request, 'app/vinstructions.html')

@login_required(login_url='login')
def violintopbandsPage(request):
	return render(request, 'app/violintopbands.html')

@login_required(login_url='login')
def violinmediumbandsPage(request):
	return render(request, 'app/violinmediumbands.html')

@login_required(login_url='login')
def violinlowbandsPage(request):
	return render(request, 'app/violinlowbands.html')



@login_required(login_url='login')
def takepianoquizPage(request):
	return render(request, 'app/pianoQuiz.html')

@login_required(login_url='login')
def pinstructionsPage(request):
	return render(request, 'app/pinstructions.html')

@login_required(login_url='login')
def pianotopbandsPage(request):
	return render(request, 'app/pianotopbands.html')

@login_required(login_url='login')
def pianomediumbandsPage(request):
	return render(request, 'app/pianomediumbands.html')

@login_required(login_url='login')
def pianolowbandsPage(request):
	return render(request, 'app/pianolowbands.html')



@login_required(login_url='login')
def takeflutequizPage(request):
	return render(request, 'app/fluteQuiz.html')

@login_required(login_url='login')
def finstructionsPage(request):
	return render(request, 'app/finstructions.html')

@login_required(login_url='login')
def flutetopbandsPage(request):
	return render(request, 'app/flutetopbands.html')

@login_required(login_url='login')
def flutemediumbandsPage(request):
	return render(request, 'app/flutemediumbands.html')

@login_required(login_url='login')
def flutelowbandsPage(request):
	return render(request, 'app/flutelowbands.html')




@login_required(login_url='login')
def takedrumsquizPage(request):
	return render(request, 'app/drumsQuiz.html')

@login_required(login_url='login')
def dinstructionsPage(request):
	return render(request, 'app/dinstructions.html')

@login_required(login_url='login')
def drumstopbandsPage(request):
	return render(request, 'app/drumstopbands.html')

@login_required(login_url='login')
def drumsmediumbandsPage(request):
	return render(request, 'app/drumsmediumbands.html')

@login_required(login_url='login')
def drumslowbandsPage(request):
	return render(request, 'app/drumslowbands.html')



@login_required(login_url='login')
def taketrumpetquizPage(request):
	return render(request, 'app/trumpetQuiz.html')

@login_required(login_url='login')
def tinstructionsPage(request):
	return render(request, 'app/tinstructions.html')

@login_required(login_url='login')
def trumpettopbandsPage(request):
	return render(request, 'app/trumpettopbands.html')

@login_required(login_url='login')
def trumpetmediumbandsPage(request):
	return render(request, 'app/trumpetmediumbands.html')

@login_required(login_url='login')
def trumpetlowbandsPage(request):
	return render(request, 'app/trumpetlowbands.html')