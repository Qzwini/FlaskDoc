# import Flask
from flask import Flask,render_template,request

#  create flask opject
app = Flask('__name__')

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
    sum = int(x)+int(y)
    return render_template('sum.html',x=x,y=y,sum=sum)

@app.route('/help')
def fav():
    return render_template('help.html', lol='FuckU')



# run App
if __name__ == "__main__":
    app.run(debug=True)



'''
http message code
200 -> K
404 -> Not Found
500 -> server error
'''