def get_discount(user):
    if user["is_premium"]:
        return 0.2
    return 0.0

def final_price(price, user):
    discount = get_discount(user)
    return price * (1 - discount)