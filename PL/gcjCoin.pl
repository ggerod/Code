#!/usr/bin/perl

use strict;
use warnings;
use diagnostics;


=for comment
Problem
The Anti Technology Party has designed a monetary reform: all payments are to be restricted to coins only (no banknotes, no credit cards etc.). The only question remaining is what the relative values of coins should be. There are many proposals, and it's your task to figure out for each proposal whether all integer amounts can be paid with the coins in the proposal, provided that everybody carries enough change. For example, if the coins are worth 2 and 3, everything can be paid: we can pay 1 by paying 3 and getting back 2 as change, we can pay 4 by paying 2 plus 2 etc.

This is an easier form of the Froebenius problem in which we want to check if the Froebenius number is undefined for our set.  In addition, we are allowed to add to our set by "giving change", and this is a huge difference from the classic problem.   The modulus of any given pair of numbers from our set can be added to our set.  
Any modulus that equals 1 means we can form any number, and the solution is possible.  If our set contains the number 1 initially, we can likewise form any integer amount.
  If we have only one number in the set (and it isn't the number one), then we cannot make modulus change, and cannot form every integer.  
  If all numbers in the set are even, then any modulus of those numbers will also be even, so we will not be able to create any negative integer from the set, and the set fails the test.
  Keep in mind from number theory the fundamental theorem of arithmetic  which states that any integer greater than 1 can be expressed as a product of primes. With any two primes in our set, we will be able to meet the problem requirement.
  My solution starts with the smallest numbers in the set, and iterates through successive modulus values, adding the final non-zero modulus to the set if it isn't already in there.  It then also reduces the set size by removing all multiples of that last modulus value, which will reduce the number of operations as we iterate.
  Note the use of the Perl smart matching operator (~~), available since Perl 5.10 in late 2007, equivalent to Python's 'in' operator.
Elapsed run time for the dataset = 0.780s
=cut


my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
 print("Case #",$case,": ");

 my @inputline=split(' ',<>);
 my $numcoins = shift(@inputline);
 my @C;

 for(my $i = 0; $i < $numcoins; $i++){
  $C[$i] = shift(@inputline);
 }

 my $possible=0;
 my $added = 1;
 my @odds = grep($_ % 2 != 0, @C);
 my $odds = @odds;
 if ($odds == 0){ $possible = 0; $added = 0; }

CHECK: while ($added){
  $added = 0;

  if (1 ~~ @C){ $possible = 1; last CHECK; }
  if ($#C == 0){ $possible = 0; last CHECK; }

  @C = sort { $b <=> $a } @C;
  
  my $modval;
  for(my $i = ($#C - 1); $i >= 0; $i--){
   for(my $j = ($i + 1); $j <= $#C; $j++){
    my $a = $C[$i];
    my $b = $C[$j];
    while($b != 0){
     $modval = ($a % $b);

     if ($modval == 1){ $possible = 1; last CHECK;}
     if ($modval == 0){ 
      #reduce it
      @C = grep($_ % $b != 0, @C); 

      if (!($b ~~ @C)){
       push (@C, $b); 
       $added = 1;
       next CHECK;
      }
     }
     $a = $b;
     $b = $modval;
    }
   }
  }
 }

 if ($possible == 1){ print("possible\n"); }
 else { print("impossible\n"); }

} #end case loop
