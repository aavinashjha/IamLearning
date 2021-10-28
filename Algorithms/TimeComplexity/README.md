- Not measuremenet in real time like in seconds
- Different computer for execution, running other application causing memory hogging
- How program run time goes asymptotically
- Linear algorithm: Solves double size problem in double time
- O(1) - Doesn't mean code has to run in 1 step, but no matter how steps it is, if it doesn't change with
  size of inputs, its asymptotically constant
- O(n2) will not always run slower than O(n) 
- O(lgn) - doubling size of array increases the runtime by 1 chunk of code
- Big O:
  > f(n) is O(g(n)) if c and n0, f(n) <= c*g(n) for all n > n0
  > f(n) is Omega(g(n)) if c and n0, f(n) >= c*g(n) for all n > n0
  > f(n) is Theta(g(n)) if f(n) is O(g(n)) and Omega(g(n))
  > n has to be positive number
