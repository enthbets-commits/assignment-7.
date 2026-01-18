products = [
    {"name": "Eco Water Bottle", "tags": ["eco-friendly", "durable", "recyclable"]},
    {"name": "Trail Backpack", "tags": ["durable", "water-resistant", "lightweight"]},
    {"name": "Vegan Leather Wallet", "tags": ["vegan", "stylish", "compact"]},
    {"name": "Bamboo Toothbrush", "tags": ["eco-friendly", "vegan", "biodegradable"]},
    {"name": "Smartwatch", "tags": ["tech", "durable", "stylish"]},
    {"name": "Solar Charger", "tags": ["eco-friendly", "tech", "portable"]},
]

customer_preferences = []
while True:
    pref = input("Input a preference: ").strip()
    if pref != "":
        customer_preferences.append(pref)
    cont = input("Do you want to add another preference? (Y/N): ").strip().upper()
    if cont == "N":
        break

customer_preferences_set = set(customer_preferences)

for product in products:
    product["tag_set"] = set(product["tags"])

def count_matches(product_tags, preferences):
    return len(product_tags.intersection(preferences))

def recommend_products(products, preferences):
    recommendations = []
    for product in products:
        matches = count_matches(product["tag_set"], preferences)
        if matches > 0:
            recommendations.append({"name": product["name"], "matches": matches})

    recommendations.sort(key=lambda x: x["matches"], reverse=True)
    return recommendations

recommended = recommend_products(products, customer_preferences_set)

print("\nRecommended Products:")
for r in recommended:
    print(f"- {r['name']} ({r['matches']} match(es))")

# Design Memo:
#
# Core operations used:
# - Loops: Loops were used to gather customer preferences from user input
#   and to check each product in the catalog for matching tags.
# - Sets and intersections: Customer preferences and product tags were
#   converted into sets. This allowed us to quickly find matches using set
#   intersections, while automatically removing duplicate preferences or tags.
# - Sorting: After counting matches, the recommended products were sorted
#   from most matches to least, so the most relevant products appear first.
#
# Scalability and considerations:
# - For a small product catalog, this method is fast and simple. The program
#   processes each product one time, which is efficient for small to medium
#   e-commerce platforms.
# - If the catalog grows to thousands of items, performance could slow down.
#   A possible improvement would be using an inverted index to map tags to
#   products, which would make finding relevant products faster.
# - Additional improvements could include assigning weights to certain tags
#   or using more advanced scoring to rank products based on preference
#   importance.
#
# Overall, this prototype shows key programming skills needed for real-world
# recommendation systems. It demonstrates how to collect and clean data,
# select efficient data structures, and produce ranked results. The code
# is clear, easy to maintain, and considers how it could scale to larger
# catalogs in the future.

