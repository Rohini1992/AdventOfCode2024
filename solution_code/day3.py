
if __name__ == "__main__":
    ##### PART 1
    import re
    path = '/content/input_day3_part1.txt'
    fp = open(path)
    input = ''
    for line in fp:
        input += line
        res = re.findall("mul\(([0-9]+,[0-9]+)\)",input)

    sum = 0
    for pair in res:
        x, y = map(int,pair.split(","))
        sum += x*y

    print(sum)

    ##### PART 2
    switch_pattern = "mul\(([0-9]+,[0-9]+)\)|(do\(\))|(don\'t\(\))"
    res_switch = re.findall(switch_pattern,input)

    on = 1
    sum_switch = 0
    for (pair, do, dont) in res_switch:
        if do:
            on = 1
        elif dont:
            on = 0
        if on and pair:
            x, y = pair.split(",")
            x, y = int(x), int(y)
            sum_switch += x*y

    print(sum_switch)