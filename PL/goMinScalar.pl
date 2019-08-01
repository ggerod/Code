#!/usr/bin/perl

use strict;

my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
	print("Case #",$case,": ");

	my $setindex=-1;
	my $vectorlen=<>;
	my @v1=split(' ',<>);
	my @v2=split(' ',<>);
	my @sv1 = sort { $a <=> $b } @v1;
	my @sv2 = sort { $b <=> $a } @v2;

	my $vectorprod = 0;

	for (my $workindex=0; $workindex <= ($vectorlen-1); $workindex++) {
		$vectorprod+=($sv1[$workindex] * $sv2[$workindex]);
	}

	print($vectorprod);
	print("\n");
}
