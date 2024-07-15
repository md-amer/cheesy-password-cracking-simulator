from random import choice
import os
from time import sleep

target_string = input('What is your target? ')
target_list = []
for i in target_string:
	target_list.append(i)
	
stuff = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',',',',','/','<','>','?',';','"','[',']','{','}','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0',' ']
	
current_list = []

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')
	
	
def print_text(a):
	for i in range(len(a)):
		if i != len(a)-1:
			print(a[i],end='')
		else:
			print(a[i],end='\n')

for i in range(len(target_string)):
	current_list.append(choice(stuff))

while current_list != target_list:
	i = choice(range(len(target_list)))
	sleep(0.01)
	clear_screen()
	if current_list[i] != target_list[i]:
		current_list[i] = choice(stuff)
	print_text(current_list)
