# import Flask
from flask import Flask,render_template,request

#  create flask opject
app = Flask('MyFirstApp')

# create web page
@app.route('/')
#  define a function from web page
def index():
    contactMail = 'qzwini@gmail.com'
    return render_template('index.html',contact=contactMail)



@app.route('/sum')
def sum():
    x=request.args.get('x')
    y=request.args.get('y')
    return '{} + {} = {}'.format(x,y,int(x)+int(y))


# run App
if __name__ == "__main__":
    app.run(debug=True)

'''
http message code
200 -> K
404 -> Not Found
500 -> server error
'''