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
