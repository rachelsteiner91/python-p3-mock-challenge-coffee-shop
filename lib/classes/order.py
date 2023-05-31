
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

####Order
##Order property price
##getter
    @property
    def price(self):
        return self._price
##setter  
##Returns the price for a coffee
##Price must be a number between 1 and 10, inclusive
    @price.setter
    def price(self, price):
        if isinstance(price, int) and 1<= price <= 10:
            self._price = price
        else:
            raise Exception("Price must be an integer")

####Order property customer
##getter
    @property
    def customer(self):
        return self._customer

##setter
##Returns the customer object for that order
##Must be of type `Customer`
    @customer.setter
    def customer(self, customer):
        from classes.customer import Customer
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("customer must be of a type Customer")
        

##Order property coffee
##getter
    @property
    def coffee(self):
        return self._coffee
##setter
##Returns the coffee object for that order
##Must be of type `Coffee`
    @coffee.setter
    def coffee(self, coffee):
        from classes.coffee import Coffee
        if isinstance(coffee, Coffee):
            self._coffee = coffee
        else:
            raise Exception("coffee must be of a type Coffee")



##Order property coffee

