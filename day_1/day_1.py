#reads input file containing both lists
with open('input.txt', 'r') as file:
    lists = file.readlines()
    
#creating empty lists to parse data into
list_1 = []
list_2 = []

#for loop to read through lists in input.txt
for line in lists:
    one, two = map(int, line.strip().split())
    list_1.append(one)
    list_2.append(two)

#sort lists
list_1.sort()
list_2.sort()

#variable for differences between numbers and similarity score
differences = []
sim_score = 0

#loop to work out differences between list 1 and 2
for num_1, num_2 in zip(list_1, list_2):
    differences.append(abs(num_1 - num_2))

#loop to work out similarity score by multiplying number being iterated through by the number of times it appears in second list
for num_1 in list_1:
    similarity = list_2.count(num_1)
    sim_score += similarity * num_1

#sum of differences to work out total
total_distance = sum(differences)

#prints out 'Total Distance' and 'Similarity Score'
print("The total distance between the two lists is {}!".format(total_distance))
print("The total similarity score is {}!".format(sim_score))
