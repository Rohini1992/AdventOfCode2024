def merge(arr, left, right, mid):
  n1 = mid - left + 1
  n2 = right - mid

  L1 = [0]*n1
  L2 = [0]*n2

  for i in range(n1):
    L1[i] = arr[left + i]

  for j in range(n2):
    L2[j] = arr[mid + 1 + j]

  i=0;j=0;k=left

  while i < n1 and j < n2:
    if L1[i] < L2[j]:
      arr[k] = L1[i]
      i += 1
    else:
      arr[k] = L2[j]
      j += 1
    k += 1

  while i < n1:
    arr[k] = L1[i]
    k+=1; i+=1

  while j < n2:
    arr[k] = L2[j]
    k+=1; j+=1

def mergeSort(arr, left, right):
  if left < right:
    mid = (left + right) // 2
    mergeSort(arr, left, mid)
    mergeSort(arr, mid+1, right)
    merge(arr, left, right, mid)

if __name__ == "__main__":
    L1 = []
    L2 = []
    fp = open('data/input_day1_part1.csv')
    for data in fp:
        data = str.replace(data, "\n",'').split('   ')
        L1.append(int(data[0]))
        L2.append(int(data[1]))

    # sorts in place
    mergeSort(L1, 0, len(L1)-1)
    mergeSort(L2, 0, len(L2)-1)

    dist = 0
    n1 = len(L1)
    for i in range(n1):
        dist = dist + abs(L1[i]-L2[i])
    print(dist)