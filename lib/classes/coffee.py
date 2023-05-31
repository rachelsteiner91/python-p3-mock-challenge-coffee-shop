class Coffee:
    def __init__(self, name):
        self.name = name
        self._orders=[]
        self._customers=[]
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
         if isinstance(name, str) and len(name) > 0 and not hasattr(self, 'name'):
             self._name=name
         else:
            raise Exception("Name cannot be changed after coffee has been created")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return self._orders
    #remember to call it  in the Order init method class as coffee.orders(self)

    def customers(self, new_customer=None):
        from classes.customer import Customer
        if isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return self._customers
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass