# DIAGNOMATIC: DISEASE DETECTION AND VISUALIZATION USING MEDICAL IMAGING AND DEEP LEARNING
## Abstract
Pneumonia is particularly a difficult disease to be diagnosed because it could be
caused by any number of pathogens that lead to a bacterial, fungal or viral infection
in the lungs and it can be contracted almost anywhere, including in hospitals. Chest
X-rays have been considered the best tool to detect any form of pneumonia, but it's
not perfect. Pneumonia can appear similar to other conditions on scan, and imaging
cannot identify the infectious pathogens, making the diagnosis difficult via x-ray.
Physicians must gather a complete picture of the patient's condition to make their
best and most accurate diagnosis.
The work portrayed targets automating entire procedure of diagnosing the
Pneumonia and visualizing it using a web-app with a high accuracy of 92% which
could make it easier for medical practitioners and patients to understand the area
diseased in the given X-ray. The model uses X-ray images to predict the actual
diseased location by the use of widely used Deep Learning Algorithms such as CNN
(Convolutional Neural Network) and Data Augmentation.
The deep learning model is trained using 5,863 JPEG images extracted from
retrospective cohorts of pediatric patients of one to five years old from X-Ray
imaging was performed as part of patients' routine clinical care.
The model is trained using the Kaggle’s cloud kernel and then saved in H5 and json
format which is later used by the Django framework to generate output is the newly
inputted images into the web-app by end user via frontend that is implemented using
the vue.js framework.
This project uses python 3.x libraries TensorFlow and Keras to implement Data
Augmentation and CNN Algorithms. To perform other visualization, mathematical
and, statistical operations it used NumPy, Pandas, Seaborn, Scikit Learn and
OpenCV libraries. Other than these it uses Django and Vue.js to implement Backend
and frontend of the web-app respectively.

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
