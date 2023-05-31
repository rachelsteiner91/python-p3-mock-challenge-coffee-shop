
class Order:

    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

        coffee.orders(self)
        coffee.customers(customer)
        
        customer.orders(self)
        customer.coffees(coffee)
    
  ##Order property price 
  # #getter  
    @property
    def price(self):
        return self._price
    #setter
    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1 <= price <= 10:
            self._price=price
        else:
            raise Exception("price must be a number between 1 aand 10,inclusive")


###Object Relationship Methods and Properties##
## Order property customer
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("customer object must be type Customer")
        
#Order property coffee`
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("coffee object must be type Coffee")


