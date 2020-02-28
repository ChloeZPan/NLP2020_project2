"""
The test file. The grader will use this file to test whether your system gives the right answer.
It should run with the following command `python3 test.py` from the *root directory* of the assignment.
"""

import csv
import re
from code import *

input_dir = 'input/'
output_dir = 'output/'


def read_file(filename):
  with open(filename, mode='r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    test = []
    for row in csv_reader:
      if row:
        if row[0].strip()[:2] == '((' and row[0].strip()[-2:] == '))':
          conclusion = []
          for goal_set in row:
            goal_set = re.sub('\)\s*\(', '),(', goal_set).strip()[1:-1]
            conclusion.append(list(map(parse_tuple_string, goal_set.split(","))))
        else:
          conclusion = list(map(list, list(map(list_tuple_string, row))))
        test.append(conclusion)
  return test


def run_tests(inputs, ans_test, ans_gold):
  """Compares test answers to gold answers and prints number correct"""
  n = 0
  m = 1
  for (i, t, g) in zip(inputs, ans_test, ans_gold):
    if t == g:
      s = 'SUCCESS'
      n = n+1
    else:
      s = 'FAILURE'
    print('%d: %s\n  in:   %s\n  test: %s\n  gold: %s' % (m, s, i, t, g))
    m += 1
  print('NUMBER CORRECT: %s / %s\n' % (n, len(ans_gold)))


def test_recognize_intent():
  """Test 'recognize_intent' function"""
  in_raw = read_file(input_dir + 'observations_test.txt') + read_file(input_dir + 'observations_custom.txt')
  out_raw = read_file(output_dir + 'intents_test.txt') + read_file(output_dir + 'intents_custom.txt')
  ans_test = [recognize_intent(x) for x in in_raw]
  ans_gold = out_raw
  print('\n\nTesting function \'recognize_intent\':')
  run_tests(in_raw, ans_test, ans_gold)


def main():
  test_recognize_intent()
  

if __name__== "__main__":
  main()
