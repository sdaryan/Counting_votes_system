#سیستم شماره آراء
import collections

ara = []
ray = dict()
n = int(input("Enter the number of elements: "))

for i in range(0, n):   #get Counting of  votes
    ara.append(input())

for i in range(0, len(ara)):         #get votes 
    ray[ara[i]] = ara.count(ara[i])


od = collections.OrderedDict(sorted(ray.items()))  #sorting list
for key, value in od.items():
    print(key," : ", value)

