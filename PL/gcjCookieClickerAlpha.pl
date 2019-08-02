#!/usr/bin/perl

use strict;
use warnings;

=for comment
Problem
In this problem, you start with 0 cookies. You gain cookies at a rate of 2 cookies per second, by clicking on a giant cookie. Any time you have at least C cookies, you can buy a cookie farm. Every time you buy a cookie farm, it costs you C cookies and gives you an extra F cookies per second.
Once you have X cookies that you haven't spent on farms, you win! Figure out how long it will take you to win if you use the best possible strategy.


This problem was just a matter of figuring out the strategy, and programming that into the solution algorithm.  I didn't even have to use Math::Bigfloat to attain an absolute or relative error of 10^-6 (today was a good day).
Elapsed time for the large dataset = 0.288s
=cut


my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
 print("Case #",$case,": ");

 my $RATE = 2;
 my $TotalTime = 0;
 my $fTotalTime = 0;
 (my $Cost, my $FRate, my $XGoal)=split(' ',<>);

 my $Keepchecking =1;
 while ($Keepchecking){
  if ($Cost >= $XGoal){
   #just calc the time to goal and exit
   $TotalTime += ($XGoal / $RATE);
   $Keepchecking = 0;
   last;
  }

  $TotalTime += ($Cost / $RATE);

  my $Tnobuy = (($XGoal - $Cost)/$RATE);
  my $Tbuy = ($XGoal / ($RATE + $FRate));

  if ($Tnobuy <= $Tbuy){
   $Keepchecking = 0;
   $TotalTime += $Tnobuy;
  }
  else { $RATE += $FRate; }
 }

 $fTotalTime = sprintf("%.7f",$TotalTime);
 print($fTotalTime,"\n");
}
