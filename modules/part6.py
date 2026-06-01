# Part 6 — Inventory & The "break" Keyword
from .part4 import scanned, count_cart_items
inventory = {"mango juice": 5, "kurta": 2, "roti": 10, "shampoo": 3}
matrix = [[100.0, 5], [200.0, 2], [50.0, 10]]

def inventory_value(matrix):
	grand_total=0
	for item in matrix:
		price = item[0]
		quantity = item[1]
		total = price * quantity
		grand_total+=total
	return grand_total

def enforce_budget(matrix, budget):
	total=0
	for row in matrix:
		total_value=inventory_value([row])
		total+=total_value
		if total > budget:
			total-=total_value
			print("Budget Exceeded!")
			break
	return total

def update_inventory(inventory, scanned_items):
	receipt = count_cart_items(scanned_items)
	for item, quantity in receipt.items():
		if item not in inventory or inventory[item] < quantity:
			return False
	for item, quantity in receipt.items():
		inventory[item] -= quantity
	return True