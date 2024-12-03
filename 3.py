# Part 1
print(sum((x := eval(mul[3:]))[0] * x[1] for mul in __import__('re').findall(r"(?:mul\()\d+,\d+\)", open('input').read())))

# Part 2
print(((f := 1) - 1) + sum(((f * (x := eval(cmd[3:]))[0] * x[1]) if cmd.startswith('mul') else ((f := int(cmd == "do()"))) * 0) for cmd in __import__('re').findall(r"(?:mul\()\d+,\d+\)|(?:do\()\)|(?:don't\()\)", open('input').read())))