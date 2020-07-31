# all-prime-numbers-upto-given-number
This is the efficient way to find out all the prime nummbers that are less than or equal to a given no.

This method is known as-Sieve of Eratosthenes and Segmented Sieve

About the Method--

Sieve of Eratosthenes-Time Complexity O(n log long ): It is an ancient algorithm for finding the prime numbers up to the given limit by the following steps:

  1.  Mark the smallest number that is not already visited or checked
  2.  Cross out all the multiples of a number you marked in step 1 except the marked number itself
  3.  You’ve to repeat step 1 and 2 until every number on the table/grid is either visited or crossed out.

Once completed, the marked numbers with which you are left are the primes.


Segmented Sieve: It follows from the optimisation “sieving till root”. The basic idea of a segmented sieve is to choose the sieving primes less 
than the square root of n, choose a reasonably large segment size that nevertheless fits in memory, and then sieve each of the segments, in turn, 
starting with the smallest. At the first segment, the smallest multiple of each sieving prime that is within the segment is calculated, then multiples 
of the sieving prime are marked as a composite in the normal way; when all the sieving primes have been used, the remaining unmarked numbers in the 
segment are prime. Then, for the next segment, for each sieving prime, you already know the first multiple in the current segment (it was the multiple 
that ended the sieving for that prime in the prior segment), so you sieve on each sieving prime and so on until you are finished.
