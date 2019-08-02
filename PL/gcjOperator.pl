#!/usr/bin/perl

use strict;
use warnings;


=for comment
Problem 
The Never Breaking Down Company has been operating a phone call center to quickly resolve small issues with their products and services. This turned out to be a great success, issues are being resolved quickly and effectively to the maximum satisfaction of the customers. However, running the call center is too expensive, because of the huge salaries the company has to pay to the call center operators. So the company has decided to downsize, and it's your task to figure out how many operators must be kept.
You have access to the call logs. For each call you know when it started and how long it took. Write a program which figures out the maximum number of operators busy at the same time. Two calls overlap if both of them are active at the same time for at least a minute.
For example, if there are two calls: one of them started at 3 (minutes after the opening time) and took 4 minutes, the other one started at 5 minutes and took 6 minutes, then the answer is 2, because 2 operators were busy in the busiest period, i.e. between 5 and 7 minutes.

This is the classic "software licenses" or other maximum use of a resource at a given time problem.
I first tried a recursive solution which would take an input set of calls, find any overlaps to each call, and generate a new set of calls out of the overlaps, then recurse.  The deeper it recurses, the more overlapping calls, so just count the deepest recursion level.  This worked on "normal" data, but would choke if the number of overlaps exceeded 10,000 due to recursion inefficiency.
A much easier solution to this classic problem is to sort the call events (start or stop) by time, then loop over the data incrementing a count variable for each start time and decrementing for each stop time.  Keep track of the maximum that variable attains.
Elapsed run time for the dataset = 3.483s
=cut


my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
 print("Case #",$case,": ");

 my @inputline=split(' ',<>);
 my $numcalls = shift(@inputline);
 my @C;
 my $maxolap = 0;
 my $olap = 0;

 for(my $i = 0; $i <= (($numcalls-1) * 2); $i+=2){
  my $start = shift(@inputline);
  my $duration = shift(@inputline);
  $C[$i][0] = $start;
  $C[$i][1] = 1;
  $C[($i + 1)][0] = ($start + $duration);
  $C[($i + 1)][1] = 0;
 }

 my @sortedC = sort {
  $a->[0] <=> $b->[0] 
   ||
  $a->[1] <=> $b->[1] 
 } @C;

 #now loop through and increment for each 1 index and decrement for each 0 index.  Find max count
 for(my $i = 0; $i <= $#sortedC; $i++){
  if ($sortedC[$i][1] == 0){ $olap--; }
  else { $olap++; }

  if ($olap > $maxolap) { $maxolap = $olap; }
 }

 print ($maxolap,"\n");

} #end case loop

