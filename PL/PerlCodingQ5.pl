#!/usr/bin/perl
use strict;
use warnings;


=for comment
Question 5:
Suppose we want to preprocess JSON strings to strip out C style line comments. An example might look
like this:
// this is a comment
{ // another comment
true, &quot;foo&quot;, // 3rd comment
&quot;http://www.ariba.com&quot; // comment after URL
}
Write a function to strip line comments without using regular expressions. Think about the other corner
cases.
=cut


sub strip_comments {
	my $charm1='';
	my $charm2='';
	my $instring = $_[0];
	foreach my $char (split('', $instring)) {
		if (($char eq "/" ) && ($charm1 eq "/") && (($charm2 eq " ") || ($charm2 eq ''))){
			print "\n";
			return();
		}
		else {
			print $charm2;
			$charm2 = $charm1;
			$charm1 = $char;
		}
	}
	#print rest
	print "$charm2";
	print "$charm1";
}


my $filename = $ARGV[0];
open(my $fh, '<:encoding(UTF-8)', $filename)
  or die "Could not open file '$filename' $!";

while (my $row = <$fh>) {
  strip_comments($row)
}
