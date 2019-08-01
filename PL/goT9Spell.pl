#!/usr/bin/perl

use strict;

my %keymap=();

$keymap{'a'} = 2;
$keymap{'b'} = 22;
$keymap{'c'} = 222;
$keymap{'d'} = 3;
$keymap{'e'} = 33;
$keymap{'f'} = 333;
$keymap{'g'} = 4;
$keymap{'h'} = 44;
$keymap{'i'} = 444;
$keymap{'j'} = 5;
$keymap{'k'} = 55;
$keymap{'l'} = 555;
$keymap{'m'} = 6;
$keymap{'n'} = 66;
$keymap{'o'} = 666;
$keymap{'p'} = 7;
$keymap{'q'} = 77;
$keymap{'r'} = 777;
$keymap{'s'} = 7777;
$keymap{'t'} = 8;
$keymap{'u'} = 88;
$keymap{'v'} = 888;
$keymap{'w'} = 9;
$keymap{'x'} = 99;
$keymap{'y'} = 999;
$keymap{'z'} = 9999;
$keymap{' '} = 0;

my $prevnum="-3";

my $numcases = <>;
for (my $case=1; $case <= $numcases; $case++) {
	print("Case #",$case,": ");
	my @chars=split('',<>);
	foreach my $char (@chars){
		#print ($char);
		my $currnum =  substr $keymap{$char}, 0, 1;
		#print $currnum;
		if ($currnum == $prevnum){
			print(" ");
		}
		print $keymap{$char};
		$prevnum=$currnum;
	}
	#print $keymap{' '};
	print ("\n");
}
