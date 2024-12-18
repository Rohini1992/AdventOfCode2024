import numpy as np
from typing import List
class xmasCrawler:

    def __init__(self, path):
        self.arr = self._txtToArr(path)
        self.xmas_count = 0
        self.xmas_modified_count = 0

    def _txtToArr(self, path: str) -> np.ndarray:
        arr = []
        with open(path, 'r') as fp:
            for line in fp:
                line = list(line.replace('\n', ''))
                arr.append(line)
        return np.array(arr)

    def validCoordinates(self, i, j):
        if (0 <= i < len(self.arr)) and (0 <= j < len(self.arr[0])):
            return True
        else:
            return False

    def countXmas(self, i, j, i_grad, j_grad):
        k = 0
        pattern = 'XMAS'
        for x in range(4):
            if self.validCoordinates(i, j) and self.arr[i][j] == pattern[x]:
                i += i_grad
                j += j_grad
            else:
                return
        self.xmas_count += 1
        return

    def countModifiedXmas(self, i, j):
      set1 = {'M', 'A', 'S'} - {self.arr[i-1,j+1],self.arr[i,j],self.arr[i+1,j-1]}
      set2 = {'M', 'A', 'S'} - {self.arr[i-1,j-1],self.arr[i,j],self.arr[i+1,j+1]}

      if (not set1) and (not set2):
        self.xmas_modified_count += 1

      return

    def runCrawler(self):
        grad_pairs = [(i_grad, j_grad) for i_grad in [-1, 0, 1] for j_grad in [-1, 0, 1] if (i_grad, j_grad) != (0, 0)]

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                if self.arr[i][j] == 'X':
                    for (i_grad, j_grad) in grad_pairs:
                        self.countXmas(i, j, i_grad, j_grad)

    def runModifiedCrawler(self):
        for i in range(1,len(self.arr)-1):
            for j in range(1,len(self.arr[0])-1):
                if self.arr[i][j] == 'A':
                  self.countModifiedXmas(i,j)

if __name__ == "__main__":
    full_input_path = '/content/input_day4_part1.txt'
    crawler = xmasCrawler(full_input_path)
    crawler.runCrawler()
    crawler.runModifiedCrawler()
    print(crawler.xmas_count, crawler.xmas_modified_count)