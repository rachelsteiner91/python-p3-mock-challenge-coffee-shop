class Customer:
    def __init__(self, name):
        self.name = name
        self._coffees = []
        self._orders = []
#### Customer
##Customer property name
    #getter
    @property
    def name(self):
        return self._name
    
    #setter
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <=15:
            self._name=name
        else:
            raise Exception("Names must be between 1 and 15 characters, inclusive")

### Customer
## Customer orders(new_order=None)
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
## Customer coffees(new_coffee=None) 
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        if isinstance(new_coffee, Coffee) and new_coffee not in self._coffees:
            self._coffees.append(new_coffee)
        return self._coffees
