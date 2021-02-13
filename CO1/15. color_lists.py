color_list1=["White", "Black", "Red"]
color_list2=["Red", "Green"]

color_set_1 = set(color_list1)
color_set_2 = set(color_list2)
print("\nColors from color-list1 not contained in color-list2: ")
print(color_set_1.difference(color_set_2))