from flask import Flask
Exp5 = Flask(__name__)
@Exp5.route('/')
def hello():
    return "Hello from Jenkins!!!"
if __name__ == '__main__':
    Exp5.run(debug=True) 
