# 1
# f = open('example.txt')
# text = f.read()
# f.close()
# print(text)

# 2
# with open('example.txt') as f:
#     text = f.read(10)
#     text2 = f.read(5)
#     text3 = f.read()
#     f.seek(0)
#     text4 = f.read()
# print(text4)


# with open('example.txt') as f:
    # print(f.readlines(-2))
    # for i in f:
    #     print(i)
    # fi = iter(f)
    # print(next(fi))

    # print(f.readline(1), f.readline(1))

counter, sum_ = 0, 0
with open('numbers') as fp:
    initial = fp.read()
    fp.seek(0)
    while (line := fp.readline().rstrip()) != '0':
        counter += 1
        sum_ += int(line)

# print(f'{counter}, {sum_}')


with open('numbers_report', 'w') as fp:
    fp.write(initial)
    fp.write('\n')

