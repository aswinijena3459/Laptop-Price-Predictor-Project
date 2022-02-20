from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import sklearn

app=Flask(__name__)## object of flask class


@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/predict', methods=['POST','GET'])
def result():
    Company = str(request.form['Company'])
    TypeName = str(request.form['TypeName'])
    Ram = float(request.form['Ram'])
    Weight = float(request.form['Weight'])
    TouchScreen = str(request.form['TouchScreen'])
    IPS = str(request.form['IPS'])
    Screen_Size = float(request.form['Screen Size'])
    Resolution = str(request.form['Screen Resolution'])
    Cpu_name = str(request.form['Cpu_name'])
    HDD = float(request.form['HDD'])
    SSD = float(request.form['SSD'])
    Gpu = str(request.form['Gpu'])
    os = str(request.form['os'])
    if TouchScreen == 'Yes':
        TouchScreen = 1
    else:
        TouchScreen = 0

    if IPS == 'Yes':
        IPS = 1
    else:
        IPS = 0

    X_res = int(Resolution.split('x')[0])
    Y_res = int(Resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / Screen_Size


    X= np.array([[Company,TypeName,Ram,Weight,TouchScreen,IPS,ppi,Cpu_name,HDD,SSD,Gpu,os]])
    model = pickle.load(open('pipe.pkl', 'rb'))
    y_predict=model.predict(X)

    output = round(y_predict[0], 2)

    return render_template('index.html', prediction_text="This laptop will cost approximately {}".format(output))

if __name__=='__main__':
    app.run(debug=True)


