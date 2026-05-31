# Part 4 — Cart Processing
from part3 import scanned, required, forgotten_items
barcode_dict = {"mango juice":1015, "roti":2002, "kurta":1009, "shampoo":3008}

def count_cart_items(scanned_items, required_items=None):
	receipt = {}
	for item in scanned_items:
		if item in receipt.keys():
			receipt[item] += 1
		else:
			receipt[item] = 1
	if required_items:
		forgot = forgotten_items(list(receipt.keys()), required_items)
		return receipt, forgot
	return receipt

def sort_barcodes(barcode_dict, scanned_items):
	receipt = count_cart_items(scanned_items)
	left_aisle = []
	right_aisle = []
	total_scanned = 0
	for key in receipt.keys():
		if key in barcode_dict:
			bar_code = barcode_dict[key]
			if bar_code%2 == 0:
				left_aisle.append(bar_code)
			else:
				right_aisle.append(bar_code)
	left_aisle.sort()
	right_aisle.sort()
	for value in receipt.values():
		total_scanned += value
	return [left_aisle, right_aisle, total_scanned]