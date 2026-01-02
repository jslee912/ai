# (windows)  PowerShell 관리자 모드 : Get-ExecutionPolicy => Restricted
# PS C:\Windows\system32> Set-ExecutionPolicy RemoteSigned

# 실행 규칙 변경
# 실행 정책은 신뢰하지 않는 스크립트로부터 사용자를 보호합니다. 실행 정책을 변경하면 about_Execution_Policies 도움말
# 항목(https://go.microsoft.com/fwlink/?LinkID=135170)에 설명된 보안 위험에 노출될 수 있습니다. 실행 정책을
# 변경하시겠습니까?
# [Y] 예(Y)  [A] 모두 예(A)  [N] 아니요(N)  [L] 모두 아니요(L)  [S] 일시 중단(S)  [?] 도움말 (기본값은 "N"):Y  => 

# ------------------------------------------------------------------------------------------------

# app.py 생성 후 ctrl+j 터미널 창을 열기(.venv)
# 가상환경 만들기    :  python -m venv .venv : .venv 가상환경 만들기  => 확인창 뜨면 예
# 가상환경 들어가기 : .venv\Scripts\activate
# pip 업그레이드 :  python -m pip install --upgrade pip
# pip install flask

# pip freeze > requirements.txt
# pip install -r requirements.txt(내일)
# ctrl+shift+p -> 인터프리터 선택 -> .venv 가상환경 선택

from flask import Flask
app = Flask(__name__)  # 웹서버 객체(앱 인스턴스 생성)

@app.route("/")  # 데코레이터를 통해 가능한 url 등록
def main_hander():
  return "<H1>Hello, World</H1>"

@app.route("/apt")
def apt_handler():
  return "<h1>예상 금액은 1,000원입니다</h1>"
  # return{
  #   'price':'1000',
  #   'unut':'won'
  # }
# app.py에서 실행 : flask run --port=80 --debug
# app.py가 아닌 파일 플라스크 실행 : python ex1_app.py
if __name__=="__main__":
  app.run(port=80, debug=True)   # 소스 수정시 서버 자동 재시작, port=80번









