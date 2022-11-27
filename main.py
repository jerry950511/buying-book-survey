from flask import Flask, render_template, request, redirect, url_for, flash , jsonify
import eportal
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/order')
def order():
    return render_template('order.html')

@app.route('/login')
def login():
    return "幹部登入查詢目前狀況"

@app.route("/eportal", methods=['POST'])
def eportal_login():
    account = request.form.get('account')
    password = request.form.get('password')
    if eportal.check_eportal(account,password):
        return jsonify({"message":"登入成功"})
    else:
        return jsonify({"message":"帳號或密碼錯誤"})
@app.route("/get_info", methods=['GET'])
def get_info():
    account = request.args.get('account')
    password = request.args.get('password')
    info = eportal.get_info(account,password)
    return jsonify({"data":info})
if __name__ == '__main__':
    app.run(debug=True)
