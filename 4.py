# Part 1
print(((it := __import__('itertools')), ('-'.join((s := [x.strip() for x in open('input')]) + [x[::-1] for x in s] + (c := [''.join(x) for x in zip(*s)]) + [x[::-1] for x in c] + (d1 := [''.join(s[x][y] for x, y in c) for _, c in it.groupby(sorted(it.product(range(len(s)), range(len(s[0]))), key=sum), key=sum)]) + [x[::-1] for x in d1] + (d2 := [''.join(s[x][y] for x, y in c) for _, c in it.groupby(sorted(it.product(range(len(s)), range(len(s[0]))), key=lambda x: x[0] - x[1] - len(s) + 1), key=lambda x: x[0] - x[1] - len(s) + 1)]) + [x[::-1] for x in d2]).count('XMAS')))[1])

# Part 2
# Just create a 3x3 search window and compare against set solutions 
print(((s := [r.strip() for r in open('input')]), (g := ['MAS', 'SAM']), (v := lambda m: int((((m[0][0] + m[1][1] + m[2][2]) in g) and ((m[2][0] + m[1][1] + m[0][2])) in g))), sum(sum(v([x[j-3:j] for x in s[i-3:i]]) for j in range(3, len(s[0]) + 1)) for i in range(3, len(s) + 1)))[-1])