Here, as a Code Ninja, I practice the art of coding.

What isn't self explanatory has a description below. Everything else may not be that important, I just want to show the world what I've done.

#Reflector
Reflector is a result of a homework from CS279 class at UCSB. The basic idea behind this program is to reflect an attackers packet to a victim through a relayer. Making the attacker believe he attacks the victim, when in reality he's attacking himself. 

The reflector "arpsoofs" the network and setup two fake nodes which is the victim and the relayer. When an attacker sends packets to the victim the program sniffs these packets and sends it back to the victim as the relayer. 

The program is in C, and not the first thing I've ever programmed in C. NB! The UDP part of this program is broken. If you want to test it, test the TCP part =) 

###External libraries
  * Libnet 1.1.4
  * libpcap 1.1.1
  
###Usage
reflector --victim-ip VICITM-IP --victim-ethernet VICTIM-ETHERNET-ADDR --relayer-ip RELAYER-IP --relayer-ethernet RELAYER-ETHERNET-ADDR

Good luck!

#Play Spotify
Some simple (and buggy) Ruby program to control Spotify from the terminal.
It's also able to download Spotify-lists in json form and play those song in that sequence. 

It will probably not be compatible on other any other computer than mine. However, if you want to give it a try. It might be good to know that I'm was running Mac OS X Lion, Spotify v0.6.4, and Ruby 1.8.7 when the scripts was coded.