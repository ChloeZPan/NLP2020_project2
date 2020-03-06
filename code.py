import json

"""
The skeleton file. You should implement your code here. Make sure that the code you write here runs properly
when called by the test.py file in the root directory.

Feel free to add any import statements above, AS LONG AS the package is jsontrips, pytrips, or any
package in the Python standard library.

Feel free to write any additional functions you need in this file, but DO NOT create any new Python files.
"""

def recognize_intent(observations, plan_library='both'):
  """Takes observations as input: this is a list of tuples of the form (word1, word2, word3), where each
     tuple represents an observation (listed in order of occurrence). Return a list of lists (interpreted as
     described in the guidelines), e.g. [[('ONT::STEAL', 'partner', 'store'), ('ONT::TARGET_PRACTICE', 'person', 'gun')]]
     NOTE: plan_library is either 'both', 'test', or 'custom'."""
  
  plan_library = read_plan_library(plan_library) # Read plan library from files in input/plan_libraries

  # TODO: IMPLEMENT FUNCTION HERE
  return [None]


def parse_tuple_string(str):
  """Parses a string representing a tuple into a tuple of strings."""
  strs = str.strip('(').strip(')').split()
  return (strs[0].lower(), strs[1].lower(), strs[2].lower())


def list_tuple_string(st):
  """Parses a string representing a tuple into list of a tuple of strings. """
  strs = st.strip().strip('(').strip(')').split()
  l = []
  l.append((strs[0].lower(), strs[1].lower(), strs[2].lower()))
  return l


def read_plan_library(plan_library='both'):
  """Reads in plan library from plan library files.
     NOTE: plan_library is either 'both', 'test', or 'custom'."""
  # Define file paths to load from
  plan_library_filename_test = 'input/plan_libraries/plan_library_test.json'
  plan_library_filename_custom = 'input/plan_libraries/plan_library_custom.json'
  plan_library_test = []
  plan_library_custom = []
  # Read test plan library
  with open(plan_library_filename_test) as f:
    plans_test = json.load(f)
    plan_library_test += [{'goal':parse_tuple_string(plan['goal']),
                           'acts':list(map(parse_tuple_string, plan['acts']))} for plan in plans_test]
  # Read custom plan library
  with open(plan_library_filename_custom) as f:
    plans_custom = json.load(f)
    plan_library_custom += [{'goal':parse_tuple_string(plan['goal']),
                             'acts':list(map(parse_tuple_string, plan['acts']))} for plan in plans_custom]
  if plan_library == 'both':
    return plan_library_test + plan_library_custom
  elif plan_library == 'custom':
    return plan_library_custom
  else:
    return plan_library_test
  