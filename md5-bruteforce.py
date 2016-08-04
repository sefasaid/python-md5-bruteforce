#usr/bin/python2.7
import time
import itertools, string
import hashlib
import sys

import threading

info = """
  Name            : Python Md5 Brute-force
  Created By      : Sefa Said Deniz
  Blog            : sefasaiddeniz.com
  Documentation   : https://github.com/sefasaid/python-md5-bruteforce/
  License         : Completely Free
  Thanks to       :  Agus Makmun (Summon Agus)-bloggersmart.net - python.web.id
"""
done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done==True:
            break
            
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')


def _attack(chrs, inputt):
    print "[+] Start Time: ", time.strftime('%H:%M:%S')
    start_time = time.time()
    t = threading.Thread(target=animate)
    t.start()
    for n in range(1, 31+1):
      characterstart_time = time.time()
      print "\n[!] I'm at ", n , "-character"
     
      
      for xs in itertools.product(chrs, repeat=n):

          saved = ''.join(xs)
          stringg = saved
          m = hashlib.md5()
          m.update(saved)
         
          if m.hexdigest() == inputt:
              time.sleep(10)
              global done
              done = True

              print "\n[!] found ", stringg
             
              print "\n[-] End Time: ", time.strftime('%H:%M:%S')
              print("\n--- %s seconds ---" % (time.time() - start_time))
              sys.exit("Thank You !")
        
      print "\n[!]",n,"-character finished in %s seconds ---" % (time.time() - characterstart_time)
   


def main():
    print info
    
    inp_usr = raw_input(" add md5\n")
    chrs = string.printable.replace(' \t\n\r\x0b\x0c', '')
    return _attack( chrs,inp_usr );

   

if __name__ == "__main__":
    main()
   
   
   
