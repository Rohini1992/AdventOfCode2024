from typing import Dict, List
from collections import defaultdict

# # Old code
# # Assume n is length of update sequence
# # Assume k is length of rules
# # Then below is time complexity of each function
# def true_index(page, update_seq):
#   # O(n*m)
#   pages_after_page = sum(f"{page}|{after}" in rules for after in update_seq)
#   idx = len(update_seq) - 1 - pages_after_page
#   return idx

# def is_valid_update(update_seq):
#   # O(n)*O(true_index)
#   return all(true_index(page, update_seq)==i for i, page in enumerate(update_seq))

# def get_mid(update_seq):
#   return next(x for x in update_seq if true_index(x, update_seq)==len(update_seq)//2)

def parseOrder(rules:str) -> Dict:
  pageDict = defaultdict(int)
  for rule in rules.split('\n'):
    before, _ = rule.split('|')
    pageDict[before] += 1
  return pageDict  

def isValidSequence(update_seq:List[str], pageDict:Dict) -> bool:
  for i in range(1,len(update_seq)):
    if pageDict[update_seq[i]] > pageDict[update_seq[i-1]]:
      return False
  return True

def getCorrectSequence(update_seq:List[str], pageDict:Dict) -> List[str]:
  pagesAfter = []
  for i in range(len(update_seq)):
    pagesAfter.append(pageDict[update_seq[i]])
  correctIdx = pagesAfter.argsort()
  correctSequence = update_seq[correctIdx[::-1]]
  return correctSequence

def getMidValue(update_seq:List[str]) -> int:
#   print(update_seq)
  return int(update_seq[len(update_seq)//2])

if __name__ == "__main__":
    path = "data/input_day5_part1.txt"
    #path = "data/dummy_day5_local.txt"
    rules, updates = open(path).read().split('\n\n')
    updates = [update.split(",") for update in updates.split('\n')]
    
    pageDict = parseOrder(rules)
    sum_pt1 = 0
    sum_pt2 = 0
    for update_seq in updates:
        if isValidSequence(update_seq, pageDict):
          sum_pt1 += getMidValue(update_seq)
        else:
          correctSequence = getCorrectSequence(update_seq, pageDict)
          sum_pt2 += getMidValue(update_seq)
    
    print(sum_pt1, sum_pt2)

    # part1 = sum(int(get_mid(update_seq)) for update_seq in updates if is_valid_update(update_seq))
    # print(part1)

# all = sum(int(get_mid(update_seq)) for update_seq in updates)
# part2 = all - part1
# print(part2)