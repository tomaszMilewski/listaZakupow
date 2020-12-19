import json


class JsonReader:
    def readProducts(self):
        with open("products.json") as json_data_file:
            data = json.load(json_data_file)
            return data

    def saveProducts(self, products):
        with open('products.json', 'w') as json_file:
            json.dump(products, json_file)

    def addSingleProduct(self, id, name, price, image):
        product = {
            "id": id,
            "name": name,
            "price": price,
            "image": image
        }
        products = self.readProducts()
        products.append(product)
        print(products)
        self.saveProducts(products)
