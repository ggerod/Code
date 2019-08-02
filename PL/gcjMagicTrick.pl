#!/usr/bin/perl

use strict;
use warnings;


=for comment
Problem
Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!
The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.
Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?
You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.
Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).

This problem was fairly simple.  The coding was optimized to store as little information as possible.  The Perl 'grep' function was put to good use to avoid an extra loop.
Elapsed time for the dataset = 0.036s
=cut


my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
 print("Case #",$case,": ");

 my $pick1=<>;
 my @a1;
 for (my $i = 1; $i <=4; $i++){
  my @temp = split(' ',<>);
  if ($i == $pick1){@a1 = @temp;}
 }

 my $pick2=<>;
 my @a2;
 for (my $i = 1; $i <=4; $i++){
  my @temp = split(' ',<>);
  if ($i == $pick2){@a2 = @temp;}
 }

 my $matches = 0;
 my $matchnum;

 for (my $i = 0; $i <=3; $i++){
  if (grep {$_ == $a1[$i]} @a2){$matches++;$matchnum = $a1[$i];}
  if ($matches > 1){print("Bad magician!\n"); last;}
 }

 if ($matches == 0){print("Volunteer cheated!\n");}
 elsif ($matches ==1) {print($matchnum,"\n");}
}
