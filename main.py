# Part 9 — Putting It All Together
from modules.part1 import prices
from modules.part2 import categories
from modules.part3 import scanned
from modules.part5 import codes, full_store_report
from modules.part6 import inventory, update_inventory
from modules.part7 import get_valid_quantity, search_price
from modules.part8 import print_receipt, celebrate_customer

def store_menu():
	while True:
		choice = int(input("Enter 1 for Report, 2 for Checkout, 3 for Price Search, 4 to Exit: ").strip())
		if choice == 1:
			result = full_store_report(prices, categories, codes)
			print(result)
		elif choice == 2:
			success = update_inventory(inventory, scanned)
			if success:
				price_lookup = {"mango juice": 105.0, "roti": 85.0, "kurta": 200.0, "shampoo": 150.0}
				print_receipt(scanned, price_lookup, prices)
				points = get_valid_quantity()
				print(celebrate_customer("rahul", 5, 150, points))
			else:
				print("Stock insufficient. Checkout failed.")
		elif choice == 3:
			target = float(input("Enter target price: "))
			index = search_price(prices, target)
			if index >= 0:
				print(f"item found at position {index}")
			else:
				print("error: item not found")
		elif choice == 4:
			print("Goodbye! Thanks for visiting.")
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	store_menu()