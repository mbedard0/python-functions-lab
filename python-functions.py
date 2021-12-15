def sum_to(n):
  x = 0
  j = 1
  while j <= n:
    x += j
    j += 1
  return x


def largest(list):
  x = 0
  for n in list:
    if n > x:
      x = n
  return x

def get_string_at(start, end, str1):  # start = 10, end = 12
  string = []
  for j in range(start, end): # [10, 11]
    string.append(str1[j])
  # string = [o, p]
  return ''.join(string)

def occurrences(str1, str2):
  total = 0
  n = range(len(str1)) # [0, 1, 2, ..., 10]
  for i in n:  # i = 10
    end = i + len(str2)  # end = 11
    if end > len(str1):
      return total
    x = get_string_at(i, end, str1)  # x = 'op'
    # x = str1[i:end]
    if (x == str2):
      total += 1
  return total

print(occurrences('fleep floop', 'p'))