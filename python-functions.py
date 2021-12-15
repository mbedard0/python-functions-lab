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

# def get_string_at(start, end, str1): 
#   string = []
#   for j in range(start, end): 
#     string.append(str1[j])
#   return ''.join(string)

def occurrences(str1, str2):
  total = 0
  n = range(len(str1)) 
  for i in n:
    end = i + len(str2)
    if end > len(str1):
      return total
    # x = get_string_at(i, end, str1)
    x = str1[i:end]
    if (x == str2):
      total += 1
  return total

def product(*args):
  x = 1
  for arg in args:
    x *= arg 
  return x