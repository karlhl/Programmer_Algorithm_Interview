# 方法一 空间换时间，hash
"""
方法：找到数组中唯一重复的元素
输入：array
输出：重复的值，如果无重复则-1
python中可以用字典来替代hash法的功能
"""

def findDup(array):
    if None == array:
        return -1
    lens = len(array)
    hashTable = dict()
    i = 0
    while i <lens-1:
        hashTable[i] = 0
        i+=1
    j = 0
    while j<lens:
        if hashTable[array[j]-1] == 0:
            hashTable[array[j]-1] = array[j] -1
        else:
            return array[i]
        j+=1
    return -1

if __name__ == "__main__":
    array=[1,3,4,2,5,3]
    print(findDup(array))
