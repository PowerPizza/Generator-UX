from colorama import Fore
import threading
import time
from unit_sorter import unitify

banner = """
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬛⬛⬜⬜⬛⬛⬜⬜⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜
⬜⬛⬛⬜⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜
⬜⬛⬛⬜⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬛⬜
⬜⬜⬜⬜⬜⬛⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬜
⬜⬛⬛⬜⬜⬛⬜⬜⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜⬜⬛⬛⬛⬜⬜
⬜⬛⬛⬜⬜⬛⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
"""
c = "abcdefghijklmnopqrstuvwxyz"
c = r"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[]{}|;:',.<>?/`~₹\\"

fp = None
counter = 0
comb_ = ""
def comb_writer(pass_len, comb=""):
	global counter, comb_
	if pass_len == 0:
		fp.write(comb+"\n")
		counter += 1
		comb_ = comb
		return comb
	for x in range(len(c)):
		comb_writer(pass_len-1, comb+c[x])

print(Fore.GREEN + "Welcome to")
print(banner)
print(Fore.MAGENTA+" "*10+">>>>> Developed By : SCIHACK <<<<<\n")

print(Fore.RED+f"Default Character List :-\n{c}")
char_list_yn = input(Fore.CYAN+"Do you want to continue with this one?\n • y for yes\n • n for no\n • e for exit : ").lower()
if char_list_yn == "n":
	c = input("Enter string of unique characters : ")
	c = "".join(set(c))
elif char_list_yn == "e":
	exit(0)
	
n = int(input("Enter length of combination : "))
agree = input(Fore.WHITE+f"Total number of possibilities : {len(c)**n}\nOutput file will consume ≈ {unitify(len(c)**n)}\n{Fore.CYAN}This may take time do you want to continue?\n • y for yes\n • n for no\n • e for exit :- ").lower()
if agree == "e":
	exit(0)
elif agree == "y":
	out_f_name = input("Enter output file name : ")
	if out_f_name:
		file_ = out_f_name+".txt"
		fp = open(file_, "a")
		t1 = time.perf_counter()
		td = threading.Thread(target=comb_writer, args=(n, ))
		td.start()
		while td.is_alive():
			print(Fore.YELLOW + f"combination : {comb_} | Progress : {int(counter/(len(c)**n)*100)} %", end="\r")
		fp.close()
		print(" "*40)
		print(Fore.CYAN+f"Time taken : {round(time.perf_counter()-t1)} sec")
		print(Fore.GREEN+"☑ Successfully generated combination file.")
	else:
		print(Fore.RED+"✖ invalid file name!")
print(Fore.RESET)
