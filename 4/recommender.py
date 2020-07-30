# 0 = Green Square
# 1 = Red Triangle
# 2 = Yellow Circle
# 3 = Blue Star

pattern = [ [1,0,0,1,2,1,3,2],
            [2,1,3,0,2,3,0,0],
            [2,3,1,2,2,0,3,1],
            [0,3,2,3,1,3,0,2],
            [1,1,0,2,3,0,1,3],
            [3,2,1,3,2,3,1,3],
            [0,1,3,0,0,1,2,1]]

print("-------")
print("PATTERN:")
for row in pattern:
    print(row)
print("-------")

# Yellow Circle, Red Triangle, Blue Star
test_pattern = [2, 1, 3]
pattern_found = False

# symbol_after_pattern[0] = Number of Green Squares after the pattern
# symbol_after_pattern[1] = Number of Red Triangles after the pattern
# symbol_after_pattern[2] = Number of Yellow Circles after the pattern
# symbol_after_pattern[3] = Number of Blue Stars after the pattern
symbol_after_pattern = [0,0,0,0]

print("")
print("Going to check the existing patterns for the pattern", test_pattern)
print("-------")
for x in range(0, len(pattern)):
    if len(test_pattern) <= len(pattern[x]):
        for y in range(0, len(pattern[x]) - (len(test_pattern)-1)):
            if(pattern[x][y:y+len(test_pattern)] == test_pattern):
                print("-------")
                print("FOUND A PATTERN")
                pattern_found = True
                print("row =", x)
                print("column start =", y)
                columnEnd = y+len(test_pattern)-1
                print("column end =", columnEnd)
                print("-------")
                if columnEnd < len(pattern[x])-1:
                    symbol_after_pattern[pattern[x][columnEnd+1]] += 1

if (not pattern_found):
    print("NO MATCHING PATTERNS FOUND!")

index_max = max(range(len(symbol_after_pattern)), key=symbol_after_pattern.__getitem__)

if index_max == 0:
    print("I would recommend the green square!")
elif index_max == 1:
    print("I would recommend the red triangle!")
elif index_max == 2:
    print("I would recommend the yellow circle!")
elif index_max == 3:
    print("I would recommend the blue star!")
