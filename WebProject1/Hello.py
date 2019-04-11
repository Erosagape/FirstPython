from flask import Flask,redirect,url_for,request,render_template,make_response
app = Flask(__name__)

@app.route('/')
def index():
    user = request.cookies.get('userID')
    if user==None:
        return render_template('login.html')
    else:
        return render_template('index.html',name=user)

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Welcome Guest <b>"%s"</b>!' % guest

@app.route('/admin')
def hello_admin():
    return 'Hello <b>Admin</b>!,How are you today?'

@app.route('/user/<name>')
def hello_user(name):
    return setCookie(name)

@app.route('/success/<name>')
def success(name):
    if name=='admin':
        return hello_admin()
    else:
        return hello_user(name)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method=='POST':
        user =request.form['username']
        password =request.form['password']
        if password=='1234':
            return success(user)
        else:
            return hello_guest(user)
    else:
        user=request.args.get('username')
        return success(user)

@app.route('/checkgrade/<int:grade>')
def check_grade(grade):
    grade_result=''
    if grade>100:
        grade_result='A+'
    elif grade>90:
        grade_result='A'
    elif grade>80:
        grade_result='B'
    elif grade>70:
        grade_result='C+'
    elif grade>60:
        grade_result='C'
    elif grade>50:
        grade_result='D'
    else:
        grade_result='F'

    return 'Your Score is %i ,Your Grade is %s' % (grade,grade_result)

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

@app.route('/index/<id>')
def setCookie(id):
    resp=make_response(render_template('index.html',name=id))
    resp.set_cookie('userID',id)
    return resp

if __name__=='__main__':
    app.run(debug=True)
