import numpy as np
import matplotlib.pyplot as plt

include_avg = False

# set width of bar
barWidth = 0.18
 
# set height of bar
# base = [7.44, 7.54, 12.56, 13.19, 33.76, 37.18, 78.56, 77.11]
# unigram = [7.71, 7.74, 16.40, 17.84, 37.05, 40.78, 78.93, 77.72]
# unigram_w = [7.72, 7.79, 18.52, 19.92, 39.86, 43.56, 80.86, 78.72]
# bigram = [7.35, 7.35, 10.89, 11.17, 30.55, 33.24, 77.52, 76.25]
# bigram_w = [7.84, 7.87, 14.64, 15.42, 37.43, 40.58, 80.75, 78.32]

# TEST SET
base = [6.81, 6.87, 11.54, 12.21, 32.43, 35.85, 77.78, 76.76]
unigram = [7.16, 7.20, 14.45, 15.49, 35.51, 39.08, 78.50, 77.56]
unigram_w = [7.76, 7.82, 18.23, 19.78, 39.43, 43.10, 80.13, 78.76]
bigram = [7.13, 7.20, 11.44, 11.89, 30.99, 34.18, 77.18, 76.39]
bigram_w = [7.74, 7.78, 18.43, 19.84, 40.23, 43.94, 81.14, 79.21]



labels = ['d1_5', 'd2_5', 'd1_10', 'd2_10', 'd1_20', 'd2_20', 'd1_avg', 'd2_avg']

if not include_avg:
    del base[-2:]
    del unigram[-2:]
    del unigram_w[-2:]
    del bigram[-2:]
    del bigram_w[-2:]
    del labels[-2:]

# Set position of bar on X axis
r1 = np.arange(len(base))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]
 
# Make the plot
plt.bar(r1, base, color='#0CCE6B', width=barWidth, edgecolor='white', label='base')
plt.bar(r2, unigram, color='#ED7D3A', width=barWidth, edgecolor='white', label='unigram')
plt.bar(r3, unigram_w, color='#F0945D', width=barWidth, edgecolor='white', label='unigram-10')
plt.bar(r4, bigram, color='#DA294F', width=barWidth, edgecolor='white', label='bigram')
plt.bar(r5, bigram_w, color='#F04065', width=barWidth, edgecolor='white', label='bigram-5')
 
# Add xticks on the middle of the group bars
plt.xlabel('groups per d-n', fontweight='bold')
plt.ylabel('diversity score', fontweight='bold')
plt.xticks([r + 2*barWidth for r in range(len(base))], ['d-1 (5%)', 'd-2 (5%)', 'd-1 (10%)', 'd-2 (10%)', 'd-1 (20%)', 'd-2 (20%)', 'd-1 (avg)', 'd-2 (avg)'])
 
# Create legend & Show graphic
plt.legend()
plt.show()
