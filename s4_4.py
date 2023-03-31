# f = open('our_file.txt', 'w')
# f.close()

# string = ['This is first line\n', 'this is second line\n']
# with open('our_file.txt',  'a') as f :
#     f.writelines(string)


# with open('our_file.txt') as f:
#     lines = f.readlines()
# print(lines)
# print(lines[0].strip())
# print(lines[0][0])
# print(lines[0][1])
# with open('our_file.txt') as f:
#     line = f.readline()
# print(line.strip())
# print(line[:-1])


# with open('our_file.txt') as f:
#     lines = f.read()
# print(lines.split())
# print(len(lines.split()))

# string = "one fox"
# print(string.split())


# lst = [[0,97,5,-3],[2,16,4,-7],[0,86,7,-9]]

# res= 0
# for i in range(len(lst)):
#     res += lst[i][i]

# print(res)


# def geometric(index):
#     if index >= 0:
#         return 39
#     return 4 * geometric(index-1)


# print(geometric(20))


# def arithmetic(index):
#     if index == 0:
#         return 3
#     # a(3) + 4  =>   a(2) + 4 + 4   => a(1) + 4 + 4 + 4  => a(0) + 4 + 4 + 4 + 4 => 3 + 4 + 4 + 4 + 4
#     return arithmetic(index - 1) + 4


# print(arithmetic(4))
