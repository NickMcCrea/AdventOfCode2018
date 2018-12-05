

#load Problem1.txt
with open("Input/Problem1.txt") as f:
    content = f.readlines()

freq_counter = dict()

searching=True
frequency = 0
while(searching):

    for line in content:
        lineInt = int(line)
        frequency += lineInt
        if not freq_counter.__contains__(frequency):
            freq_counter.update({frequency:1})
            print("Adding new frequency to dict")
        else:
            freq_counter.update({frequency:freq_counter.get(frequency)+1})
            print("Incrementing frequency count")
            print(frequency)
            searching = False
            exit()
