#!/usr/bin/perl

use strict;

my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
	print("Case #",$case,": ");
	my @words=split(' ',<>);
	my @revwords = reverse (@words);
	print join(" ", @revwords);
	print ("\n");
