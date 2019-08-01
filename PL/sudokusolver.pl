#!/usr/bin/perl

=for comment
[ggerod@localhost PERL]$ ./sudoku.pl sudokuhard.txt 

Input:
(0)(0)(0) (0)(0)(0) (0)(0)(0)
(0)(0)(0) (0)(0)(3) (0)(8)(5)
(0)(0)(1) (0)(2)(0) (0)(0)(0)

(0)(0)(0) (5)(0)(7) (0)(0)(0)
(0)(0)(4) (0)(0)(0) (1)(0)(0)
(0)(9)(0) (0)(0)(0) (0)(0)(0)

(5)(0)(0) (0)(0)(0) (0)(7)(3)
(0)(0)(2) (0)(1)(0) (0)(0)(0)
(0)(0)(0) (0)(4)(0) (0)(0)(9)


The solved array
(9)(8)(7) (6)(5)(4) (3)(2)(1)
(2)(4)(6) (1)(7)(3) (9)(8)(5)
(3)(5)(1) (9)(2)(8) (7)(4)(6)

(1)(2)(8) (5)(3)(7) (6)(9)(4)
(6)(3)(4) (8)(9)(2) (1)(5)(7)
(7)(9)(5) (4)(6)(1) (8)(3)(2)

(5)(1)(9) (2)(8)(6) (4)(7)(3)
(4)(7)(2) (3)(1)(9) (5)(6)(8)
(8)(6)(3) (7)(4)(5) (2)(1)(9)
[ggerod@localhost PERL]$ 

  My code was rapidly hacked together,
  so there are repeats that should be put into functions,
  and it hasn't been optimized to eliminate unnecessary computations.
  If I had more time, I would have written a shorter program.

=cut

use strict;
use warnings;
use diagnostics;

open INF,"<$ARGV[0]" or die $!;

my @M=();
my $h=1;
print("\nInput:\n");
while (<INF>){
 chomp($_);
 my $w=1;
 my @entries = split(//,$_);
 foreach my $entry (@entries){
  $M[$h][$w++] = [$entry]; 
  print("(",$entry,")");
  if (($w == 4) || ($w == 7)){print(" ");}
 }
 print("\n");
 $h++;
 if (($h == 4) || ($h == 7)){print("\n");}
}


# set M[h][w] to an array starting with the section,
# followed by each possible value for that square
my $row = 0;
for (my $h=1; $h <= 9; $h++){
 if (($h == 4) || ($h == 7)){$row+=3;}
 my $col = 1;
 for (my $w=1; $w <= 9; $w++){
  if (($w == 4) || ($w == 7)){$col++;}
  my $section = ($row + $col);
  if ($M[$h][$w][0] == 0){ $M[$h][$w] = [1..9]; }
  unshift(@{ $M[$h][$w] },$section);
 }
}


#now iterate over all the squares and reduce the possible value array
#by numbers in the same section, numbers in the same row, and 
#numbers in the same column. Any time a reduction is done, start over.
my $finished=0;
until ($finished){
 my $reduced =0;
 for (my $h=1; $h <= 9; $h++){
  for (my $w=1; $w <= 9; $w++){
   $reduced += ReduceSection($h, $w);
   $reduced += ReduceRow($h,$w);
   $reduced += ReduceColumn($h,$w);
  }
 }
 $reduced += ReduceSingleCheck();
 $reduced += ReduceRowUnique();
 $reduced += ReduceColumnUnique();

 if ($reduced == 0){$finished = 1;}
}


#Now print the WHOLE array
print("\n\nThe whole array\n");
for (my $h=1; $h <= 9; $h++){
 for (my $w=1; $w <= 9; $w++){ 
  print("(",@{ $M[$h][$w] }[1..$#{ $M[$h][$w] }],")");
  if (($w == 3) || ($w == 6)){print(" ");}
 }
 print("\n");
 if (($h == 3) || ($h == 6)){print("\n");}
}



##################### subroutines
sub ReduceSection{ # if a value has been determined in that section
 my $hcheck = shift(@_);
 my $wcheck = shift(@_);
 my $reduced = 0;

 for (my $h=1; $h <= 9; $h++){
  for (my $w=1; $w <= 9; $w++){
   if (($h != $hcheck) && ($w != $wcheck)){ # don't check against itself
    if($M[$h][$w][0] == $M[$hcheck][$wcheck][0]){ #same section
     if($#{ $M[$h][$w] } == 1){ #value has been determined
      if ( grep {$_ == $M[$h][$w][1]} @{ $M[$hcheck][$wcheck] }[1..$#{ $M[$hcheck][$wcheck] }] ){
       for (my $i = 1; $i <= $#{ $M[$hcheck][$wcheck] }; $i++){
        if ($M[$hcheck][$wcheck][$i] == $M[$h][$w][1]){
         splice (@{ $M[$hcheck][$wcheck] }, $i, 1);
        }
       }
       $reduced = 1;
      }
     }
    }
   }
  }
 }
 return($reduced);
}

sub ReduceRow{ # if a value has been determined in that row
 my $hcheck = shift(@_);
 my $wcheck = shift(@_);
 my $reduced = 0;

 for (my $w=1; $w <= 9; $w++){
  if ($w != $wcheck){ # don't check against itself
   if($#{ $M[$hcheck][$w] } == 1){ #value has been determined
    if ( grep {$_ == $M[$hcheck][$w][1]} @{ $M[$hcheck][$wcheck] }[1..$#{ $M[$hcheck][$wcheck] }] ){
     for (my $i = 1; $i <= $#{ $M[$hcheck][$wcheck] }; $i++){
      if ($M[$hcheck][$wcheck][$i] == $M[$hcheck][$w][1]){
       splice (@{ $M[$hcheck][$wcheck] }, $i, 1);
      }
     }
     $reduced = 1;
    }
   }
  }
 }
 return($reduced);
}

sub ReduceColumn{ # if a value has been determined in that column
 my $hcheck = shift(@_);
 my $wcheck = shift(@_);
 my $reduced = 0;

 for (my $h=1; $h <= 9; $h++){
  if ($h != $hcheck){ # don't check against itself
   if($#{ $M[$h][$wcheck] } == 1){ #value has been determined
    if ( grep {$_ == $M[$h][$wcheck][1]} @{ $M[$hcheck][$wcheck] }[1..$#{ $M[$hcheck][$wcheck] }] ){
     for (my $i = 1; $i <= $#{ $M[$hcheck][$wcheck] }; $i++){
      if ($M[$hcheck][$wcheck][$i] == $M[$h][$wcheck][1]){
       splice (@{ $M[$hcheck][$wcheck] }, $i, 1);
      }
     }
     $reduced = 1;
    }
   }
  }
 }
 return($reduced);
}

sub ReduceSingleCheck{ #check sections value possibility sets for any that only occur in a single square
 my $reduced = 0;

 my @EC=();
 for (my $h=1; $h <= 9; $h++){
  for (my $w=1; $w <= 9; $w++){
   foreach my $element (@{ $M[$h][$w] }[1..$#{ $M[$h][$w] }]){
    if (! defined($EC[$M[$h][$w][0]][$element])){$EC[$M[$h][$w][0]][$element]=0;}
    $EC[$M[$h][$w][0]][$element]++;
   }
  }
 }

 for (my $sec=1; $sec <= 9; $sec++){
  for (my $index=1; $index <= 9; $index++){
   if ($EC[$sec][$index] == 1){
    for (my $h=1; $h <= 9; $h++){
     for (my $w=1; $w <= 9; $w++){
      if (($M[$h][$w][0] == $sec) && ($#{ $M[$h][$w] } != 1) && ( grep {$_ == $index} @{ $M[$h][$w] }[1..$#{ $M[$h][$w] }] )){
       @{ $M[$h][$w] } = ($sec,$index);
       $reduced = 1;
      }
     }
    }
   }
  }
 }
 return($reduced);
}


sub ReduceRowUnique{ #check row value possibility sets for any values that only occur in a single square
 my $reduced = 0;

 my @EC=();
 for (my $h=1; $h <= 9; $h++){
  for (my $w=1; $w <= 9; $w++){
   foreach my $element (@{ $M[$h][$w] }[1..$#{ $M[$h][$w] }]){
    if (! defined($EC[$h][$element])){$EC[$h][$element]=0;}
    $EC[$h][$element]++;
   }
  }
 }

 for (my $h=1; $h <= 9; $h++){
  for (my $index=1; $index <= 9; $index++){
   if ($EC[$h][$index] == 1){
    for (my $w=1; $w <= 9; $w++){
     if (($#{ $M[$h][$w] } != 1) && ( grep {$_ == $index} @{ $M[$h][$w] }[1..$#{ $M[$h][$w] }] )){
       @{ $M[$h][$w] } = ($M[$h][$w][0],$index);
       $reduced = 1;
     }
    }
   }
  }
 }
 return($reduced);
}


sub ReduceColumnUnique{ #check column value possibility sets for any values that only occur in a single square
 my $reduced = 0;

 my @EC=();
 for (my $h=1; $h <= 9; $h++){
  for (my $w=1; $w <= 9; $w++){
   foreach my $element (@{ $M[$h][$w] }[1..$#{ $M[$h][$w] }]){
    if (! defined($EC[$w][$element])){$EC[$w][$element]=0;}
    $EC[$w][$element]++;
   }
  }
 }

 for (my $w=1; $w <= 9; $w++){
  for (my $index=1; $index <= 9; $index++){
   if ($EC[$w][$index] == 1){
    for (my $h=1; $h <= 9; $h++){
     if (($#{ $M[$h][$w] } != 1) && ( grep {$_ == $index} @{ $M[$h][$w] }[1..$#{ $M[$h][$w] }] )){
       @{ $M[$h][$w] } = ($M[$h][$w][0],$index);
       $reduced = 1;
     }
    }
   }
  }
 }
 return($reduced);
}
