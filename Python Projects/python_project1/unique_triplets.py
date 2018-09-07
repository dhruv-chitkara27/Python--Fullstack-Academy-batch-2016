# Task :
#
# to find unique triples whose 3 elements gives the sum 0 from the given numbers

def triplets(my_list):
    n = len(my_list)

    found = True
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (my_list[i] + my_list[j] + my_list[k] == 0):
                    print(my_list[i],'\t', my_list[j],'\t', my_list[k])
                    found = True


    # If no triplet with 0 sum found in listt
    if (found == False):
        print("No triplets with sum zero exists")
