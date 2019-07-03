from flask import Flask, render_template, request, redirect, url_for
import joblib

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        
        sex = int(request.form['sex'])
        age = int(request.form['age'])
        if sex == 0:
            female = 1; male = 0
            if age < 15:
                child = 1; man = 0
                woman = 0; adultM = 0
            else:
                child = 0; man = 0
                woman = 1; adultM = 0
        else:
            female = 0; male = 1
            if age < 15:
                child = 1; man = 0
                woman = 0; adultM = 0
            else:
                child = 0; man = 1
                woman = 0; adultM = 1

        
        if sex == 0 and age >= 18:
            child = 0
            man = 0
            woman = 1
            adultM = 0
        if sex == 1 and age >= 18:
            child = 0
            man = 1
            adultM = 1
            woman = 0
        else:
            child = 1
            man = 0
            woman = 0
            adultM = 0

        pclass = int(request.form['class'])
        sibsp = int(request.form['sibsp'])
        parch = int(request.form['parch'])

        if sibsp == 0 and parch == 0:
            alone = 1
        else:
            alone = 0

        fare = int(request.form['fare'])

        fitur = [female, male, child, man, woman, pclass, age, sibsp, parch, fare, adultM, alone]
        print(fitur)
        prediksi = model.predict([fitur])[0]
        
        return redirect(url_for('show_prediction', prediksi = prediksi))
    else:        
        return render_template('home.html')

@app.route('/result/<int:prediksi>')
def show_prediction(prediksi):
    print(prediksi)
    if prediksi == 1:
        return render_template('selamat.html')
    else:
        return render_template('mati.html')

if __name__ == '__main__':
    model = joblib.load('model_titanic')
    app.run(debug = True)