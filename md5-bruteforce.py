#usr/bin/python2.7
import time
import itertools, string
import hashlib
import sys

import threading
from threading import Thread
info = """
  Name            : Python Md5 Brute-force
  Created By      : Sefa Said Deniz
  Blog            : sefasaiddeniz.com
  Documentation   : https://github.com/sefasaid/python-md5-bruteforce/
  License         : Completely Free
  Thanks to       :  Agus Makmun (Summon Agus)-bloggersmart.net - python.web.id
"""

def _attack(chrs, inputt):
    print "[+] Start Time: ", time.strftime('%H:%M:%S')
    start_time = time.time()
   
    for n in range(1, 31+1):
      for xs in itertools.product(chrs, repeat=n):
          
          saved = ''.join(xs)
          stringg = saved
          m = hashlib.md5()
          m.update(saved)
         
          if m.hexdigest() == inputt:
             
             
              print "\n[!] found ", stringg
             
              print "\n[-] End Time: ", time.strftime('%H:%M:%S')
              print("\n--- %s seconds ---" % (time.time() - start_time))
              sys.exit("Thank You !")
   


def main():
    print info
    inp_usr = raw_input(" add md5\n")
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    return _attack( chrs,inp_usr );

   

if __name__ == "__main__":
    main()
   
   
   
