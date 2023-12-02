import regex

lines = open('input').readlines(-1)
calsum = 0

for l in lines:
    pattern = regex.compile('\d')  #compiling since we're doing this a lot
    digits = pattern.findall(l)
    calsum += int(digits[0]) * 10 + int(digits[-1]) #first match is the 10s digit

print(calsum)

calsum = 0  #i am surprised I did not forget to do this

def word_to_int(word):
    if word == 'one':
        return 1
    elif word == 'two':
        return 2
    elif word == 'three':
        return 3
    elif word == 'four':
        return 4
    elif word == 'five':
        return 5
    elif word == 'six':
        return 6
    elif word == 'seven':
        return 7
    elif word == 'eight':
        return 8
    elif word == 'nine':
        return 9
for l in lines:
    pattern = regex.compile('\d|one|two|three|four|five|six|seven|eight|nine')
    #alternatively could s// words for digits?  not sure which would be faster

    digits = pattern.findall(l,overlapped=True)
    if len(digits[0]) > 1:
        firstnum = word_to_int(digits[0])
    else:
        firstnum = int(digits[0])

    if len(digits[-1]) > 1:
        lastnum = word_to_int(digits[-1])
    else:
        lastnum = int(digits[-1])

    calsum += ((firstnum * 10)+ lastnum)

print(calsum)

