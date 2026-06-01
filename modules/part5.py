# Part 5 — Promos, The "continue" Keyword & Second Report
from .part1 import prices, total_shopping
from .part2 import categories, most_expensive_category, shopping_report
codes = ["racecar", "wow", "python", "level", "discount", "madam"]

def valid_promo_codes(codes):
	working_codes=[]
	for code in codes:
		if len(code) < 4:
			continue
		if len(code) > 4 and code == code[::-1]:
			working_codes.append(code)
	return working_codes

def apply_best_promo(items, promo_codes):
	result=valid_promo_codes(codes)
	total = total_shopping(items)
	if result:
		return round(total*0.9,2)
	else:
		return total

def full_store_report(items, categories, codes):
	return {
	"top_category": most_expensive_category(items, categories),
	"promo_total": apply_best_promo(items, codes),
	"overall": shopping_report(items)
}
r = full_store_report(prices, categories, codes)