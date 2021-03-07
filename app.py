from flask import Flask , render_template, request,url_for, redirect ,Response
import os

import numpy as np
import pickle
import sklearn

app = Flask(__name__)

model = pickle.load(open('model.pickle', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/after', methods=['GET','POST'])
def form():
    r = int(request.form.get("r"))
    f = int(request.form.get("f"))
    m = int(request.form.get("m"))
    t = int(request.form.get("t"))
    a = [r,f,t,m]
    final = [np.array(a)]
    
    predictions = model.predict(final)

    output = predictions[0]

    if output == 0:
        s = "The person will not donate soon"
    else:
        s = "The person will donate soon"

    return render_template('after.html',data= [r,f,m,t,output,s])

if __name__ == '__main__':
    app.run(debug=True)