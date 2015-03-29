# Created by cxy on 15/3/15 with PyCharm
# -*- coding: utf-8 -*-
import random


# 生成随机数据集
def get_random_list(num):
    result = []
    for i in xrange(num):
        result.append(random.randint(0, 10000000))
    return result


# 冒泡排序
def bubble_sort(l):
    """
    从待排序列表首元素开始, 将相邻两元素进行比较, 若两者反序, 则交换两元素值;
    下一轮则进行到倒数第二个元素, 以此类推
    """
    n = len(l)
    i = 0
    j = n - 1
    while i < j:
        for k in range(i, j):
            if l[k] > l[k+1]:
                l[k], l[k+1] = l[k+1], l[k]
        j -= 1
    return l


# 插入排序
def insertion_sort(l):
    """
    从第二个元素起将当前元素与前一个相邻元素比较, 若比前一个元素小, 则前一个元素向后挪动一位
    直至比较到首元素或不比待比较元素小为止; 这样维护一个递增的列表, 直至整个排序完成
    """
    for i in range(1, len(l)):
        tmp = l[i]
        j = i
        while i >= 1 and tmp < l[j-1]:
            l[j] = l[j-1]
            j -= 1
        l[j] = tmp
    return l


# 选择排序
def selection_sort(l):
    """
    每一轮选择一个最小元素替换当前元素, 直至排序完成
    """
    n = len(l)
    for i in range(0, n):
        index_min = i
        min = l[i]
        for j in range(i+1, n):
            if l[j] < min:
                min = l[j]
                index_min = j
        l[i], l[index_min] = l[index_min], l[i]
    return l


# 希尔排序
def shell_sort(l):
    """
    升级版的插入排序, 设置gap将原列表中元素按照间隔gap进行插入排序, 一次次缩小gap直至全部完成
    """
    n = len(l)
    gap = n / 2
    while gap > 0:
        for i in range(gap, n):
            tmp = l[i]
            j = i
            while j >= gap and tmp < l[j-gap]:
                l[j] = l[j-gap]
                j -= gap
            l[j] = tmp
        gap /= 2
    return l


# 归并排序
def merge(l, r):
    """
    merge_sort的merge部分, 将两个有序列表合并为一个有序列表
    每次取两列表顶端元素(最小值)进行比较, 取较小值添加到结果列表中
    """
    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
    result += l[i:]
    result += r[j:]
    return result


def merge_sort(l):
    """
    merge_sort的sort部分, 递归地将列表拆分成两部分, 直至长为0或1, 再调用merge函数
    """
    if len(l) <= 1:
        return l
    mid = len(l) / 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


# 快速排序
def quick_sort(l, left, right):
    if left >= right:
        return l
    left_index, right_index = left, right
    key = l[left_index]
    while left_index < right_index:
        while l[right_index] >= key and left_index < right_index:
            right_index -= 1
        while l[left_index] <= key and left_index < right_index:
            left_index += 1
        l[left_index], l[right_index] = l[right_index], l[left_index]
    l[left], l[left_index] = l[left_index], l[left]
    quick_sort(l, left, left_index-1)
    quick_sort(l, left_index+1, right)
    return l


# 堆排序


def main():
    random_nums = get_random_list(20)
    print 'random nums:' + str(random_nums)
    print 'bubble sort:' + str(bubble_sort(random_nums))
    print 'insertion sort' + str(insertion_sort(random_nums))
    print selection_sort(random_nums)
    print shell_sort(random_nums)
    print merge_sort(random_nums)
    print quick_sort(random_nums, 0, len(random_nums)-1)


if __name__ == '__main__':
    main()