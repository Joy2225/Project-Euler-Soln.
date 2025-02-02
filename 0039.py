'''If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.
{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
For which value of p<1000, is the number of solutions maximised?'''
def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2

def find_right_triangles(p):
    count = 0
    for a in range(1, p//2):
        for b in range(a, p//2):
            c = p - a - b
            if c < b:
                break
            if is_right_triangle(a, b, c):
                count += 1
    return count

max_count = 0
max_p = 0
for p in range(1, 1000):
    count = find_right_triangles(p)
    if count > max_count:
        max_count = count
        max_p = p
print(max_p)
# 840