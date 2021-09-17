- Number of ways to arrange n objects: n!
- Ways to select (Order doesn't matter) - nCr
- Ways to arrange n objects - Order matters - nPr

Probability:
- Probabilities are defined using a sample space of possible states of the world
- The event can occur on not occur in each world
- The probability of an event is the fraction of worlds in which it occurs
- A distribution just assigns probabilities to events of the variable having a particular value 
- A measure of likelihood of an event
- A formal system to quantify uncertainity
- Applications: Everyday real-world problems deal with uncertain information and/or outcomes
  > Product reliability [Electronics and Vehicles]
  > Risk Assesment [Financial, Environmental]
  > Diagnosis - Predict cause given symptoms [Medical Treatment, Mechanical Repairs]
- Rules of Probability:
  > A and B are events of uncertain occurrence
  > Probability  theory assumes these axioms: 0 <= P(A) <= 1
  > P(True) = 1, P(False) = 0
  > P(A or B) = P(A) + P(B) - P(A and B)
- Discrete Probability: Deals with events that occur in countable sample spaces
- We can collapse continuous things like temperature to discrete values
- Uniform Distribution
  > Simplest of all probability distributions
  > A known finite number of outcomes are equally likely to occur
  > Each of n values have 1/n probability
- Word Frrequencies:
  > How many distinct words are in a text sample?
  > What are frequencies of individual words?
  > We distinguish between tokens and types:
    - Tokens: Occurrences of words
    - Types: Distinct words 
    blue fish red fish yellow fish black fish
    tokens: 8
    types: 5
  > Sample using word frequencies:
    - Duplicate words in a list by their multiplicity, then sample that list with their multiplicity
    - Assign a number 2 3 4 5 to fish and other 4 numbers and do uniform sampling
- Joint Probabilities:
  - Pr(A) and Pr(B) don't give enough information to determine the joint probability Pr(A and B)
    usually written Pr(A, B)
  - One event might prevent occurrence of another event
- Marginal Proibabilities:
  - We can go the other way, and recover the marginals Pr(A) and Pr(B) from the joints:
    Pr(odd) = Pr(odd, prime) + Pr(odd, non-prime)
- Conditional Proability:
  - Given the rol was odd, what is the probability it is prime?
  - Pr(A|B) = Pr(A,B)/Pr(B)
- If A and B don't influence each other P(A, B) = P(A).P(B)

Markov Chain:
- A Markov chain consists of states linked by transitions labeled with probabilities
- Directed Graph
- Starting from a state, we repeatedly pick transitions according to their probabilities
- Previous states are not important, we reached at a state and how we transitionfrom it
- Decision on current state is independent of the previous states we were in
- Memory less process

Second Order Markov Chain:
- Has transitions depending upon two previous states [more context]

- nth order Markov Chain has transitions depending on n previous states

