import numpy as np

list = [2, 6, 2, 8, 4, 0, 1, 5, 7]
arr = np.array(list)

arr = np.reshape(arr, (3, 3))
#print(arr)

# Mean for Columns
mean1 = np.zeros((1, 3))
mean1[(0, 0)] = np.mean(arr[:, 0])
mean1[(0, 1)] = np.mean(arr[:, 1])
mean1[(0, 2)] = np.mean(arr[:, 2])
mean1 = mean1.tolist()

# Mean for Rows
mean2 = np.zeros((1, 3))
mean2[(0, 0)] = np.mean(arr[0, :])
mean2[(0, 1)] = np.mean(arr[1, :])
mean2[(0, 2)] = np.mean(arr[2, :])
mean2 = mean2.tolist()

# Mean for Flattened Array
flatten = np.ravel(arr)
meanflat = np.mean(flatten)
meanflat = meanflat.tolist()

# Variance for Columns
var1 = np.zeros((1, 3))
var1[(0, 0)] = np.var(arr[:, 0])
var1[(0, 1)] = np.var(arr[:, 1])
var1[(0, 2)] = np.var(arr[:, 2])
var1 = var1.tolist()

# Variance for Rows
var2 = np.zeros((1, 3))
var2[(0, 0)] = np.var(arr[0, :])
var2[(0, 1)] = np.var(arr[1, :])
var2[(0, 2)] = np.var(arr[2, :])
var2 = var2.tolist()

# Variance for Flattened Array
flatten = np.ravel(arr)
varflat = np.var(flatten)
varflat = varflat.tolist()

#Standard Deviation for Columns
stan1 = np.zeros((1, 3))
stan1[(0, 0)] = np.std(arr[:, 0])
stan1[(0, 1)] = np.std(arr[:, 1])
stan1[(0, 2)] = np.std(arr[:, 2])
stan1 = stan1.tolist()

#Standard Deviation for Rows
stan2 = np.zeros((1, 3))
stan2[(0, 0)] = np.std(arr[0, :])
stan2[(0, 1)] = np.std(arr[1, :])
stan2[(0, 2)] = np.std(arr[2, :])
stan2 = stan2.tolist()

#Standard Deviation for Flattened Array
stdflat = np.std(flatten)
stdflat = stdflat.tolist()

#Max of Columns
max1 = np.zeros((1, 3))
max1[(0, 0)] = np.max(arr[:, 0])
max1[(0, 1)] = np.max(arr[:, 1])
max1[(0, 2)] = np.max(arr[:, 2])
max1 = max1.tolist()

#Max for Rows
max2 = np.zeros((1, 3))
max2[(0, 0)] = np.max(arr[0, :])
max2[(0, 1)] = np.max(arr[1, :])
max2[(0, 2)] = np.max(arr[2, :])
max2 = max2.tolist()

#Max for Flattened Array
maxflat = np.max(flatten)
maxflat = maxflat.tolist()

#Min for Columns
min1 = np.zeros((1, 3))
min1[(0, 0)] = np.min(arr[:, 0])
min1[(0, 1)] = np.min(arr[:, 1])
min1[(0, 2)] = np.min(arr[:, 2])
min1 = min1.tolist()


#Min for Rows
min2 = np.zeros((1, 3))
min2[(0, 0)] = np.min(arr[0, :])
min2[(0, 1)] = np.min(arr[1, :])
min2[(0, 2)] = np.min(arr[2, :])
min2 = min2.tolist()

#Min for Flattened Array
minflat = np.min(flatten)
minflat = minflat.tolist()

#Sum of Columns
sum1 = np.zeros((1,3))
sum1[(0, 0)] = np.sum(arr[:, 0])
sum1[(0, 1)] = np.sum(arr[:, 1])
sum1[(0, 2)] = np.sum(arr[:, 2])
sum1 = sum1.tolist()

#Sum of Rows
sum2 = np.zeros((1,3))
sum2[(0, 0)] = np.sum(arr[0, :])
sum2[(0, 1)] = np.sum(arr[1, :])
sum2[(0, 2)] = np.sum(arr[2, :])
sum2 = sum2.tolist()

#Sum for Flattened Array
sumflat = np.sum(flatten)
sumflat = sumflat.tolist()

calculations = {
    'mean': [mean1, mean2, meanflat],
    'variance': [var1, var2, varflat],
    'standard deviation': [stan1, stan2, stdflat],
    'max': [max1, max2, maxflat],
    'min': [min1, min2, minflat],
    'sum': [sum1, sum2, sumflat]
}

calculations