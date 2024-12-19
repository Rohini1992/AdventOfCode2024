from typing import Tuple, List

# instead of getting the full list of possible operation sequences
# we can use a generator to save space
# arguably this will occupy space for the call stack
# but looks cleaner
def generate_ops(n):
    if n <= 0:
        yield ""
    else:
        for substring in generate_ops(n - 1):
            yield substring + '*'
            yield substring + '+'

def generate_ops_2(n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    else:
        result = []
        for substring in generate_ops_2(n - 1):
            result.append(substring + ['*'])
            result.append(substring + ['+'])
            result.append(substring + ['||'])
        # For n = 1, include the initial operations
        if n == 1:
            result.append(['*'])
            result.append(['+'])
            result.append(['||'])
        return result

def parseTxtToArr(path: str) -> List:
    data = open(path).read().splitlines()
    data = [line.split(": ") for line in data]
    data = [(int(tup[0]),list(map(int,tup[1].split(" ")))) for tup in data]
    return data

# This is a convenience function. We don't necessarily need it
def createOpsString(ops_seq: str, int_seq:List[int]) -> List:
    final = []
    for i in range(len(ops_seq)):
        final.append(int_seq[i])
        final.append(ops_seq[i])
    final.append(int_seq[i+1]) # one more number than operator
    return final

# Accidentally wrote the function to apply BODMAS rules
# But our part 1 question is strictly left to right
def isMatchRules(input:Tuple[int,List[int]]) -> bool:
    outcome = input[0]
    int_seq = input[1]
    int_seq_len = len(int_seq)
    for ops_seq in generate_ops(int_seq_len-1):
        seq_final = createOpsString(ops_seq, int_seq)
        stack = []
        i = 0
        print(seq_final)
        while (i < len(seq_final)):
            print("stack is :", stack)
            if seq_final[i] != "*":
                stack.append(seq_final[i])
                print("stack is :", stack)
                i += 1
            else:
                last = stack.pop()
                temp = last*seq_final[i+1]
                stack.append(temp)
                i += 2
                print("stack is :", stack)
        
        outcome_ops = sum([stack[i] for i in range(len(stack)) if i%2==0])
        if outcome_ops == outcome:
            return True
    
    return False

def isMatchLefttoRight(input:Tuple[int,List[int]]) -> bool:
    outcome = input[0]
    int_seq = input[1]
    int_seq_len = len(int_seq)
    for ops_seq in generate_ops(int_seq_len-1):
        # helpful if you want to print it
        seq_final = createOpsString(ops_seq, int_seq)
        i = 0
        left = int_seq[0]
        # print(seq_final)
        while (i < len(ops_seq)):
            # print(left)
            right = int_seq[i+1]
            if ops_seq[i] == "+":
                left = (left + right)
            else:
                left = (left * right)
            i += 1
        if left== outcome:
            return True
    return False

def isMatchLefttoRight_2(input:Tuple[int,List[int]]) -> bool:
    outcome = input[0]
    int_seq = input[1]
    int_seq_len = len(int_seq)
    for ops_seq in generate_ops_2(int_seq_len-1):
        # helpful if you want to print it
        # print(ops_seq, int_seq)
        seq_final = createOpsString(ops_seq, int_seq)
        i = 0
        left = int_seq[0]
        # print(seq_final)
        while (i < len(ops_seq)):
            right = int_seq[i+1]
            # print(f"left and right are {left}, {right}")
            if ops_seq[i] == "+":
                left = (left + right)
            elif ops_seq[i] == "*":
                left = (left * right)
            else:
                left = int(str(left)+str(right))
                # print(f"left is {left}")
            i += 1
        if left== outcome:
            return True
    return False

if __name__ == "__main__":
    # outcome = 7290
    # int_seq = [6,8,6,15]
    # print(isMatchLefttoRight_2((outcome, int_seq)))

    input_path = "data/input_day7_part1.txt"
    input_data = parseTxtToArr(input_path)
    # match_results = [isMatchLefttoRight(pair) for pair in input_data]
    match_sum = sum([pair[0] for pair in input_data if isMatchLefttoRight(pair)])
    match_sum_2 = sum([pair[0] for pair in input_data if isMatchLefttoRight_2(pair)])
    print(match_sum, match_sum_2)

