#!/usr/bin/env python3
import sys
import unittest
import numpy as np
import filter

PKG = "human_info"


# This class is copied from the pose_engine file.
class Keypoint:
    __slots__ = ['k', 'yx', 'score']

    def __init__(self, k, yx, score=None):
        self.k = k
        self.yx = yx
        self.score = score

    def __repr__(self):
        return 'Keypoint(<{}>, {}, {})'.format(self.k, self.yx, self.score)


class TestHumanInfo(unittest.TestCase):
    def setUp(self):
        self.input = np.random.normal(0, 1, 1000)
        self.max_input = max(self.input)
        self.min_input = min(self.input)

    def test_average_filter(self):
        self.average_filter = filter.Average_Filter()
        for i in self.input:
            self.distance = i
            self.updated_distance = self.average_filter.update(self.distance)
        self.assertTrue(abs(self.updated_distance) < 1)


    def test_keypoint_filter(self):
        keypoints = {'nose': Keypoint("nose", [81.410835, 304.39337], 0.9973853230476379),
                     'left eye': Keypoint("left eye", [71.47854, 314.43033], 0.9972434043884277),
                     'right eye': Keypoint("right eye", [71.80488, 295.17383], 0.9972702860832214),
                     'left ear': Keypoint("left ear", [73.39448, 327.2892], 0.8895582556724548),
                     'right ear': Keypoint("right ear", [74.901, 282.77927], 0.9370625019073486),
                     'left shoulder': Keypoint("left shoulder", [131.08563, 348.47763], 0.9869135022163391),
                     'right shoulder': Keypoint("right shoulder", [135.85083, 257.59082], 0.9882190227508545),
                     'left elbow': Keypoint("left elbow", [214.84499, 341.70224], 0.1400817632675171),
                     'right elbow': Keypoint("right elbow", [216.13953, 240.53134], 0.7240224480628967),
                     'left wrist': Keypoint("left wrist", [266.73596, 344.28912], 0.04551970586180687),
                     'right wrist': Keypoint("right wrist", [284.7887, 255.05605], 0.317013680934906),
                     'left hip': Keypoint("left hip", [285.78522, 331.20517], 0.5591225028038025),
                     'right hip': Keypoint("right hip", [295.74838, 281.54306], 0.5805069804191589),
                     'left knee': Keypoint("left knee", [390.70868, 330.60098], 0.5389679074287415),
                     'right knee': Keypoint("right knee", [395.54587, 279.84836], 0.7566099166870117),
                     'left ankle': Keypoint("left ankle", [480., 293.88235], 0.32836902141571045),
                     'right ankle': Keypoint("right ankle", [480., 291.47543], 0.1815498173236847)}
        FEATURES = ['nose', 'left eye', 'right eye', 'left ear', 'right ear', 'left shoulder', 'right shoulder',
                    'left elbow', 'right elbow', 'left wrist', 'right wrist', 'left hip', 'right hip', 'left knee',
                    'right knee', 'left ankle', 'right ankle']

        kpfilter = filter.Keypoint_Filter(0.5, 2, FEATURES, 50 ** 2)

        keypoints = kpfilter.update(keypoints)

        keypoints2 = keypoints.copy()
        self.assertEqual(keypoints, keypoints2)

        keypoints2["nose"].yx[0] -= 40
        keypoints3 = keypoints2.copy()
        keypoints2 = kpfilter.update(keypoints2)
        self.assertNotEqual(keypoints2["nose"].yx[0], keypoints3["nose"].yx[0])
        self.assertNotEqual(keypoints2, keypoints)

        oldKeypoints2 = kpfilter.update(keypoints2)
        del keypoints2["nose"]
        keypoints4 = kpfilter.update(keypoints2)
        self.assertTrue("nose" in keypoints4)
        kpfilter.update(keypoints2)
        keypoints5 = kpfilter.update(keypoints2)
        self.assertFalse("nose" in keypoints5)
        keypoints6 = kpfilter.update(keypoints2)
        self.assertFalse("nose" in keypoints6)



if __name__ == '__main__':
    import rosunit
    import rostest

    rostest.rosrun(PKG, 'test_filter', TestHumanInfo, sys.argv)
