Here, as a Code Ninja, I practice the art of coding.

What isn't self explanatory has a description below. Everything else may not be that important, I just want to show the world what I've done.

#Reflector (C)
Reflector is a result of a homework from CS279 class at UCSB. The basic idea behind this program is to reflect an attackers packet to a victim through a relayer. Making the attacker believe he attacks the victim, when in reality he's attacking himself. 

The reflector "arpsoofs" the network and setup two fake nodes which is the victim and the relayer. When an attacker sends packets to the victim the program sniffs these packets and sends it back to the victim as the relayer. 

The program is in C, and not the first thing I've ever programmed in C. NB! The UDP part of this program is broken. If you want to test it, test the TCP part =) 

###External libraries
  * Libnet 1.1.4
  * libpcap 1.1.1
  
###Usage

		reflector --victim-ip VICITM-IP --victim-ethernet VICTIM-ETHERNET-ADDR --relayer-ip RELAYER-IP --relayer-ethernet RELAYER-ETHERNET-ADDR

Good luck!

#Play Spotify (Ruby)
Some simple (and buggy) Ruby program to control Spotify from the terminal.
It's also able to download Spotify-lists in json form and play those song in that sequence. 

It will probably not be compatible on other any other computer than mine. However, if you want to give it a try. It might be good to know that I'm was running Mac OS X Lion, Spotify v0.6.4, and Ruby 1.8.7 when the scripts was coded.

#ICTF 2011 Submitter Program (Python)
I programmed this with Saeed for the International Capture the Flag 2011 competition hosted by UCSB. The program was design to help us automatically submit flags and points to the judges in a intelligent fashion. The theme of the ICTF in 2011 was money laundering where we had to consider many variables too make a good decision where to launder money. 

The program has a lot of bugs in it, because it's not the final version which we forgot too pull from the virtual machines before the competition was over.

###More about the ICTF at
* http://www.independent.com/news/2011/dec/07/hackers-battle-global-spoils/
* http://ictf2011.info/

#Unfinished (maybe work on)
* parasort (python)
* pstat
