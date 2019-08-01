#!/usr/bin/perl
use strict;
use warnings;

=for comment
Question 3:
Given a string consists of different types of brackets, write a function to determine the string is
balanced. For example, &quot; ([])&quot; and &quot;[]{}&quot; are balanced but &quot;([)]&quot; and &quot;](){&quot; are not. You can assume these
are the only characters in the string: ()[]{}
=cut


sub check_balanced {
	my %brackets = (
	    "("  => 0,
	    ")"  => 0,
	    "["  => 0,
	    "]"  => 0,
	    "{"  => 0,
	    "}"  => 0,
	);

	my $instring = $_[0];
	foreach my $char (split('', $instring)) {
		$brackets{$char} ++;
	}

	my $b1 = $brackets{"("} - $brackets{")"} ;
	my $b2 = $brackets{"["} - $brackets{"]"} ;
	my $b3 = $brackets{"{"} - $brackets{"}"} ;

	if (($b1 == 0) && ($b2 == 0) && ($b3 == 0)){
		return(0); # The brackets were all balanced
	}
	else {
		return(1); # The brackets were NOT balanced
	}
}


#$checkstring="((())[]{{{}}";
my $checkstring="((()))[]{{}}";
my $result = check_balanced($checkstring);

print "Result = $result  -- 0=balanced, 1=NOT balanced\n";
