from flask import Flask, request
import part7.exercise_decorators
#from replit import db


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

def calculate(calc_function, n1, n2):
  return calc_function(n1, n2)

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello from Flask!'


if __name__ == "__main__":
  import socket

  hostname=socket.gethostname()   
  IPAddr=socket.gethostbyname(hostname)   
  print("Your Computer Name is:"+hostname)   
  print("Your Computer IP Address is:"+IPAddr) 
  print(calculate(add, 2, 3))
  part7.exercise_decorators.fast_function()
  part7.exercise_decorators.slow_function()
  
  
  app.run(host='0.0.0.0', port=81)
