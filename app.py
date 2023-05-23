from flask import Flask, render_template
from misc.databaseCNX import DatabaseCnx
cnx_db = DatabaseCnx()
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/analyzer')
def hello():
    list_data = cnx_db.databaseAction("get",{})
    print(list_data[0])
    if(list_data[0] == 200):
        return render_template('analyzer.html', data=list_data[1])
    else:
        return "Error Cannot Get "
