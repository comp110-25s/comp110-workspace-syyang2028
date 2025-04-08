""" "Classwork"""

pids: set[int] = {710000000, 712345678}

pids.add(730746714)

print(pids)

ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 4}

ice_cream["vanilla"] += 110

ice_cream["mint"] = 3

f"There are {ice_cream["strawberry"]} orders of strawberry"

ice_cream["vanilla"] = 10

if "mint" in ice_cream:
    print(f"{ice_cream["mint"]} orders of mint")
else:
    print("No orders of Mint")

ice_cream.pop("strawberry")
