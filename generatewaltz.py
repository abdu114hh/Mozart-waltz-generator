import stdarray
import stdrandom
import stdio

# Create an 11 x 16 2D array with all values set to 0
x = stdarray.create2D(11, 16, 0)

# Read the data from mozart.txt into the 2D array x
for i in range(11):
    for j in range(16):
        x[i][j] = stdio.readInt()

# create a 6 x 16 2D array with all values set to 0

y = stdarray.create2D(6, 16, 0)
# Read the remaining data from mozart.txt into the 2D array y
for i in range(6):
    for j in range(16):
        y[i][j] = stdio.readInt()

# Populate array x with a random minuet measures, determined
# by the sum of two die rolls, from the minuet table and write
# it to standard output
for j in range(16):
    for i in range(1):
        die_roll_1 = stdrandom.uniformInt(0, 6)
        die_roll_2 = stdrandom.uniformInt(0, 6)
        sum_die_rolls = die_roll_1 + die_roll_2
        stdio.write(str(x[sum_die_rolls][j]) + " ")

# Populate array y with 16 random Trio measures, determined
# by a single die rolls, from the Trio Table and write it to
# standard output
for j in range(16):
    for i in range(1):
        die_roll_3 = stdrandom.uniformInt(0, 6)
        stdio.write(str(y[die_roll_3][j]) + " ")
stdio.writeln()
