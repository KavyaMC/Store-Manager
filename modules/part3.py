# Part 3 — Sets — Cleaning, Comparing, Finding Gaps
scanned = ["mango juice", "roti", "mango juice", "roti", "mango juice"]
required = {"Mango Juice", "roti", " Paneer ", "MILK"}

def shared_shopping(list_a, list_b):
	set_a=set(list_a)
	set_b=set(list_b)
	return {
		"mutual_items": set_a&set_b,
		"only_a_wants": set_a-set_b
	}

def clean_product_names(raw_a, raw_b):
	clean_a=set()
	clean_b=set()
	for name in raw_a:
		clean_a.add(name.strip().lower())
	for name in raw_b:
		clean_b.add(name.strip().lower())
	return shared_shopping(list(clean_a), list(clean_b))

def forgotten_items(cart, required_items):
	result = clean_product_names(required_items, cart)
	return result["only_a_wants"]

print(forgotten_items(
    ["mango juice", "roti"],
    {"Mango Juice", " roti ", "PANEER", "milk"}
))