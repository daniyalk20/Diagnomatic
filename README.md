# Diagnomatic
Final Year Project

# Dependency 
1. Install Virtual Environment
	pip install virtualenv
2. Create Virtual Environment
	python -m venv environment
3. Activate the Environment
	/environment/Scripts/activate
4. Install Django
	pip install django
5. Install Django REST Framework (For Creting APIs)
	pip install django-rest-framework
6. Install Django Cors for creating TCP/IP Headers for API calls
	pip install django-cors-headers
7. Install Djoser for Authentication
	pip install djoser
8. Install Pillow (PIL) for Image Processing
	pip install pillow
9. Install Strip
	pip install stripe
10. Create a Django Project
	django-admin startproject diagnomatic_django
11. Configuring the Django Project
	a. Configuring settings.py
		INSTALLED_APPS = [
			...
			...
			'rest_framework',
			'rest_framework.authtoken',
			'corsheaders',
			'djoser',
		]
		
		CORS_ALLOWED_ORIGINS = [
			"http://localhost:8000", # Where the site is allowed to run
		]
		
		MIDDLEWARE = [
			'django.middleware.security.SecurityMiddleware',
			'django.contrib.sessions.middleware.SessionMiddleware',
			'corsheaders.middleware.CorsMiddleware',
			'django.middleware.common.CommonMiddleware',
			'django.middleware.csrf.CsrfViewMiddleware',
			'django.contrib.auth.middleware.AuthenticationMiddleware',
			'django.contrib.messages.middleware.MessageMiddleware',
			'django.middleware.clickjacking.XFrameOptionsMiddleware',
		]
	b. Configuring urls.py
		urlpatterns = [
			...
			path('api/v1', include('djoser.urls')),
			path('api/v1', include('djoser.urls.authtoken')),
		]
12. Migrate Database
	python manage.py migrate
	
13. Create Superuser
	python manage.py createsuperuser
	username: diagnomatic
	email: diagnomatic@daniyalk.com
	password: *123dani#
	
14. Setup Frontend (Vue.js)
	a. Install Node.js
	b. Install Vue Cli
		npm install -g @vue/cli
	c. Create Vue Project
		vue create diagnomatic_vue
		=> Configuration Manually
			i) Babel, Router, Vuex, CSS-Preprocessor
			ii) 3.x (Preview)
			iii) History mode for router -> Yes
			iv) CSS-Preprocessor -> Sass/SCSS (with dart-sass)
			v) deidicated config Files