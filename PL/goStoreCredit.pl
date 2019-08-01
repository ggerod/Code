#!/usr/bin/perl

use strict;

my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
	print("Case #",$case,": ");
	my $credit=<>;
	my $numitems=<>;
	my @prices=split(' ',<>);
	for (my $firstindex=0; $firstindex <= ($numitems-2); $firstindex++) {
		if ($prices[$firstindex] >= $credit) { next; }
		for (my $secondindex=($firstindex+1); $secondindex <= ($numitems-1); $secondindex++) {
			if (($prices[$firstindex] + $prices[$secondindex]) == $credit){
				print(($firstindex+1)," ",($secondindex+1),"\n");
				last;
			}
		}
	}
}
