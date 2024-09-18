import random
import time
import matplotlib
matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
import math
# Initialize an empty list to store random numbers
random_numbers = []

# Set the end time to 60 seconds from the current time
end_time = time.time() + 1

# Generate random numbers for 60 seconds
while time.time() < end_time:
    # Generate a random float number between 0 and 10
    rand_num = math.ceil(random.random()*10)
    # Append the generated random number to the list
    random_numbers.append(rand_num)

# Plot the distribution of the generated random numbers
plt.hist(random_numbers, bins=30, edgecolor='black', alpha=0.7)
plt.title('Distribution of Random Numbers Generated in 60 Seconds')
plt.xlabel('Random Number')
plt.ylabel('Frequency')
# matplotlib.interactive(True)
plt.savefig('figure.png')
plt.show()
