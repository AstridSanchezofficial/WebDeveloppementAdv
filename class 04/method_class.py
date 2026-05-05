#CREATE A CLASS THAT RECEIVES DATA IN DIFFERENT FORMATS
#CHALLENGE: CLEAN THE DATA

class Product:
#The data to create this class may arrive in 3 different formats:
#1. SEPARATE CONSTRUCTOR ARGUMENTS (_INIT_)   
    def __init__(self,name, price, category):
        self.name=name
        self.price=price
        self.category=category
#2. ONE COMMA-SEPARATES STRING
    @classmethod
    def from_string(cls, data):
        name, price, category=data.split(",")
        return cls(name, price, category)
    


#3. A DICTIONARY
    @classmethod
    def from_dictionary(cls, data):
        rawData=data
        name=rawData["name"]
        price=rawData["price"]
        category=rawData["category"]
        return cls(name, price, category)
        

#4. A NEW PRODUCT WITH NO CATEGORY AND PRICE (JUST A NAME )
    @classmethod
    def from_missingData(cls,data):
        name=data
        return cls(name, 0, "")
    def show(self):
        #print (f"${Product.name} cost ${Product.price} and belongs to ${Product.category}")  -> ES un MISTAKE por que aquie estoy diceiendo que la clase PRODUCT tiene un atraibuto
                                                                                               #->Pero la clase Product no tiene ningun atributo name o price (es el objeto que lo tiene)
                                                                                               #-> Asi que debemos poner self.name y self.price  
        print(f"{self.name} costs: ${self.price} and belongs to {self.category}")

product1=Product.from_string("Keyboard, 20.5, electronics") # el classmethod recibe dos arguments la class, y la data en forma de una sola string
product2=Product.from_dictionary({"name":"Mouse","price":7,"category":"electronics"})
product3=Product.from_missingData("Led")

#Display the data 
product1.show()
product2.show()
product3.show()