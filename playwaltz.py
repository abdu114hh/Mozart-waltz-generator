import stdaudio
import stdio
import sys

# read a sequence of 32 numbers representing the 32 measures of
# the mozart waltz
samples = stdio.readAllInts()

# if the length of the sequence does not equal 32, exit with
# an error message.
if len(samples) != 32:
    sys.exit("A waltz must contain exactly 32 measures.")

else:

    # if a Minuet measure is not from [1, 176], exit with an
    # error message.
    for i in range(16):
        if samples[i] < 1 or samples[i] > 176:
            sys.exit("A minuet measure must be from [1, 176]")
    # if a Trio measure is not from [1, 96], exit with an
    # error message.
    for j in range(16, 32):
        if samples[j] < 1 or samples[j] > 96:
            sys.exit("A trio measure must be form [1, 96]")

    # Play the waltz sequence
    for i in samples:
        stdaudio.playFile('data/M' + str(i))
