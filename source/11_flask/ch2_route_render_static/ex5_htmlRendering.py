from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html") # templates/index.html => Jinja2템플릿

@app.route("/profile/<name>/<int:age>") # 동적 라우팅
def get_profile(name,age):
  return render_template("profile.html", 
                         name = name,
                         age = age)  # name, age => context 변수

if __name__=="__main__":
  app.run(debug=True)