from flask import Flask, render_template

app=Flask(__name__)


@app.route("/add")
def add():
    return render_template('add.html')

@app.errorhandler(404)
def invalid():
    return render_template('add.html')


if __name__=='__main__':
    app.run(debug=True)
