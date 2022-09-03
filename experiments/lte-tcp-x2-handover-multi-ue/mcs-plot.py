import sys
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
# Positional arguments
parser.add_argument("--fileName", help="file name", default="DlMacStats.txt")
parser.add_argument("--plotName", help="plot name", default="mcs.png")
# Optional timestep argument
parser.add_argument("--title", help="title string", default="LTE handover MCS")
args = parser.parse_args()

times1=[]
times2=[]
values1=[]
values2=[]

fd = open(args.fileName, 'r')
next(fd)
for line in fd:
    l = line.strip().split()
    if line == "":
        continue
    if l[1].strip() == "1":
        times1.append(float(l[0]))
        values1.append(int(l[6]))
    elif l[1].strip() == "2":
        times2.append(float(l[0]))
        values2.append(int(l[6]))
fd.close()

if len(times1) == 0:
    print("No data points found, exiting...")
    sys.exit(1)

plt.scatter(times1, values1, marker='.', label='cell 1', color='red')
if len(times2) != 0:
    plt.scatter(times2, values2, marker='.', label='cell 2', color='blue')
plt.xlabel('Time (s)')
plt.ylabel('MCS')
plt.title(args.title)
#plt.show()
plt.ylim([-1,30])
plotname = args.plotName
plt.savefig(plotname, format='png')
plt.close()

sys.exit (0)