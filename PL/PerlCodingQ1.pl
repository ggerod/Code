#!/usr/bin/perl

=for comment
Question 1:
Write code to generate the following histogram display based on the frequency of occurrence of
characters in the first argument to the program. Example:
   $ perl histogram.pl &quot;Mississippi borders Tennessee.&quot;
   s: #######
   e: #####
   i: ####
    : ##
   n: ##
   p: ##
   r: ##
   .: #
   M: #
   T: #
   b: #
   d: #
   o: #
=cut


#   $ perl histogram.pl "Mississippi borders Tennessee."
my %charhash;
$instring = $ARGV[0];

foreach $char (split('', $instring)) {
  $charhash{$char} += 1;
}

my @keys = sort { $charhash{$b} <=> $charhash{$a} } keys(%charhash);

foreach my $key ( @keys ) {
    #print "$key, $charhash{$key}\n";
    print "$key: ";
    for (my $i=0; $i < $charhash{$key} ; $i++) {
	print "#";
    }
    print "\n";
}
