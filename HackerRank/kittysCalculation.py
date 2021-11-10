

def def_value():
    return 'Not defined'


from collections import defaultdict

""" 

d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

print(d)

"""

def read_row():
    return (int(x) for x in input().split())

#add adjacancy list

adj_list = defaultdict(list)


n,q = read_row()


for _ in range (n-1):
    u,v = read_row()
    adj_list[u].append(v)
    adj_list[v].append(u)



for p, v in adj_list.items():
    print('key is  {} , value is {}'.format(p,v))


for v in adj_list:
    print(v)