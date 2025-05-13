class Product:

    def __init__(self, name, price, quantity):
        self.name = name 
        self.price = price
        self.quantity = quantity 
class Inventory:

    def __init__(self):
        self.products = []      

    def add_product(self, product):
        self.products.append(product)    

    def display_inventory(self):
        print ("Inventory:  ")    
        for idx, product in enumerate(self.products,start=1):
            print (f"{idx}. {product.name} - price: ${product.price}, Quantity: {product.quantity} ")

    def find_product_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None 

    def sell_product(self , name , quantity):
        product = self.find_product_by_name(name)
        if product:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"{quantity} units of {name} sold")
            else:
                print ("insufficient quantity of {name} available. ") 
        else:
            print (f"{name} not found in inventory")   

# now creating our main function 

def main():
        inventory = Inventory()  
        
        while True:
            print ("\n1. Display Inventory")     
            print ("2. Add Product")
            print ("3. Sell Product")
            print ("4. Exit ")      

            choice = input ("Enter your choice: ")    

            if choice == "1":
                inventory.display_inventory()

            elif choice == "2":
                product_name = input ("Enter product name: ")
                product_price = float(input("Enter product price: "))
                product_quantity = int(input("Enter product quantity: "))
                new_product = Product(product_name, product_price, product_quantity) 
                inventory.add_product(new_product)   
                print(f"{product_name} added to inventory.")
            
            elif choice == "3":
                product_name =input ("Enter product name: ")
                quantity = int(input("Enter quantity to sell: "))
                inventory.sell_product(product_name, quantity)

            elif choice == 4:
                print ("Exciting")
                break
            else:
                print ("Invalid choice. Please try again.") 

if __name__ == "__main__": 
    main()
