def self_num(n:int):
    return n+sum(list(map(int,str(n))))
a=set(range(1,10001))
b=set()
for i in a:
    b.add(self_num(i))
aa=a-b
for i in sorted(aa):
    print(i)