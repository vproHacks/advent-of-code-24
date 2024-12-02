# Part 1
print(sum(int((l := list(map(int, line.split()))) and (s := sorted(l)) and (l == s or l == s[::-1]) and all(abs(l[i - 1] - l[i]) in [1, 2, 3] for i in range(1, len(l)))) for line in open('input')))

# Part 2
print(sum(any((f := list(map(int, line.split()))) and (l := f if i < 0 else f[:i] + f[i+1:]) and (s := sorted(l)) and (l == s or l == s[::-1]) and all(abs(l[i - 1] - l[i]) in [1, 2, 3] for i in range(1, len(l))) for i in range(-1, len(line.split()))) for line in open('input')))