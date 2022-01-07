import emoji
import time
Name1 = input("ENTER FIRST NAME : ") #Getting inputs from the user
Name2 = input("ENTER SECOND NAME : ")
def flames(Name1,Name2):
	F1name = list(Name1) #changing the string inputs into list
	F2name = list(Name2)
	for f1 in F1name[:]: #Remove the common elements in both lists
		if f1 in F2name:
			F1name.remove(f1)
			F2name.remove(f1)
			result = F1name + F2name #adding two lists
	length = len(result) #find the length of the list
	print("Let's GOOO......") #set some attractive time delay
	time.sleep(2)
	print(f"NOT MACTHED WORDS : {length}") #print the unmatched words from the given inputs
	time.sleep(2)
	relt = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"] #FLAMES list
	while len(relt) > 1 : #here is the logic for the FLAMES choosing
		split_index = (length % len(relt) - 1) 
		if (split_index>=0) :
			right = relt[split_index + 1 : ]
			left = relt[ : split_index] 
			relt = right + left
		else : 
			relt = relt[ : len(relt) - 1]

	print("<< RELATIONSHIP STATUS IS LOADING >> ") #ATTRACTION
	time.sleep(2)
	print("1.FRIENDS")
	time.sleep(1)
	print("2.LOVERS")
	time.sleep(1)
	print("3.AFFECTION")
	time.sleep(1)
	print("4.MARRIAGE")
	time.sleep(1)
	print("5.ENEMY")
	time.sleep(1)
	print("6.SIBILINGS")
	time.sleep(3)
	print("<< LOADED 100%..... >>")
	time.sleep(2)
	print(f"YOUR CONNECTION IS : {relt}") #Result will be print at the end
flames(Name1,Name2)
