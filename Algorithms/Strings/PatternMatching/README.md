- Sorting can do better than NlgN if we don't do key compares

Key-Indexed Counting
--------------------
- Assumption about counting: Keys are integer between 0 and R-1
- Implication: Can use key as array index

Application:
- Sort string by first letter
- Sort class roster by section
- Sort phone numbers by area code
- Subroutine in a sorting algorithm

Remark:
- Keys may have associated data => Can't just count up number of keys of each value

Goal:
- Sort an array a[] of N integers between 0 to R-1
- Compute frequency cumulates which specify destination
 
Keyword-in-context search
-------------------------
Suffix Sorting solution
Preprocess: suffix sort the text
Query: binary search for query, scan until mismatch

> Longest repeated substring
  - Given a string of N characters, find the longest repeated substring
  - Applications: Bioinformatics, cryptanalysis, data compression
  Brute Force:
  - Try all indices i and j for start of possible match
  - Compute longest common prefix of each pair
  - We have to find two indices out of n which have same prefix nC2
    <= DN^2 where D is length of longest match

  - sort suffixes to bring repeated substrings together
  - compute longest prefix between adjacent suffixes

  Suffix Sorting: worst-case input , Suffix Arrays
  Bad input: longest repeated substring very long
  Ex: Same letter repeated N times
      Two copies of same codebase
  D = length of longest match
  LRS: Longest Repeated Substring
  Comparison is done for all smaller versions
  LRS needs atleast 1+2+3+..+D character compares
  Running Time: Quadratic(or worse) in D for LRS (also for sort)

  Linearithmetic(Manber-Myers Algorithm)
  Linear(Suffix trees)

Manber-Myers MSD algorithm overview
- Phase 0: sort on first character using key-indexed counting sort
- Phase i: Given array of suffixes sorted on first 2^i-1 characters,
  create array of suffixes sorted on first 2^i charcaters

Worst case running time: NlgN
- Finishes after lgN phases [This is because we are doubling the characters on each iteration]
- Can perform a phase in linear time

Suffix Trees and Suffix Arrays
------------------------------
- Suffix: A suffix is a substring at the end of string of characters. [Non empty]
- Suffix Array: Array which contains all the sorted suffixes of a string

where suffix started in actual string
0 camel
1 amel
2 mel
3 el
4 l

1 amel
0 camel
3 el
4 l
2 mel

The actual suffix array is the array of sorted indices
This provides a compressed representation of the sorted suffixes without actually
needing to store the suffixes

The suffix array provides a space efficient alternative to a suffix tree which itself is a
compressed version of a trie
NOTE: suffix arrays can do everything suffix trees do, with some additional information
such as Longest Common Prefix (LCP) array

LCP array: An array in which every index tracks how many characters two sorted adjacent suffixes
have in common
LCP[0] is undefined, but it could be taken as 0

Finding unique substrings
n(n+1)/2 substrings
The number of unique substrings in a string is given by:
n(n+1)/2  - Sum i = 1 to n LCP(i)
number of substrings   Duplicates 

Longest Common Substring
How to we find the longest common substring that appears in atleast 2 <= k <=n of the strings?
- Approach 1: Use dynamic programming running in O(n1*n2*n3..*nm), where ni is the length of the string Si
- Approach 2: Use the suffix array whihc can find the solution in O(n1+n2+..+nm) time

Use unique sentinels and lexicographically less than any of the characters contained in any of the strings Si
S1 = abca, S2 = bcad, S3 = daca
T = abca#bcad$daca%

- Data structures for representing the texts that allow substring queries 
  like "where does this pattern appearn in text" or "how many times does this pattern appear in text"
- Storing all suffixes of a n-character text would take O(n^2) space, so instead each suffix is represented
  by a pointer to its first character
- A suffix tree is similar, but instead using an array, we use some sort of tree data structure to hold the sorted list
- Comparison based sorting algorithm on the ste of suffixes, O(nlogn) but in worst case each comparison will take O(n)
  leading to O(n^2logn)
- Manber and Myers O(nlogn)

Least significant digit first string sort
-----------------------------------------
Consider characters from right to left
Stable sort using dth character as the key using key-indexed counting
Proposition: LSD sorts fixed-length string in ascending order
After pass i, string are sorted by last i characters


MSD String Sort
---------------
Partition array into R pieces according to first character (Use key-indexed counting)
Recursively sort all strings that start with each character (key-index counting delineate subarray to sort)

variable length string
- Treat strings as if they had extra char at end (smaller than any character)

Algorithm                Guarantee      Random		Extra Space  Stable  Operation on Keys
Insertion Sort            N^2/2		N^2/4 		1	      Yes	compareTo()
Mergesort		  NLgN		NlgN		N	      Yes	compareTo()	
quicksort		  1.39NlgN	1.39NlgN	clogN         No	compareTo()
heapsort		  2NlgN		2NlgN		1	      No 	compareTo()		
LSD			  2NW	        2NW		N+R	      Yes	charAt()
MSD			  2NW		NlogRN(R is base) N+DR	      Yes	charAt() D len of longest prefix match-fn call stack depth

Disadvantages of MSD:
- access memory randomly (cache inefficient)
- inner loop has lot of instructions
- extra space for count and aux

Disadvantages of quicksort:
- Linearithmetic number of string compares (not linear)
- Has to rescan many characters in keys with long prefix matches

3-way radix quicksort
---------------------
- Do 3-way partitioning on the dth character
- Less overhead than R way partitioning in MSD string sort
- Does not reexamine characters equal to the partitioning char
(but does reexamine chars not equal to partitioning chars)
- 2NlgN char compares on avg foir random strings [2NlgN string compares standard quicksort]
- Avoids recomparing long common prefixes [Costly for keys with longe common prefixes standard quicksort]		
