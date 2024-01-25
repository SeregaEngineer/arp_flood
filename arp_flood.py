from scapy.all import *
from randmac import RandMac
import time


                                                              
for i in range(10,200):
    mac = str(RandMac())
    mac2 = str(RandMac())
   #сеть должна быть такой же на какой сидит arpwatch иначе он в богон кидает
    ip_src = f'192.168.100.{i}'#.format(*__import__('random').sample(range(0,255),1))
    ip_dst = f'192.168.100.{i+1}'#.format(*__import__('random').sample(range(0,255),1))

    pkt=Ether(dst="FF:FF:FF:FF:FF:FF", src=mac)/ARP(
                                    pdst=ip_dst, 
                                    psrc=ip_src,
                                    hwsrc=mac
                                    #hwdst=mac2

                   )
    
    sendp(pkt)
    time.sleep(1)

