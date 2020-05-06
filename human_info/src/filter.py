"""
Contains filters used in human pose estimation

"""

class Average_Filter:
    """
    Filter apllied to calculated distances from human pose estimation.
    First iteration calculates average distance over samplesize n = 10
    only last 10 distances are considered
    """
    def __init__(self):
        self.lst = []
        # samplesize n = 10
        self.n = 10

    def update(self, new_dist):
        #global average_distance
        self.lst.append(new_dist)
        average_distance = sum(self.lst) / len(self.lst)
        if len(self.lst) > self.n:
            self.lst.remove(self.lst[0])
        return average_distance

class Outlier_Rejection:
    """
    outlier rejection of extremes in calculated distance from human pose estimation
    Discards all outputs that are further away than
        max_difference
    compared to previous timestep.
    """
    def __init__(self):
        # maximal difference allowed between two timesteps
        self.max_difference = 50
        self.lst = {}

    def update(self, new_dist, keypoint_type):

        # if there is no entry, for that feature, in the dictionary, this is the first pose with that feature
        if !self.lst[keypoint_type]:
            self.lst[keypoint_type]=new_dist
            return self.lst[keypoint_type]
        # otherwise check the difference between this new pose distance, and the old one; if it's bigger that max_difference, this is an outlier, and should be ignored
        elif abs(new_dist - self.lst[keypoint_type]) > self.max_difference:
            return -1
        # otherwise it's within the acceptable range, and we return the value
        return self.lst[keypoint_type]
