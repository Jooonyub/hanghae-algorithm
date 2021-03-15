'''
house = {}
house['r'] = 53
house['g'] = 82
house['b'] = 60

print(house.keys())
print(house.values())

minimum = min(house['r'],house['g'],house['b'])
#min_color = house.key(minimum)
value_list = list(house.values())
print(value_list)
idx = value_list.index(minimum)
idx_key = list(house.keys())[idx]

print(f"minimum = {minimum}")
print(idx)
print(idx_key)
#print("min_color = {min_color}")

'''
houses = []
#for i in range(4):
    
    #houses.append(i)

dic = {'r':50, 'g':30, 'b': 35}
houses.append(dic)
print(houses)