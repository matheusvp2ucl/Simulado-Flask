from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    url = "http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline"
    response = requests.get(url)
    data = []
    for item, index in zip(response.json(), range(len(response.json()))):
        data.append({
            "id": index+1,
            "imagem": item['image_link'],
            "marca": item['brand'],
            "nome": item['name'],
            "preco": item['price'],
            "link": item['product_link']
        })
    total = len(data)
    return render_template('index.html', produtos=data, total=total)


if __name__ == '__main__':
    app.run()
