#linear search
from codecs import make_identity_dict
from numpy.testing.print_coercion_tables import print_new_cast_table

pos=-1
def search (list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
list=[5,7,3,6,9,1,4]
n=9
if search(list,n):
    print("found at",pos+1)
else:
    print("not found")


#binary search
#first we have to sort in binary search
pos=-1
def serach(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
list=[4,7,9,12,95,132,456,789]
n=12
if search(list,n):
    print("found at",pos+1)
else:
    print("not found")

#bobbblesort
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
nums=[5,3,8,6,7,2]
sort(nums)
print(nums)


#selectionsort
def sort(nums):
    for i in range(5):
        minpos=i
        for j in range(i,6):
            if nums[j]<nums[minpos]:
                minpos=j
            temp=nums[i]
            nums[i]=nums[minpos]
            nums[minpos]=temp
            print(nums)
nums=[5,6,3,7,8,1,2,9]
sort(nums)
print(nums)

