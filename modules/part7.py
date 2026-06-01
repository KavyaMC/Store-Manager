# Part 7 — While Loops & Search
from .part1 import prices

def search_price(items, target):
	i=0
	while i < len(items):
		if items[i] == target:
			return i
		i+=1
	return -1

def get_valid_quantity():
	while True:
		quantity = input("Enter a valid quantity: ").strip()
		if quantity.isdigit():
			int(quantity)
			print("Quantity accepted")
			return quantity
		print("Invalid input! Please try again.")