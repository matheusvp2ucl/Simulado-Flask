from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"
    response = requests.get(url)
    data = []
    for item in response.json():
        data.append({
            "imagem" : item['image_link'],
            "marca" : item['brand'],
            "nome" : item['name'],
            "preco" : item['price'] + " " + item['price_sign'] + " " + item['currency'],
            "link" : item['product_link']
        })
    total = len(data)
    return render_template('index.html', data=data, total=total)


if __name__ == '__main__':
    app.run()
