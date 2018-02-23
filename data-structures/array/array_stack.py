class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            raise Empty('stack is empty')
        return self._data.pop()

def reverse_file(filename):
  """Overwrite given file with its contents line-by-line reversed."""
  S = ArrayStack()
  original = open(filename)
  for line in original:
    S.push(line.rstrip('\n'))     # we will re-insert newlines when writing
  original.close()

  # now we overwrite with contents in LIFO order
  output = open(filename, 'w')    # reopening file overwrites original
  while not S.is_empty():
    output.write(S.pop() + '\n')  # re-insert newline characters
  output.close()

def is_matched_html(raw):
  """Return True if all HTML tags are properly match; False otherwise."""
  S = ArrayStack()
  j = raw.find('<')               # find first '<' character (if any)
  while j != -1:
    k = raw.find('>', j+1)        # find next '>' character
    if k == -1:
      return False                # invalid tag
    tag = raw[j+1:k]              # strip away < >
    if not tag.startswith('/'):   # this is opening tag
      S.push(tag)
    else:                         # this is closing tag
      if S.is_empty():
        return False              # nothing to match with
      if tag[1:] != S.pop():
        return False              # mismatched delimiter
    j = raw.find('<', k+1)        # find next '<' character (if any)
  return S.is_empty()             # were all opening tags matched?

def is_matched(expr):
  """Return True if all delimiters are properly match; False otherwise."""
  lefty = '({['                               # opening delimiters
  righty = ')}]'                              # respective closing delims
  S = ArrayStack()
  for c in expr:
    if c in lefty:
      S.push(c)                               # push left delimiter on stack
    elif c in righty:
      if S.is_empty():
        return False                          # nothing to match with
      if righty.index(c) != lefty.index(S.pop()):
        return False                          # mismatched
  return S.is_empty()                         # were all symbols matched?