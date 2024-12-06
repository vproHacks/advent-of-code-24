# Part 1
print(((o := [list() for _ in range(100)]), (u := []), list(o[(r := list(map(int, s.split('|'))))[1]].append(r[0]) if '|' in s else (u.append(list(map(int, s.split(',')))) if s != '\n' else 0) for s in open('input')), (v := lambda i, t: all(c in t[:i] or c not in t for c in o[t[i]])), (sum(t[len(t)//2] if all(v(i, t) for i in range(len(t))) else 0 for t in u)))[-1])

# Part 2
# Could have used sorted before to make it better, but laziness and bad ideas prevail
print(((o := [list() for _ in range(100)]), (u := []), list(o[(r := list(map(int, s.split('|'))))[1]].append(r[0]) if '|' in s else (u.append(list(map(int, s.split(',')))) if s != '\n' else 0) for s in open('input')), (v := lambda i, t: all(c in t[:i] or c not in t for c in o[t[i]])), (sum(0 if all(v(i, t) for i in range(len(t))) else (sorted(t, key=__import__('functools').cmp_to_key(lambda a, b: -1 if a in o[b] else 1))[len(t)//2]) for t in u)))[-1])