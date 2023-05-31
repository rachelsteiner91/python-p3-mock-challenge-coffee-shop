class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []

#### Coffee
##Coffee property name
##getter for coffee name
    @property
    def name(self):
        return self._name
##setter for coffee name
##Should not be able to change after the coffee is created - _hint: `hasattr()`
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception("coffee name should not be able to change after the coffee is created")

#### Coffee
##Coffee orders(new_order=None)
#  - Adds new orders to coffee
#   - Returns a list of all orders for that coffee
#   - orders must be of type `Order`
#   - _Will be called from `Order.__init__`_     

    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders

##Coffee customers(new_customer=None)`
#  - Adds new customers to coffee
#   - Returns a **unique** list of all customers who have ordered a particular coffee.
#   - Customers must be of type `Customer`
#   - _Will be called from `Order.__init__`_
    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer) and new_customer not in self._customers:
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass