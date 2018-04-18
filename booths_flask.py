from flask import Flask, render_template, request
from booths import *
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("index.html")

@app.route('/eval', methods=['POST'])
def eval():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    print("Num1", num1)
    print("Num2", num2)
    P_dec, P_bin = booths(num1, num2)
    response = "The product is: <br> Binary: "+str(P_bin)+"<br> Decimal: "+str(P_dec)
    return response

if __name__ == "__main__":
    app.run(host = 'localhost',debug=True, port=5002 )
