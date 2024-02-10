# Creating a virtual environment & importing all modules

from flask import Flask, render_template, request
import requests

app= Flask(__name__)


# making application route/hosting port etc. | we render html pages here
@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        base_curr= request.form.get('base_curr')
        target_curr= request.form.get('target_curr')
        quantity= request.form.get('quantity')

        base_url= 'https://v6.exchangerate-api.com/v6/0b1c29787bef9799b65c9243/pair/'
        url= base_url +base_curr +"/"+ target_curr

        response= requests.get(url)

        if (response.ok is False):     
            print("\nError {}:".format(response.status_code))
            print(response.json()['error'])

        else:
            result_dict = response.json()
            rate= result_dict['conversion_rate']

        result = float(quantity) * rate
        
        return render_template('home.html', result=result)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug= True)
