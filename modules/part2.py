# Part 2 — Categories & Second Payoff
from part1 import shopping_report, prices
categories = ["food", "clothes", "food", "toiletries"]

def shopping_report_with_categories(items, categories):
	by_category = {
		"food": 0,
		"clothes": 0,
		"others": 0
	}
	for i in range(len(items)):
		price = items[i]
		category = categories[i]
		if category=="food":
			by_category["food"]+=price
		elif category=="clothes":
			by_category["clothes"]+=price
		else:
			by_category["others"]+=price
	return {
		"overall": shopping_report(items),
		"by_category": by_category
	}


def most_expensive_category(items, categories):
	r = shopping_report_with_categories(prices, categories)
	by_category = r["by_category"]
	highest_amount=0
	highest_cat=""
	for category, amount in by_category.items():
		if amount > highest_amount:
			highest_amount = amount
			highest_cat = category
	return f"{highest_cat}: {highest_amount}"

print(most_expensive_category(prices, categories))