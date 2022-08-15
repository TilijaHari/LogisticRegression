from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def SearchPage():
    return render_template('index.html')

@app.route('/classify', methods=['GET','POST'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            intercept = float(request.form['intercept'])
            occ_2 = float(request.form['occ_2'])
            occ_3 = float(request.form['occ_3'])
            occ_4 = float(request.form['occ_4'])
            occ_5 = float(request.form['occ_5'])
            occ_6 = float(request.form['occ_6'])
            occ_husb_2 = float(request.form['occ_husb_2'])
            occ_husb_3 = float(request.form['occ_husb_3'])
            occ_husb_4 = float(request.form['occ_husb_4'])
            occ_husb_5 = float(request.form['occ_husb_5'])
            occ_husb_6 = float(request.form['occ_husb_6'])
            rate_marriage = float(request.form['rate_marriage'])
            age = float(request.form['age'])
            yrs_married = float(request.form['yrs_married'])
            children = float(request.form['children'])
            religious = float(request.form['religious'])
            educ = float(request.form['educ'])

            filename = 'logistic_model.pickle'
            loaded_model = pickle.load(open(filename,'rb'))
            prediction = loaded_model.predict([[intercept,occ_2,occ_3,occ_4,occ_5,occ_6,occ_husb_2,occ_husb_3,occ_husb_4,occ_husb_5,occ_husb_6,rate_marriage,age,yrs_married,children,religious,educ]])

            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print("The Exception message is:",e)
            return "Something is wrong"
    else:
        return render_template('index.html')

if __name__ == "__main__":
    #app.run(host='0.0.0.0',port='8080')
    app.run(debug=True)