#!/usr/bin/perl

=for comment
Question 2:
Write a Perl program to create an associative array (&quot;hash&quot;) named &quot;last_name&quot; 
whose keys are the five first names &quot;Mary&quot;, &quot;James&quot;, &quot;Thomas&quot;, &quot;William&quot;, &quot;Elizabeth&quot;. 
Set the corresponding values for these keys to be &quot;Li&quot;, &quot;O&#39;Day&quot;, &quot;Miller&quot;, &quot;Garcia&quot;, &quot;Davis&quot;. 
Then print out the five full names, each on its own line, sorted primarily by length of last name 
and with a secondary sort alphabetically by first name. 
=cut


my %last_name = (
    Mary  => "Li",
    James => "O'Day",
    Thomas  => "Miller",
    William  => "Garcia",
    Elizabeth  => "Davis",
);

my @keys = sort { length $last_name{$b} <=> length $last_name{$a} or $a cmp $b } keys(%last_name);

foreach my $key ( @keys ) {
    print "$key $last_name{$key}\n";
}
