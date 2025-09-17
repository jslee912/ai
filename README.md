# [KDT] 기업맞춤형 AI-X 융복합 인재 양성 과정

1. Create repository
2. git-scm을 다운받고 install
3. Git Bash에서 git 환경 설정
   - git config --global user.name
   - git config --global user.email
   - git config --list (확인)
4. git 공간에 자료 올리기
   - git init (초기화)
   - git add . (공유 추가할 파일 더하기)
   - git status (상태 확인 – 선택)
   - git commit –m “first commit” (히스토리 버전 이름)
   - git branch –M main (branch 생성 – branch 생성을 하지 않을 경우 master로)
   - git remote add origin 본인깃주소 (연결고리)
   - git remote –v (확인 – 선택)
   - git push –u origin main (branch에 올리기 branch를 생성하지 않았다면 master)
5. 내 pc와 git이 동기화된 거 확인 후, 추가 파일 만든 후 추가 올리기
   - git add .
   - git commit –m “second”
   - git push –u origin main
6. 협업 (웹에서 수정하거나 다른 장소에서 수정 후 pull 필수)
   - git clone 주소 폴더이름 (다른 pc에 git 내용 그대로 받기)
   - git pull origin main (git 저장소와 내 PC간 동기화)
