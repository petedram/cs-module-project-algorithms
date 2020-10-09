#!/usr/bin/python

import sys

def rock_paper_scissors(n, cache=[[]]):
  # Your code here
  if n == 0:
    return cache
  
  #recursion
  #use a cache to store each possible play
  '''
  * used to repeat
  for each item in cache, add item to array, add same value to it
  if none, adds ['rock'], ['paper'], ['scissors']
  next recursion adds:
    [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']])
    and so on

  '''
  return rock_paper_scissors(n-1, [[*i, x] for i in cache for x in ['rock', 'paper', 'scissors']])


print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')