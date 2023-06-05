#سیستم شماره آراء

ara = []
ray = dict()
n = int(input("Enter the number of elements: "))

for i in range(0, n):
    ara.append(input())

for i in range(0, len(ara)):
    ray[ara[i]] = ara.count(ara[i])

sorted_keys = sorted(ray.keys())
sorted_ray = {}
for key in sorted_keys:
    sorted_ray[key] = ray[key]
for k,v in sorted_ray.items():
    print(k ,' ', v)   




