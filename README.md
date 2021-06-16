# Study-Django

## 1일차

Django -> MVT 패턴을 사용

M : model

V : view

T : template

startapp -> 다른 프로젝트를 연결하여 하나의 프로젝트 안에서 다른 사이트로 연결

views -> 해당 프로젝트에서 화면을 연결

urls -> 해당 프로젝트에서 url을 연결 하고 view로 연결

## 2일차

{{ }} -> <%= %> -> 값을 출력

{% %} -> <% %> -> 소스 입력

python manage.py migrate

migrations을 만들어줌

python manage.py makemigrations dbtest

dbtest의 테이블을 만들어줌

python manage.py sqlmigrate dbtest 0001

dbtest shell을 연다

python manage.py shell

dbtest에 값을 넣는다

from dbtest.models import Myboard
from django.utils import timezone
test = Myboard(myname='admin',mytitle='test',mycontent='test0123',mydate=timezone.now())
test.save()
Myboard.objects.all()


csrf_token -> Cross Site Request Forgery
