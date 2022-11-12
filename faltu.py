import multiprocessing as mp
print(mp.cpu_count())
# a = [x+1 for x in range(16)]
# b = [x for x in a[:len(a)//4]]
# c = [x for x in a[len(a)//4:len(a)//2]]
# d = [x for x in a[-len(a)//2:-len(a)//4]]
# e = [x for x in a[-len(a)//4:]]
a = [x+1 for x in range(27)]
f = len(a)//4
b = [x for x in a[:f]]
c = [x for x in a[f:f*2]]
d = [x for x in a[f*2:f*3]]
e = [x for x in a[f*3:]]
print(a)
print(b)
print(c)
print(d)
print(e)