#
# Decorator enhanced strategy pattern
#

# Most decorators do change the decorated function. They usuallly do it by defining an inner function and returning it to
# replace the decorated function.
# Code that uses inner functions almost always depends on closures to operate correctly.
# 

promos = []

def promotion(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion
def fidelity(order):
    """%5 discount for customers with 1000 or more fidelity points
    """

    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

@promotion
def bulk_item(order):
    """%10 discount for each LineItem with 20 or more units
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

@promotion
def large_order(order):
    """%7 discount for orders with 10 or more distinct items.
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

def best_promo(order):
    """Select best discount available
    """
    return max(promo(order) for promo in promos)
