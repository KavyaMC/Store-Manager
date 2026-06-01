#Part 1 — Price Analysis
prices = [105.0, 200.0, 150.0, 85.0]

def total_shopping(items):
	total=0
	if len(items) > 0:
		for price in items:
			total += price
		return total

def average_price(items):
	total=total_shopping(items)
	if len(items) > 0:
		return round(total/len(items),2)

def most_expensive(items):
	if len(items) > 0:
		highest_price = items[0]
		for price in items:
			if price > highest_price:
				highest_price = price
	return highest_price

def cheapest_item(items):
	if len(items) > 0:
		lowest_price = items[0]
		for price in items:
			if price < lowest_price:
				lowest_price = price
	return lowest_price

def get_expensive_items(items):
	average = average_price(items)
	expensive_list = []
	if len(items) > 0:
		for price in items:
			if price > average:
				expensive_list.append(price)
		return expensive_list

def count_in_range(items, low, high):
	count=0
	if len(items) > 0:
		for price in items:
			if low <= price <= high:
				count+=1
	return count

def apply_discount(price, items, discount_rate):
	if len(items) > 0:
		if price in get_expensive_items(items):
			return price*(1 -discount_rate)
		else:
			return price

def shopping_report(items):
	r = report = {}
	r["total price"]=total_shopping(items)
	r["average price"]=average_price(items)
	r["highest price"]=most_expensive(items)
	r["lowest price"]=cheapest_item(items)
	r["total expensive items"]=len(get_expensive_items(items))
	r["mid range items"]=count_in_range(items, 100, 180)

	discounted_total = 0
	for price in items:
		discounted_total += apply_discount(price, items, 0.2)
	r["discounted total price"]=round(discounted_total,2)
	return report