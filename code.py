import json

"""
The skeleton file. You should implement your code here. Make sure that the code you write here runs properly
when called by the test1.py file in the root directory.

Feel free to add any import statements above, AS LONG AS the package is jsontrips, pytrips, or any
package in the Python standard library.

Feel free to write any additional functions you need in this file, but DO NOT create any new Python files.
"""

def recognize_intent(observations):
  """Takes observations as input: this is a list of tuples of the form (word1, word2, word3), where each
     tuple represents an observation. Return a set of possible goals, e.g.
     {(ONT::STEAL partner store), (ONT::TARGET_PRACTICE person gun)}"""
  
  plan_library = read_plan_library() # Read plan library from files in input/plan_libraries
  print(plan_library)

  # TODO: IMPLEMENT FUNCTION HERE
  pass


def parse_tuple_string(str):
  """Parses a string representing a tuple into a tuple of strings."""
  strs = str.strip('(').strip(')').split()
  return (strs[0], strs[1], strs[2])


def read_plan_library():
  """Reads in plan library from plan library files."""
  plan_library_test = 'input/plan_libraries/plan_library_test.json'
  plan_library_custom = 'input/plan_libraries/plan_library_custom.json'
  plan_library = []
  # Read test plan library
  with open(plan_library_test) as f:
    plans_test = json.load(f)
    plan_library += [{'goal':parse_tuple_string(plan['goal']),
                      'acts':list(map(parse_tuple_string, plan['acts']))} for plan in plans_test]
  # Read custom plan library
  with open(plan_library_custom) as f:
    plans_custom = json.load(f)
    plan_library += [{'goal':parse_tuple_string(plan['goal']),
                      'acts':list(map(parse_tuple_string, plan['acts']))} for plan in plans_custom]
  return plan_library
  