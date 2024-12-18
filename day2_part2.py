from typing import List
from day2_part1 import parseReports, isSafe

def isSafeDiff(diff:int, diff_prior:int) -> bool:
  if abs(diff) == 0 or abs(diff) > 3:
      return False
  if diff_prior and diff_prior*diff <0:
      return False
  return True

def isSafeDroppedLevel(report: List[int]) -> bool:
  l = len(report)
  if l<2:
    return True

  if isSafe(report):
    return True

  diff_prior = None
  count_drop = 0

  for i in range(1,l-1):
    diff = report[i] - report[i-1]
    diff_next = report[i+1] - report[i]
    print(f"prior diff is {diff_prior}\ncurrent diff is: {diff}.\nNext diff is {diff_next}")
    if not isSafeDiff(diff, diff_prior):
      print("entering not safe diff condition")
      diff = diff + diff_next
      print(f"new ndiff is {diff}")
      if not isSafeDiff(diff, diff_prior):
        print("new diff was also not safe")
        return False
      else:
        count_drop += 1
        break
    diff_prior = diff

  if count_drop:
    i = i+1
    if not isSafe(report[i:]):
      return False

  return True

if __name__ == "__main__":
  reports_path = 'data/input_day2_part2.csv'
  data = parseReports(reports_path)
  result_drop_level_safe = [isSafeDroppedLevel(x) for x in data]
  print(sum(result_drop_level_safe))