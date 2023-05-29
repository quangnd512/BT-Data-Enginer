def is_valid_brackets(string):
  """
  Determines if the given string contains balanced brackets.

  Args:
    string: The string to check.

  Returns:
    True if the string contains balanced brackets, False otherwise.
  """

  stack = []
  for char in string:
    if char in '({[':
      stack.append(char)
    elif char in ')})':
      if len(stack) == 0 or stack.pop() != char:
        return False

  return len(stack) == 0
