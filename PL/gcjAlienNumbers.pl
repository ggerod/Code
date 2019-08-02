#!/usr/bin/perl

use strict;
use warnings;


=for comment
Problem
The decimal numeral system is composed of ten digits, which we represent as "0123456789" (the digits in a system are written from lowest to highest). Imagine you have discovered an alien numeral system composed of some number of digits, which may or may not be the same as those used in decimal. For example, if the alien numeral system were represented as "oF8", then the numbers one through ten would be (F, 8, Fo, FF, F8, 8o, 8F, 88, Foo, FoF). We would like to be able to work with numbers in arbitrary alien systems. More generally, we want to be able to convert an arbitrary number that's written in one alien system into a second alien system.
The description on this one left a lot to be desired, and I think that was intentional on the part of the challenge creator.  I understood what they meant because I've always been interested in different base number systems, and the symbols used to describe numbers.  
So really, all this challenge requires is to convert a base-x number with x arbitrary number symbols to a base-y number with y arbitrary number symbols.
Elapsed time for large dataset = 0.013s
=cut


chomp(my $numcases = <>);

for (my $case=1; $case <= $numcases; $case++) {
        print("Case #",$case,": ");

        (my $an, my $sl, my $tl) = split / /, <>;
        chomp $tl;
        my @andigits = split //, $an;
        my @ssymb = split //, $sl;
        my @tsymb = split //, $tl;
        my $base10an;
        my %smap = ();
        my %tmap = ();

        for (my $digit = 0; $digit <= $#ssymb; $digit++){
                $smap{"$ssymb[$digit]"} = $digit
        }

        for (my $digit = 0; $digit <= $#tsymb; $digit++){
                $tmap{"$tsymb[$digit]"} = $digit
        }

        my $power = 0;
        for (my $digit = $#andigits; $digit >=0; $digit--){
                $base10an += $smap{$andigits[$digit]} * ( ($#ssymb +1) ** $power++ )
        }
        #print ("the base 10 representation of the source number is: ",$base10an,"\n");

        #now convert to new base
        my $i=0;
        my $j=0;
        my $k=0;
        while ($base10an >= (($#tsymb + 1) ** $i)){ $i++; }
        for ( $j=($i - 1); $j>=0; $j-=1){ #this many digits
                my $subnum = (($#tsymb + 1) ** $j);
                for ( $k = $#tsymb; $k>=0; $k--){ #find the right multiplier
                        if (($k * $subnum) <= $base10an){
                                $base10an -= ($k * $subnum);
                                print($tsymb[$k]);
                                last;
                        }
                }
        }
        print("\n");
} #CASE

