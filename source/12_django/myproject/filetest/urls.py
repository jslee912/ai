# file/           DB에 저장없이 파일 첨부 받기
# file/predict/   예측결과 출력하기
from django.urls import path
from . import views # 함수 기반
app_name = "file"
urlpatterns = [
    path("", views.upload_file, name="upload_file"),
    path("predict/", views.predict, name="predict"),
    
    # 회원가입, 로그인, 로그아웃
]    