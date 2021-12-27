"# Django_REST_API" 

1. python -m venv 가상환경 이름" # 가상환경 만들기
  "가상환경 이름\scripts\activate" # 가상환경 활성화
   pip install django djangorestframework" 
   django-admin startproject rest_api .
   python manage.py startapp example

   setting.py 고치기
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver

   python manage.py createsuperuser

2. 모델 만들기
3. 시리얼라이저 만들기 # 장고 모델 데이터를 JSON 형식(직렬화)으로 바꾸기 위해
4. 모델 만들고 난후 마이그레이션 