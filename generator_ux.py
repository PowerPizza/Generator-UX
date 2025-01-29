from colorama import Fore
import threading
import time

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
def make(pass_len, comb):
	if pass_len == 0:
		print(comb)
		return comb
	for x in range(len(c)):
		make(pass_len-1, comb+c[x])
		

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

print(Fore.RED+f"Default Character List :-\n{c}")
char_list_yn = input(Fore.CYAN+"Do you want to continue with this one? (y/n) : ").lower()
if char_list_yn == "n":
	c = input("Enter string of unique characters : ")
	c = "".join(set(c))
	
n = int(input("Enter length of combination : "))
agree = input(f"Total number of possibilities : {len(c)**n}\nThis may took time do you want to continue? [y / n] :- ").lower() == "y"
if agree:
	out_f_name = input("Enter output file name : ")
	if out_f_name:
		file_ = out_f_name+".txt"
		fp = open(file_, "a")
		t1 = time.perf_counter()
		td = threading.Thread(target=comb_writer, args=(n, ))
		td.start()
		while td.is_alive():
			print(Fore.CYAN + f"combination : {comb_} | Progress : {int(counter/(len(c)**n)*100)} %", end="\r")
		fp.close()
		print(" "*40)
		print(Fore.CYAN+f"Time taken : {round(time.perf_counter()-t1)} sec")
		print(Fore.GREEN+"☑ Successfully generated combination file.")
	else:
		print(Fore.RED+"✖ invalid file name!")