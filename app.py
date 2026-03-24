def get_discount(user):
    if user.get("is_premium"):
        return 0.2
    if user.get("coupon") == "VIP":
        return 0.5
    return None

def final_price(price, user):
    discount = get_discount(user) or 0
    return price * (1 - discount)

def log_user(user):
    print("USER DATA:", user)