# CSC247/447 Project 2: Intention/Goal Recognition

## Description

Based on the weighted abductive reasoning we learned in lecture, write a program that can match the observation into plans and output a set of possible goals.

You're given 

1) a set of observations, which are triples of words in the TRIPS lexicon. 

2) a plan library with a set of plans. A plan consists of sequences of actions associatd with a goal. Each element in a plan triple is a TRIPS ontology type and the argument elements contain a variable.

The input is a list of consecutive observations and the result of matching the observation into a plan is an action instantiated with the word from the observation. Your goal is to find the best action that explains the observations. For each observation, your code should output a set of possible goals and continue this task as it receives more observations.

For weighted abduction, assume that the cost to assume each goal is 1.

## Examples

Given a plan library
```
goal: (ONT::STEAL ?x:ONT::PERSON ?z:FACILITY)   
acts: (ONT::MOTION ?x::PERSON ?Z::FACILITY)
      (ONT::BODY-MANIPULATION ?x::PERSON ?Y::WEAPON)
      (ONT::DIRECTIVE ?x::PERSON ?X:MONEY)
      (ONT::DEPART ?x::PERSON ?z::FACILITY)
```
and an observation

```
(travel partner store)
```

the result of matching the observation into this plan would be an instantiated plan where we use the word as the instance of the TRIPS ontology type.

```
goal: (ONT::STEAL partner store)   
acts: (ONT::MOTION partner store)
      (ONT::BODY-MANIPULATION partner ?Y::WEAPON)
      (ONT::DIRECTIVE partner ?X:MONEY)
      (ONT::DEPART partner store)
```

## Notes

Your code should be able to do the following tasks.

1. Variable binding

Given `(travel partner store)`, once you bind the varialbes in `(ONT::BODY-MANIPULATION partner ?Y::WEAPON)` and instantiate `(ONT::BODY-MANIPULATION partner ?Y::WEAPON)`, you cannot match this instantiated action with `(grasp person gun)` since `person` is not equal to `partner`.


2. Word sense disambiguation in context

Note that some words are ambiguous as in they can have multiple meanings. For example, the word `partner` can map to two different TRIPS ontology types: `ONT::AFFILIATE` and `ONT::FAMILY-RELATION`. This means `(travel partner store)` can match either `(ONT::MOVE ?x::PERSON ?Z::FACILITY)` or `(ONT::MOVE ?x::AFFILIATE ?Z::FACILITY)`.


3. Intention recognition with minimal covering explanation

Your goal is to find the best actions with the least commitment and the least cost. Use the following functions as we discussed in lecture.
```
cost(P ∨ Q) = min(cost(P), cost(Q))
cost(P & Q) = cost(P) + cost(Q)
```

## Provided starter code

We are providing PyTrips, a basic libarary for the Trips Ontology from the previous project. Details on how to use it are available in `demo.ipynb`. Please report any problems with PyTrips to the repository [here](https://github.com/mrmechko/pytrips). You can open issues for any bugs, errors, or questions.

## Submission

Submit a `[yourname].zip` file on Blackboard. Make sure that you've implemented the skeleton code in the`code.py` file.

Please include a `README.{txt|pdf}` file in your submission. This file should contain your **name**, **student ID**, and **email** in a header. Give a short outline of your implementation of the algorithms, and any additional commentary you feel is necessary (any specific running instructions, known issues/bugs your code has, etc.)

## Acknowledgement

Thanks to Rik Bose for providing us with PyTrips demo. 
