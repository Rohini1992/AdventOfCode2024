from typing import Tuple, List
def parseReports(path: str) -> List[List[int]]:
  L = []
  fp = open(path)
  for data in fp:
    data = str.replace(data, "\n",'').split(' ')
    sublist = [int(x) for x in data]
    L.append(sublist)
  return L

def isSafe(report: List[int]) -> bool:
  l = len(report)
  diff_prior = None
  for i in range(1,l):
    diff = report[i] - report[i-1]
    if abs(diff) == 0 or abs(diff) > 3:
      return False
    if diff_prior and diff_prior*diff <0:
      return False
    diff_prior = diff
  return True

if __name__ == "__main__":
  reports_path = 'data/input_day2_part2.csv'
  data = parseReports(reports_path)
  result = [isSafe(x) for x in data]
  print(sum(result))