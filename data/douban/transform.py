# g = open("edges_space.txt", "w")
#
# with open("edges.txt") as f:
#     for line in f.readlines():
#         print(" ".join(line.strip().split(",")), file=g)
#
# g.close()


# users = {}
# with open("edges.txt") as f:
#     for line in f.readlines():
#         u, v = line.strip().split(",")
#         if u not in users:
#             users[u] = 1
#         if v not in users:
#             users[v] = 1
#
# print(len(users))


max_len = 0
avg_len = 0
sum_len = 0
min_len = 10000
count = 0
with open("cascade.txt") as f:
    for line in f.readlines():
        length = len(line.strip().split())
        sum_len += length
        count += 1
        if length > max_len:
            max_len = length
        if length < min_len:
            min_len = length
avg_len = sum_len / count

print(max_len)
print(min_len)
print(avg_len)