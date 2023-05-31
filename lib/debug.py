#!/usr/bin/env python3
import ipdb

from classes.customer import Customer
from classes.order import Order
from classes.coffee import Coffee

if __name__ == '__main__':
    print("HELLO! :) let's debug")

c1=Customer("Rachel")
co1=Coffee("stormio")
o1=Order(c1, co1, 7)


ipdb.set_trace()
