from django.urls import path
from . import views

urlpatterns = [
	path('', views.homePage),
	path('register', views.registerPage, name="register"),
	path('login', views.loginPage, name="login"),
	path('instruments', views.instrumentsPage, name="instruments"),

	path('ginstructions', views.ginstructionsPage, name="ginstructions"),
	path('guitarQuiz', views.takeguitarquizPage, name="guitarQuiz"),
	path('guitartopbands', views.guitartopbandsPage, name="guitartopbands"),
	path('guitarmediumbands', views.guitarmediumbandsPage, name="guitarmediumbands"),
	path('guitarlowbands', views.guitarlowbandsPage, name="guitarlowbands"),

	path('vinstructions', views.vinstructionsPage, name="vinstructions"),
	path('violinQuiz', views.takeviolinquizPage, name="violinQuiz"),
	path('violintopbands', views.violintopbandsPage, name="violintopbands"),
	path('violinmediumbands', views.violinmediumbandsPage, name="violinmediumbands"),
	path('violinlowbands', views.violinlowbandsPage, name="violinlowbands"),

	path('pinstructions', views.pinstructionsPage, name="pinstructions"),
	path('pianoQuiz', views.takepianoquizPage, name="pianoQuiz"),
	path('pianotopbands', views.pianotopbandsPage, name="pianotopbands"),
	path('pianomediumbands', views.pianomediumbandsPage, name="pianomediumbands"),
	path('pianolowbands', views.pianolowbandsPage, name="pianolowbands"),

	path('dinstructions', views.dinstructionsPage, name="dinstructions"),
	path('drumsQuiz', views.takedrumsquizPage, name="drumsQuiz"),
	path('drumstopbands', views.drumstopbandsPage, name="drumstopbands"),
	path('drumsmediumbands', views.drumsmediumbandsPage, name="drumsmediumbands"),
	path('drumslowbands', views.drumslowbandsPage, name="drumslowbands"),

	path('finstructions', views.finstructionsPage, name="finstructions"),
	path('fluteQuiz', views.takeflutequizPage, name="fluteQuiz"),
	path('flutetopbands', views.flutetopbandsPage, name="flutetopbands"),
	path('flutemediumbands', views.flutemediumbandsPage, name="flutemediumbands"),
	path('flutelowbands', views.flutelowbandsPage, name="flutelowbands"),

	path('tinstructions', views.tinstructionsPage, name="tinstructions"),
	path('trumpetQuiz', views.taketrumpetquizPage, name="trumpetQuiz"),
	path('trumpettopbands', views.trumpettopbandsPage, name="trumpettopbands"),
	path('trumpetmediumbands', views.trumpetmediumbandsPage, name="trumpetmediumbands"),
	path('trumpetlowbands', views.trumpetlowbandsPage, name="trumpetlowbands"),


	path('logout', views.logoutUser, name="logout"),
]