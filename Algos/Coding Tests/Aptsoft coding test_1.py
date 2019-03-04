'''
The problem is to find the 'N' closest points from the origin in a coordinate system
'''
import math


class Solution:
    def calc_dist(self, point, ref_point=(0, 0)):
        return math.sqrt((point[0] - ref_point[0])**2 + (point[1] - ref_point[1])**2)

    def get_closest_points(self, points, N, *args):
        ref_point = ()
        if len(args) > 0:
            ref_point = args[0]
        distances = [self.calc_dist(point, ref_point if ref_point else (0, 0)) for point in points]
        sorted_dist = (distances.index(i) for i in sorted(distances))
        return [points[next(sorted_dist)] for _ in range(N)]


test1 = Solution()
print(test1.get_closest_points([(5, 6), (1, 2), (2, 3), (3, 4)], 2))  # [(1, 2), (2, 3)]
