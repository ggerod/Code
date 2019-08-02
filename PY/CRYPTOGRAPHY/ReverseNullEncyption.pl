#!/usr/bin/perl
use strict;
use warnings;

#get string to embed
my $embedtextfile = $ARGV[0];

#get base text to embed into
my $basetextfile = $ARGV[1];

#get starting offset
my $offset = $ARGV[2];

#open filehandles on the two files
open EMBD, "<$embedtextfile" or die $!;
open BASE, "<$basetextfile" or die $!;
local $/ = ' '; #read word by word

#make sure to start at the offset from the first word
for(my $i=1; $i<$offset; $i++){my $baseword = ;}

my $pattern = "";
#iterate over the embed text and generate the acrostic code from the embed text
while (my $embedword = <EMBD>){
 my @embedchars = split(//, lc($embedword));
 foreach my $embedchar (@embedchars){
  #read each word from the base text.  For each word, check if char
  #is contained in the word.  if yes, print index num. else print 0
  my $foundmatch=0;
  if($embedchar =~ /\s/){$pattern .= "-1,"; $foundmatch = 1;}
  while ($foundmatch == 0){
   my $baseword = <BASE>;
   my @basechars = split(//, lc($baseword));
   for (my $i = 0; $i <= $#basechars; $i++){
    if ($basechars[$i] eq $embedchar){
     $pattern .= ((++$i).",");
     $foundmatch = 1;
     last;
    }
   }
   if (! $foundmatch){$pattern .= "0,";}
  }
 }
}

my @patchars = split (/\,/, $pattern);
my @pat2chars=();

my $zeros=0;
for (my $i = 0; $i <= $#patchars; $i++){
 if ($patchars[$i] == 0){$zeros++; }
 elsif ($zeros){ 
  push(@pat2chars, ($zeros, 0));
  $zeros = 0; 
  if ($patchars[$i] == -1){ push(@pat2chars, (0, 0)); }
  else {push(@pat2chars, $patchars[$i]); }
 }
 else {
  if ($patchars[$i] == -1){ push(@pat2chars, (0, 0)); }
  else{ push(@pat2chars, $patchars[$i]); }
 }
}
if($pat2chars[$#pat2chars] == 0){pop(@pat2chars);pop(@pat2chars);}

my $codeoutput = join(',', @pat2chars);

print($codeoutput,"\n");
