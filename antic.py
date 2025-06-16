# 🕰️ Ye Olde Programme: Summatione of Two Numerals 🕰️
# By the grace of Python, under the reign of Guido van Rossum

def summon_numeral(prompteth):
    try:
        return float(input(prompteth))
    except ValueError:
        print("Thou hast entered folly! Only numerals, kind soul.")
        return summon_numeral(prompteth)

def ye_addeth(a, b):
    return a + b

print("📜 Welcome, noble user, to Ye Olde Adding Machine 📜\n")

# The sacred input
numeral_one = summon_numeral("Pray, enter thy first numeral: ")
numeral_two = summon_numeral("Now, noble one, thy second numeral: ")

# The ancient calculation
total = ye_addeth(numeral_one, numeral_two)

# The proclamation of result
print(f"\n✨ Lo! The sum of thine inputs is: {total} ✨")
print("\nMay your computations be ever accurate, and your syntax ever true.")
