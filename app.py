from flask import Flask,render_template,request
import pickle


file1 = open('fotieefinal.pkl','rb')
lr1 = pickle.load(file1)
file1.close()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    if request.method == 'POST':
        my_dict = request.form
        meanrad = float(my_dict['meanrad'])
        meanrad1 = float(my_dict['meanrad1'])
        meanper = float(my_dict['meanper'])
        meanarea = float(my_dict['meanarea'])
        meancon = float(my_dict['meancon'])
        concavemean= float(my_dict['concavemean'])
        concavepoints = float(my_dict['concavepoints'])
        radworst= float(my_dict['radworst'])
        perworst= float(my_dict['perworst'])
        concaveworst= float(my_dict['concaveworst'])
        concaveworst1= float(my_dict['concaveworst1'])
        concaveworst2= float(my_dict['concaveworst2'])
        concaveworst3= float(my_dict['concaveworst3'])
        input_features = [meanrad,meanrad1,meanper,meanarea,meancon,concavemean,concavepoints,radworst,perworst,concaveworst,concaveworst1,concaveworst2,concaveworst3]
        inf = lr1.predict([input_features])
        inf*=2.5
        return render_template('showresult.html',inf = inf)
    return render_template('predict.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')

if __name__ == "__main__":
    app.run(debug = True)