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
            "id": int(id),
            "name": name,
            "price": float(price),
            "image": image
        }
        products = self.readProducts()
        products.append(product)
        self.saveProducts(products)

    def saveLists(self, lists):
        print('save lists')
        with open("lists.json", "w") as json_file:
            json.dump(lists, json_file, indent=2)

    def readLists(self):
        print('read lists')
        with open("lists.json") as json_data_file:
            data = json.load(json_data_file)
            return data

    def addSingleList(self, listName, products):
        print('add single list')
        list = {
            "list_name": listName,
             "products": products
        }

        lists = self.readLists()
        lists.append(list)
        self.saveLists(lists)
