from flask import *  
app = Flask(__name__)  
  
@app.route('/',methods = ['POST'])  
def login():  
      uname=request.form['uname']  
      passwrd=request.form['pass']  
      if uname=="ayush" and passwrd=="google":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)       
 
app.run(host="0.0.0.0",port=4050, debug=True)
