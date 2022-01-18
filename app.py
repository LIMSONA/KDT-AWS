from flask import Flask

app = Flask(__name__)

@app.route('/')
def hell():
    return "<h1> hello!! hi!!  Flask <h1>"

@app.route('/test')
def test():
    # 수행 해야할 로직이 이 자리에 들어온다.
    return "test 페이지 입니다."

@app.route('/exam')
def tomarrow():
    # 수행 해야할 로직이 이 자리에 들어온다.
    return "내일은 AWS 시험입니다........ㅠㅠㅠㅠ"

if __name__ == '__main__':
    app.run("0.0.0.0", port =8080)
