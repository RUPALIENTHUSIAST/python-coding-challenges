def farmer_revenue():
    acres = 80
    segment = acres / 5  # Each crop gets 16 acres

    # ---- Tomato ----
    tomato_acres = segment
    tomato_yield_30 = 0.30 * tomato_acres * 10 * 1000   # 10 tonnes → 10,000 kg
    tomato_yield_70 = 0.70 * tomato_acres * 12 * 1000   # 12 tonnes → 12,000 kg
    tomato_total_yield = tomato_yield_30 + tomato_yield_70
    tomato_revenue = tomato_total_yield * 7

    # ---- Potato ----
    potato_acres = segment
    potato_yield = potato_acres * 10 * 1000   # 10 tonnes → 10,000 kg
    potato_revenue = potato_yield * 20

    # ---- Cabbage ----
    cabbage_acres = segment
    cabbage_yield = cabbage_acres * 14 * 1000
    cabbage_revenue = cabbage_yield * 24

    # ---- Sunflower ----
    sunflower_acres = segment
    sunflower_yield = sunflower_acres * 0.7 * 1000   # 0.7 tonnes → 700 kg
    sunflower_revenue = sunflower_yield * 200

    # ---- Sugarcane ----
    sugarcane_acres = segment
    sugarcane_yield = sugarcane_acres * 45   # tonne
    sugarcane_revenue = sugarcane_yield * 4000

    # ---- Final calculations ----
    overall_sales = (
        tomato_revenue + potato_revenue + cabbage_revenue +
        sunflower_revenue + sugarcane_revenue
    )

    # Chemical-free crops at 11 months:
    # First 6 months: Tomato, Potato, Cabbage
    # Next 4 months: Sunflower (total = 10 months)
    # Sugarcane still NOT converted at 11 months
    chemical_free_sales = (
        tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue
    )

    return {
        "tomato": tomato_revenue,
        "potato": potato_revenue,
        "cabbage": cabbage_revenue,
        "sunflower": sunflower_revenue,
        "sugarcane": sugarcane_revenue,
        "overall": overall_sales,
        "chemical_free": chemical_free_sales
    }

data = farmer_revenue()

print("Revenue Details (in ₹):")
print("Tomato:", int(data["tomato"]))
print("Potato:", int(data["potato"]))
print("Cabbage:", int(data["cabbage"]))
print("Sunflower:", int(data["sunflower"]))
print("Sugarcane:", int(data["sugarcane"]))
print()

print("a) Overall Sales (all crops):", int(data["overall"]))
print("b) Chemical-Free Sales at 11 Months:", int(data["chemical_free"]))
