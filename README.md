Here, as a Code Ninja, I practice the art of coding.

What isn't self explanatory has a description below. Everything else may not be that important, I just want to show the world what I've done.

#Reflector
Reflector is a result of a homework from CS279 class at UCSB. The basic idea behind this program is to reflect an attackers packet to a victim through a relayer. Making the attacker believe he attacks the victim, when in reality he's attacking himself. 

The reflector "arpsoofs" the network and setup two fake nodes which is the victim and the relayer. When an attacker sends packets to the victim the program sniffs these packets and sends it back to the victim as the relayer. 

###External libraries
  * Libnet 1.1.4
  * libpcap 1.1.1
  
###Usage
reflector --victim-ip VICITM-IP --victim-ethernet VICTIM-ETHERNET-ADDR --relayer-ip RELAYER-IP --relayer-ethernet RELAYER-ETHERNET-ADDR

Good luck!