# Name      : Pranav Bhandari
# Student ID: 1001551132
# Date      : 11/23/2020

import sys, random, math

class Data:
    def __init__(self, items, cluster_number):
        self.items = items
        self.cluster_number = cluster_number
        
    def __repr__(self):
        return "{} {}".format(self.items, self.cluster_number) 
    
    def __str__(self):  
        return "{} {}".format(self.items, self.cluster_number)  

def calc_dist(list1, list2):
    if len(list1)!=len(list2):
        print("calc_dist: Error, the length of the two lists is not the same.")
        sys.exit(1)
    result= 0.0
    for i in range(len(list1)):
        result += math.pow(list1[i]-list2[i], 2)
    result = math.pow(result, 0.5)
    return result

def k_means(data_file, k, method):
    file = open(data_file, "r");
    Lines = file.readlines();
    data = []
    if method == "round_robin":
        temp = 0
        for line in Lines:
            intermediate = [float(num) for num in line.split()]
            data.append(Data(intermediate, temp))
            temp = (temp+1)%k
    else:
        for line in Lines:
            intermediate = [float(num) for num in line.split()]
            data.append(Data(intermediate, random.randint(0, k-1)))


    num_dimensions = len(data[0].items)
    while True:
        changes = 0
        means = [[0.0 for j in range(num_dimensions)] for i in range(k)]
        nums = [0 for i in range(k)]
        for i in range(len(data)):
            nums[data[i].cluster_number] += 1
            for j in range(num_dimensions):
                means[data[i].cluster_number][j] += data[i].items[j]

        means = [[float(temp)/nums[i] for temp in means[i]] for i in range(k)]
        
        for i in range(len(data)):
            min_dist = sys.float_info.max
            index = -1
            for j in range(k):
                dist = calc_dist(data[i].items, means[j])
                if dist < min_dist:
                    min_dist = dist
                    index = j
            if index!=-1 and index!=data[i].cluster_number:
                data[i].cluster_number = index
                changes +=1
        if changes == 0:
            break

    for i in range(len(data)):
        if num_dimensions == 1:
            print("{:10.4f} --> cluster {:d}".format(data[i].items[0], data[i].cluster_number+1))
        elif num_dimensions ==2:
            print("({:10.4f}, {:10.4f}) --> cluster {:d}".format(data[i].items[0], data[i].items[1], data[i].cluster_number+1))
        else: 
            print("k_means: Error, number of dimensions is not 1 or 2")
            sys.exit(1)
                
        

if __name__=="__main__": 
    print(sys.argv[0])
    k_means(sys.argv[1], int(sys.argv[2]), sys.argv[3])