from flask import Flask, render_template, request, redirect

app=Flask(__name__)


@app.route("/")
def add():
    return render_template('add.html')

# @app.errorhandler('/404')
# def invalid():
#     return render_template('add.html')

@add.route('/addexpense', method=['POST'])
def addexpense():
    date = request.form['date']
    name = request.form['enxpensename']
    amount = request.form['amount']
    category = request.form['catagory']
    print(date + " " + name + ' ' + amount + ' '  + category)
    return redirect("/")


if __name__=='__main__':
    app.run(debug=True)
