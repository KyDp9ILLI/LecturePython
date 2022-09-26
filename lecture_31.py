# f = open('f.txt', 'r')
# data = f.read() + ' '
# f.close()

# numbers = []

# while data != '':
#     space_pos = data.index(' ')
#     numbers.append(int(data[:space_pos]))
#     data = data[space_pos+1:]

# out = []
# for e in numbers:
#     if not e % 2:
#         out.append((e,e **2))
# print(out)

# def select(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = select(int,data)
# res = where(lambda x: not x%2, res )
# res = select(lambda x: (x,x**2),res)
# print(res)

# def select(f,col):
#     return [f(x) for x in col]

# def where(f,col):
#     return [x for x in col if f(x)]

# data = '1 2 3 5 8 15 23 38'.split()

# res = map(int,data)
# res = filter(lambda x: not x%2, res )
# res = list(map(lambda x: (x,x**2),res))
# print(res)

# li = [x for x in range(1,20)]

# li = list(map(lambda x:x+10,li))

# print(li)

# data = list(map(int,input().split()))
# print(data)

# data = map(int,'1 2 3'.split())

# for e in data:
#     print(e)

# print('--')

# for e in data:
#     print(e)

# data = [x for x in range(10)]
# res = list(filter(lambda x:not x%2,data))
# print(res)
