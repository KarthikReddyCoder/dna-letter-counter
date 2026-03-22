#Dna sequence letter counter my first project on 2026/3/22
#enter dna sequence in CAPITALS only
dna = input("enter your dna sequence :      ")#enter your dna sequence example ATGCGTATGACCTGA
letter = input("enter the letter you want to count :      ") # enter the letter u want to count A or whatever letter
count = dna.count(letter) #code for counting the letter
print("Letter" , letter , "appears" , count , "times in you dna sequence" ) #this code tells the user how many times the letter is  in their dna sequence