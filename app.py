# import Flask
from flask import Flask, render_template, request 

#  create flask opject
app = Flask('__name__')

# create web page
@app.route('/')
#  define a function from web page
def index():
    link = '/calculator /help /hi /sum /index /words /testMaster1'.split()
    contactMail = 'qzwini@gmail.com'
    return render_template('index.html',contact=contactMail ,link=link)
    


# # block
# app.route('/master')
# def block():
#     page = '/calculator /help /hi /sum /index /words /testMaster1'.split()
#     return render_template('master.html', page=page)



@app.route('/sum')
def sum():
    x=request.args.get('x')
    y=request.args.get('y')
    sum = int(x)+int(y)
    return render_template('sum.html',x=x,y=y,sum=sum)

@app.route('/help')
def fav():
    return render_template('help.html', lol='FuckU')

@app.route('/hi/<name>')
def hi (name):
    return render_template('hi.html',name=name)



@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    l = 'this is my calculator'.split()
    result = None  # when the method is GET
    if request.method == 'POST':
        if not request.form['num1'] and not request.form['num2'] \
                and not request.form['op']:
            result = 'please fil the form'
            # print(result)
        else:
            try:
                n1 = request.form['num1']
                n2 = request.form['num2']
                op = request.form['op']
                # print(n1, op, n2)
                result = eval('{}{}{}'.format(n1, op, n2))
                # print(result)
            except BaseException as error:
                result = 'error: {}'.format(error)
                # print(result)
    return render_template('calculator.html', result=result, l=l)



@app.route('/words', methods=['GET', 'POST'])
def word ():
    result = None
    op = 'most frequent'
    if request.method=='POST':
        text = request.form['mytext']
        if not text:
            result = 'please fil the form'
        else:
            counts={}
            for word in text.split():
                counts[word]= counts.get(word, 0) +1
            result = sorted([(v, k) for k, v in counts.items()], reverse=True)[0]
    return render_template('words.html', op=op, result=result)



     
@app.route('/testMaster1')
def test():
    return render_template('testMaster1.html')





# run App
if __name__ == "__main__":
    app.run(debug=True)



'''
http message code
200 -> K
404 -> Not Found
500 -> server error
'''