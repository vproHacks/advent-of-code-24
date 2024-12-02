# Part 1
print(sum(abs(x - y) for x, y in zip(*map(sorted, zip(*(map(int, line.split()) for line in open('input')))))))

# Part 2
print(([(x := list(zip(*(map(int, line.split()) for line in open('input')))))] + [c := __import__('collections').Counter(x[1])] + [sum(c.get(a, 0) * a for a in x[0])])[2])