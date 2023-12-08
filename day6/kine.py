from math import ceil, floor

lines = open('testcase')

times = [ int(i) for i in lines.readline().split(':')[1].split() ]
distances = [ int(i) for i in lines.readline().split(':')[1].split() ]

# basic kinematics, equation is  d = -x^2 + tx (d=distance, t=time)
# ==> d = -(x - t/2) + (t/2)^2
# ==> x = t/2 +/- ((t/2)^2 - d)^0.5

timeprod = 1

def min_time(t, d):
    charge = ceil(t/2 - ((t/2)**2 - d)**0.5)
    return charge

def max_time(t, d):
    charge = floor(t/2 +   ((t/2)**2 - d)**0.5)
    return charge


for i in range(len(times)):
    min_charge = min_time(times[i], distances[i])
    max_charge = max_time(times[i], distances[i])
    # have to charge for at least min, but no more than max, so ints 
    # between the two (inclusive)
    charge_diff = max_charge - min_charge
    if charge_diff % 2 == 0:
        timeprod *= (charge_diff - 1)
    else:
        timeprod *= (charge_diff + 1)

print(timeprod)
