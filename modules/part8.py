# Part 8 — Receipt & Celebration
from .part1 import prices, apply_discount
from .part4 import scanned, count_cart_items
price_lookup = {"mango juice":105.0, "roti":85.0, "kurta":200.0, "shampoo":150.0}
import random

def mystery_discount(price, items):
	discount_percentage = random.randint(5, 25)
	discount_rate = round(discount_percentage/100,2)
	return apply_discount(price, items, discount_rate)

def print_receipt(scanned_items, price_lookup, items_list):
	receipt = count_cart_items(scanned_items)
	for item, quantity in receipt.items():
		base_price = price_lookup[item]
		final_price = mystery_discount(base_price, items_list)
		total = final_price * quantity
		print(f"{quantity}x {item} @ ₹{final_price:.1f} (total: ₹{total:.1f})")

def update_loyalty_points(current_points, points_earned):
		return int(current_points) + int(points_earned)

def celebrate_customer(name, years_loyal, current_points, points_earned):
	updated_points = update_loyalty_points(current_points, points_earned)
	stars = "*" * years_loyal
	year = "year" if years_loyal == 1 else "years"
	return f"{stars} Thank you for {years_loyal} {year}, {name.capitalize()}! Total points: {updated_points}."