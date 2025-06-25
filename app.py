from flask import Flask, request, render_template
from predict import predict_url

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        result = predict_url(url)
        return render_template('index.html', prediction=result, url=url)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

