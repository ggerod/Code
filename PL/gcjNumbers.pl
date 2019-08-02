#!/usr/bin/perl
use strict;
use warnings;


=for comment
Problem
In this problem, you have to find the last three digits before the decimal point for the number (3 + √5)n.
For example, when n = 5, (3 + √5)5 = 3935.73982... The answer is 935.
For n = 2, (3 + √5)2 = 27.4164079... The answer is 027.
Elapsed time for large dataset = 0.056s
Here is my coded solution ==>
=cut


my $numcases = <>;

sub matrix_mult {
 my @locA = @{$_[0]};
 my @locB = @{$_[1]};
 my @C;
 $C[0][0]=0;
 $C[0][1]=0;
 $C[1][0]=0;
 $C[1][1]=0;

 for (my $i=0; $i <= 1; $i++) {
  for (my $j=0; $j <= 1; $j++) {
   for (my $k=0; $k <= 1; $k++) {
    $C[$i][$k] = ($C[$i][$k] + $locA[$i][$j] * $locB[$j][$k]) % 1000;
   }
  }
 }
 return(\@C);
}

sub fast_exponentiation {
 my $locexplev = shift(@_);
 my @locmatrix = @{$_[0]};

 if ($locexplev ==1){
  return(\@locmatrix);
 }
 elsif ($locexplev % 2 == 0){
  my $locmatA1 = fast_exponentiation(($locexplev/2),\@locmatrix);
  my @locmatA1 = @$locmatA1;
  my $locA1sq = matrix_mult(\@locmatA1, \@locmatA1);
  my @locA1sq = @$locA1sq;
  return(\@locA1sq);
 }
 else {
  return(matrix_mult(\@locmatrix, fast_exponentiation($locexplev-1,\@locmatrix)));
 }
}

for (my $case=1; $case <= $numcases; $case++) {
 my @matrix;
 $matrix[0][0]=3;
 $matrix[0][1]=5;
 $matrix[1][0]=1;
 $matrix[1][1]=3;

 print("Case #",$case,": ");

 my $exponentlev = <>;
 chomp($exponentlev);

 my $mat_n = fast_exponentiation($exponentlev,\@matrix);
 my @mat_n = @$mat_n;

 my $answer = ((2 * $mat_n[0][0]) + 999) % 1000;

 $answer = "0" . $answer while length($answer) < 3 ;

 print($answer);
 print("\n");
}
