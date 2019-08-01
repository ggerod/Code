#!/usr/bin/perl

=for comment
Password generator for brute force attacks

   Here is a simple program for generating every permutation of (k) characters given set of (n) characters to choose from.  The output can be piped into brute force attack programs such as Aircrack-ng's airodump-ng when cracking WPA and WPA2.   If you have the disk space, the outuput can be saved in various dictionaries of different character sets and string lengths.

Keep in mind that the number of permutations will grow exponentially with respect to the number of characters in the password strings you are generating.  

Number of permutations = nk

This with k being the string/password length, so typically from 4 to 10 characters long.  (8 to 63 printable ASCII characters for WPA/WPA2)

n will be all lowercase letters (26), uppercase letters (26), numeric digits (10), special characters (varies, depending on which you want to add in, but could be 32 just using the keys on a typical US keyboard).  So, to be fairly complete, n=94.  I've run mine with a reduced set and n=73.

This can take some time, but with luck you will get a match early in the process.  Each digit we add to the password length multiplies the permutations by 73, so it will take 73 times longer to generate all the permutations than the previous length.

73^4 = 28,398,241
73^5 = 2,073,071,593
73^6 = 151,334,226,289
73^7 = 11,047,398,519,097
73^8 = 806,460,091,894,081
73^9 = 58,871,586,708,267,913
73^10 = 4,297,625,829,703,557,649


On an extremely under-powered raspberry pi, the four character set completed in 183m22.769s.  
On the XPS9000 using a single core it took 6m6.487s
Extrapolating for the XPS:
5 characters would take 7.3 hours
6 characters would take 22.2 days
7 characters would take 4.4 years

A nice chart from 2009 at: lockdown.co.uk

This is intractable by design.  Brute force is not supposed to be feasible.  The process can be sped up greatly by using tools such as oclHashcat to take advantage of screaming fast GPU's, and also intelligent password generation rather than brute force.  Brute forcing 8 characters with a full character set AND hashing takes oclHashcat 25 days with my old AMD Radeon HD 5870.  This is a huge improvement, but still takes too long, and if you expand to 9 character passwords, you are looking at 6.6 years. 

Using dictionary lists can save a lot of time, but they typically won't use mixed case or special characters.  Weak passwords do exist in the wild, but you can waste a lot of time if you underestimate the difficulty at the outset.  
If you already have the hash(es) you are trying to crack, pre-computed rainbow tables reduce the time to a simple lookup among quadrillions of entries rather than any computational work.  Of course, any system that adds salt to the hashes will defeat rainbow tables.  Microsoft in their wisdom (to be fair, it was due to backward compatibility) do not use salt, so their hashes are very easily cracked with rainbow tables.

New code and updates to follow.
=cut

my @chars=(a..z,A..Z,0..9,"!","@","#",'$',"%","^","&","*","-","+","=");

my $numchars=4;
our @I=();
for (my $i = 0; $i < $numchars; $i++){ $I[$i] = 0; }

my $updated;
my $windex;
while(1){
        $updated=0;
        $windex=($numchars - 1);

        for (my $i = 0; $i < $numchars; $i++){
                print($chars[$I[$i]]);
                #print($I[$i]," ");
        }
        print("\n");

        until ($updated){
                if( $I[$windex]++ >= $#chars){
                        if ($windex == 0){exit 0;}
                        $windex--;
                }
                else {
                        until ($windex >= $numchars){
                                $windex++;
                                $I[$windex] = 0;
                        }
                        $updated = 1;
                }
        }
}
