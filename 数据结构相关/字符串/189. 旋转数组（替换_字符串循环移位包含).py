189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入: [-1,-100,3,99] 和 k = 2
输出: [3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]


############方法1 三次旋转法
##Tips：这个技巧性挺酷的，值得掌握。

"""
执行用时 :
36 ms
, 在所有 Python3 提交中击败了
92.16%
的用户
内存消耗 :
13.8 MB
, 在所有 Python3 提交中击败了
97.30%
的用户
"""



