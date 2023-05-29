def longest_substring_without_repeats(string):
    

  start = 0
  end = 0
  seen = set()
  max_length = 0

  while end < len(string):
    if string[end] not in seen:
      seen.add(string[end])
      end += 1
      max_length = max(max_length, end - start)
    else:
      seen.remove(string[start])
      start += 1

  return max_length


if __name__ == "__main__":
  string = input("Enter a string: ")
  length = longest_substring_without_repeats(string)
  print("The length of the longest substring without repeating characters is", length)
