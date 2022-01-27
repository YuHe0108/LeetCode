
from collections import defaultdict
import heapq


# def solution(buildings):
#     points = []
#     for build in buildings:
#         points.append((build[0], -build[2]))
#         points.append((build[1], build[2]))
#     points.sort(key=lambda x: (x[0], x[1]))
#     # 用来保存当前扫描线所经过的建筑的高度，用堆来表示
#     should_del = defaultdict(int)  # 因为在堆里面删除元素需要更多的时间开销，所以先把需要删除的元素保存起来
#     heights = []
#     res = []
#     cur_height = 0
#     for p, h in points:
#         if h < 0:
#             heapq.heappush(heights, h)
#         else:
#             # 高度开始降低
#             should_del[h] += 1
#
#         print(heights, should_del, p, h, res)
#         while heights and -heights[0] in should_del:
#             temp = -heights[0]
#             heapq.heappop(heights)
#             should_del[temp] -= 1
#             if should_del[temp] == 0:
#                 should_del.pop(temp)
#
#         max_h = -heights[0] if heights else 0
#         if max_h != cur_height:
#             cur_height = max_h
#             res.append([p, cur_height])
#
#     print(res)
#     return res

def solution(building):
    points = []
    for left, right, h in building:
        points.append([left, -h])
        points.append([right, h])
    points.sort(key=lambda x: (x[0], x[1]))  # 按照x排序
    heights = []
    should_del = defaultdict(int)
    res = []
    cur_h = 0
    for p, h in points:
        if h < 0:  # 高楼开始出现
            heapq.heappush(heights, h)
        else:  # 高楼结束出现
            should_del[h] += 1  # 应当删除当前的高度

        # 应当删除的高度正好是当前最高的高度，则应当删除当前的高度
        while heights and should_del[-heights[0]] > 0:
            should_del[-heights[0]] -= 1
            heapq.heappop(heights)

        max_h = -heights[0] if heights else 0
        if max_h != cur_h:
            cur_h = max_h
            res.append([p, max_h])
    print(res)
    return


if __name__ == '__main__':
    solution([[0, 2, 3], [2, 5, 3]])
