#!/usr/bin/perl
use strict;


=for comment
Problem
You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.
Suppose you are allowed to permute the coordinates of each vector as you wish. Choose two permutations such that the scalar product of your two new vectors is the smallest possible, and output that minimum scalar product.

This one turned out to be fairly simple after you think how to mathematically ensure the lowest resulting value.
Elapsed time for large dataset = 0.016s
=cut


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
