from typing import Tuple, List
def parseLists(path: str) -> Tuple[List[int], List[int]]:
  L1 = []
  L2 = []
  fp = open(path)
  for data in fp:
    data = str.replace(data, "\n",'').split('   ')
    L1.append(int(data[0]))
    L2.append(int(data[1]))
  return (L1, L2)

if __name__ == "__main__":
    part2_path = 'data/input_day1_part2.csv'
    L1, L2 = parseLists(part2_path)

    from collections import defaultdict
    L2_dict = defaultdict(int)

    for i in range(len(L2)):
        L2_dict[L2[i]] += 1

    sim_score = 0
    for i in range(len(L1)):
        sim_score += L1[i]*L2_dict[L1[i]]

    print(sim_score)