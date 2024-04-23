"""Trains a DQN/DDQN to solve CartPole-v0 problem


"""
#import ground_truth_dict_dataset0819


import json
import math


import matplotlib.pyplot as plt


def plotone(rewards, fig = "test.png", xlabel = "Episodes", ylabel="Rewards"):
    plt.figure(figsize=(20,5))
    plt.plot(rewards)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    # plt.legend()
    plt.savefig(fig)

    #plt.show()
    plt.clf()

def plot(rewards1, rewards2):
    plt.figure(figsize=(20,5))
    plt.plot(rewards1, label='rewards1')
    plt.plot(rewards2, label='rewards2')

    plt.xlabel("Episode")
    plt.ylabel("Rewards")
    plt.legend()
    plt.savefig('multi_reward.png')

    plt.show()
    plt.clf()










# total_wmu_cam_trigger_times =  [5546, 4371, 2939, 2191, 1882, 1112, 1432, 604, 530, 760] + [346, 409, 324] + [310, 282, 300, 283, 272, 274, 258, 262, 259, 255]

# # ignore the fisrt trigger
# total_wmu_mic_trigger_times = [3762, 2612, 1774, 1167, 846, 536, 362, 266, 167, 95] + [83, 72, 56] + [51, 25, 35, 35, 28, 24, 19, 22, 17, 9]
# total_wmu_trigger_times = [1828, 1347, 883, 617, 424, 261, 191, 142, 80, 45] + [41, 34, 28] + [26, 11, 18, 20, 16, 14, 11, 8, 10, 4]

# total_robot_mic_trigger_times = [6302, 6732, 6503, 3134, 2504, 1617, 1346, 1852, 1550, 1762] + [1031, 628, 718] + [984, 331, 333, 655, 590, 577, 552, 290, 281, 845]
# total_robot_cam_trigger_times = [4142, 3661, 2325, 1734, 1225, 686, 489, 309, 255, 192] + [260, 134, 230] + [126, 129, 120, 115, 107, 105, 105, 93, 94, 100]
# total_robot_trigger_times = [2334, 1857, 1141, 831, 489, 430, 312, 188, 187, 143] + [219, 111, 207] + [108, 104, 104, 99, 99, 95, 96, 88, 89, 91]
# total_privacy_level1_times = [1455, 1369, 680, 435, 324, 216, 151, 96, 67, 52] + [40, 33, 37] + [32, 31, 31, 26, 20, 28, 21, 24, 21, 20]
# total_privacy_level2_times = [10416, 9778, 8780, 4768, 3761, 2192, 1733, 2142, 1717, 1853] + [1114, 689, 759] + [1020, 349, 352, 679, 605, 582, 558, 292, 281, 842]



# total_privacy_level1_robot_vision_times = [432, 321, 203, 175, 99, 66, 40, 24, 16, 13] + [6, 6, 8] + [4, 5, 4, 4, 2, 4, 1, 2, 3, 2]
# total_privacy_level1_robot_sound_times = [751, 870, 398, 237, 174, 133, 92, 56, 38, 35] + [31, 23, 27] + [22, 26, 26, 23, 19, 23, 18, 20, 18, 19]
# total_privacy_level1_wmu_sound_times = [474, 316, 189, 125, 105, 57, 43, 24, 20, 10] + [8, 7, 6] + [9, 4, 3, 1, 1, 3, 3, 3, 1, 1]
# total_privacy_level2_robot_vision_times = [3710, 3340, 2122, 1559, 1126, 620, 449, 285, 239, 179] + [254, 128, 222] + [122, 124, 116, 111, 105, 101, 104, 91, 91, 98]
# total_privacy_level2_robot_sound_times = [5551, 5862, 6105, 2897, 2330, 1484, 1254, 1796, 1512, 1727] + [1000, 605, 691] + [962, 305, 307, 632, 571, 554, 534, 270, 263, 826]
# total_privacy_level2_wmu_sound_times = [3287, 2295, 1584, 1041, 740, 478, 318, 241, 146, 84] + [74, 64, 49] + [41, 20, 31, 33, 26, 20, 15, 18, 15, 7]




# scores = [
# -8799.485206666699,
# -5962.1147106672925,
# -3341.9217086673566,
# -2038.6806866666468,
# -1404.990996000011,
# -678.4099999999966,
# -567.8119999999955,
# -204.79199999999133,
# -80.02000000000476,
# -77.7120000000061,
# 63.58199999999945,
# 79.87800000000014,
# 102.65800000000044,
# 124.13799999999893,
# 158.2179999999993,
# 147.82399999999964,
# 153.12799999999783,
# 165.54399999999828,
# 166.68599999999822,
# 179.06599999999767,
# 176.19199999999898,
# 181.68199999999888,
# 183.99399999999608,
# ]





total_wmu_cam_trigger_times =  [5647, 4044, 2863, 2071, 2111, 1009, 784, 753, 498, 753] + [345, 485, 309, 302, 415, 280, 279, 264, 262, 255]

# ignore the fisrt trigger
total_wmu_mic_trigger_times = [3709, 2653, 1760, 1217, 822, 526, 354, 251, 165, 100] + [82, 68, 64, 49, 30, 27, 28, 24, 17, 18]
total_wmu_trigger_times = [1826, 1384, 887, 587, 412, 268, 187, 124, 80, 59] + [44, 31, 34, 23, 17, 13, 15, 13, 10, 8]

total_robot_mic_trigger_times = [6623, 6723, 5907, 5516, 5325, 4295, 4088, 3866, 3198, 3049] + [3212, 2792, 2492, 2028, 1743, 1628, 818, 1475, 305, 297]
total_robot_cam_trigger_times = [3770, 2557, 1767, 1281, 838, 1149, 399, 586, 206, 154] + [164, 107, 110, 110, 92, 99, 79, 71, 76, 74]
total_robot_trigger_times = [1941, 1308, 875, 682, 439, 310, 220, 179, 128, 100] + [91, 70, 80, 84, 74, 86, 64, 64, 67, 63]
total_privacy_level1_times = [1347, 933, 599, 445, 310, 195, 140, 105, 67, 51] + [39, 36, 36, 35, 26, 32, 23, 24, 22, 24]
total_privacy_level2_times = [10813, 9691, 7959, 6886, 6235, 5464, 4480, 4418, 3373, 3151] +  [3327, 2860, 2549, 2067, 1764, 1635, 837, 1481, 308, 301]



total_privacy_level1_robot_vision_times = [440, 300, 186, 142, 91, 54, 46, 25, 18, 10] + [9, 7, 8, 8, 3, 6, 1, 1, 1, 1]
total_privacy_level1_robot_sound_times = [665, 456, 303, 226, 160, 104, 71, 64, 41, 32] + [26, 23, 26, 27, 22, 27, 19, 20, 19, 19]
total_privacy_level1_wmu_sound_times = [484, 318, 213, 151, 102, 65, 43, 32, 17, 13] + [8, 8, 5, 4, 2, 3, 3, 3, 2, 4]
total_privacy_level2_robot_vision_times = [3330, 2257, 1581, 1139, 747, 1095, 353, 561, 188, 144] + [155, 100, 102, 102, 89, 93, 78, 70, 75, 73]
total_privacy_level2_robot_sound_times =  [5958, 6267, 5604, 5290, 5165, 4191, 4017, 3802, 3157, 3017] + [3186, 2769, 2466, 2001, 1721, 1601, 799, 1455, 286, 278]
total_privacy_level2_wmu_sound_times = [3224, 2334, 1546, 1065, 719, 460, 310, 218, 147, 86] + [73, 59, 58, 44, 27, 23, 24, 20, 14, 13]


scores = [
    -8868.795974000148,
-5543.136826000774,
-3212.5621286672117,
-1928.5895139999586,
-1528.9494266666018,
-684.0959999999744,
-394.69199999997556,
-284.073999999974,
-74.40600000000485,
-85.25200000001259,
59.1479999999999,
33.76199999999913,
103.12199999999834,
124.2939999999948,
114.5160000000011,
155.4819999999949,
168.20399999999668,
163.6939999999935,
187.52199999999888,
191.2439999999988,
]


# cat test.0421_p_0.6_1layer_Transition2_level1_0.2_nositting_energy_0.35_acc_0.05_0.6_trianall_true.txt |grep epi | awk '{print $4}'
# total_wmu_cam_trigger_times: [5647, 4044, 2863, 2071, 2111, 1009, 784, 753, 498, 753]
# total_wmu_mic_trigger_times: [3709, 2653, 1760, 1217, 822, 526, 354, 251, 165, 100]
# total_wmu_trigger_times: [1826, 1384, 887, 587, 412, 268, 187, 124, 80, 59]
# total_robot_mic_trigger_times: [6623, 6723, 5907, 5516, 5325, 4295, 4088, 3866, 3198, 3049]
# total_robot_cam_trigger_times: [3770, 2557, 1767, 1281, 838, 1149, 399, 586, 206, 154]
# total_robot_trigger_times: [1941, 1308, 875, 682, 439, 310, 220, 179, 128, 100]
# total_privacy_level1_times: [1347, 933, 599, 445, 310, 195, 140, 105, 67, 51]
# total_privacy_level2_times: [10813, 9691, 7959, 6886, 6235, 5464, 4480, 4418, 3373, 3151]
# total_privacy_level1_robot_vision_times: [440, 300, 186, 142, 91, 54, 46, 25, 18, 10]
# total_privacy_level1_robot_sound_times: [665, 456, 303, 226, 160, 104, 71, 64, 41, 32]
# total_privacy_level1_wmu_sound_times: [484, 318, 213, 151, 102, 65, 43, 32, 17, 13]
# total_privacy_level2_robot_vision_times: [3330, 2257, 1581, 1139, 747, 1095, 353, 561, 188, 144]
# total_privacy_level2_robot_sound_times: [5958, 6267, 5604, 5290, 5165, 4191, 4017, 3802, 3157, 3017]
# total_privacy_level2_wmu_sound_times: [3224, 2334, 1546, 1065, 719, 460, 310, 218, 147, 86]


# total_wmu_cam_trigger_times: [345, 485, 309, 302, 415, 280, 279, 264, 262, 255]
# total_wmu_mic_trigger_times: [82, 68, 64, 49, 30, 27, 28, 24, 17, 18]
# total_wmu_trigger_times: [44, 31, 34, 23, 17, 13, 15, 13, 10, 8]
# total_robot_mic_trigger_times: [3212, 2792, 2492, 2028, 1743, 1628, 818, 1475, 305, 297]
# total_robot_cam_trigger_times: [164, 107, 110, 110, 92, 99, 79, 71, 76, 74]
# total_robot_trigger_times: [91, 70, 80, 84, 74, 86, 64, 64, 67, 63]
# total_privacy_level1_times: [39, 36, 36, 35, 26, 32, 23, 24, 22, 24]
# total_privacy_level2_times: [3327, 2860, 2549, 2067, 1764, 1635, 837, 1481, 308, 301]
# total_privacy_level1_robot_vision_times: [9, 7, 8, 8, 3, 6, 1, 1, 1, 1]
# total_privacy_level1_robot_sound_times: [26, 23, 26, 27, 22, 27, 19, 20, 19, 19]
# total_privacy_level1_wmu_sound_times: [8, 8, 5, 4, 2, 3, 3, 3, 2, 4]
# total_privacy_level2_robot_vision_times: [155, 100, 102, 102, 89, 93, 78, 70, 75, 73]
# total_privacy_level2_robot_sound_times: [3186, 2769, 2466, 2001, 1721, 1601, 799, 1455, 286, 278]
# total_privacy_level2_wmu_sound_times: [73, 59, 58, 44, 27, 23, 24, 20, 14, 13]




default_x_ticks = range(len(scores[2:]))

print('len(scores):', len(scores))


#plotone(scores, fig = "dqn_accumulated_rewards.png", xlabel = "Episodes", ylabel="Accumulated Rewards")

plt.figure(figsize=(20,5))
plt.rcParams.update({'font.size': 23})
plt.plot(default_x_ticks, scores[2:])
plt.xticks(default_x_ticks)
# plt.xlabel('Episodes')
# plt.ylabel('Accumulated Rewards')
# plt.legend()
plt.savefig('dpqn_accumulated_rewards.png')
plt.clf()




print('len(wmu times):', len(total_wmu_cam_trigger_times))

plt.figure(figsize=(20,5))
plt.rcParams.update({'font.size': 23})
plt.plot(total_wmu_cam_trigger_times[2:], label='wmu_cam_trigger_times')
plt.plot(total_wmu_mic_trigger_times[2:], label='wmu_mic_trigger_times')
# plt.plot(total_wmu_trigger_times, label='total_wmu_mic_cam_trigger_times')
plt.plot(total_robot_mic_trigger_times[2:], label='robot_mic_trigger_times')
plt.plot(total_robot_cam_trigger_times[2:], label='robot_cam_trigger_times')
plt.plot(total_privacy_level1_times[2:], label='privacy_level1_times')
plt.plot(total_privacy_level2_times[2:], label='privacy_level2_times')



plt.xticks(default_x_ticks)

# plt.xlabel("Episodes")
# plt.ylabel("Times")
plt.legend()
plt.savefig('dpqn_multi_reward.png')
# plt.show()
plt.clf()




plt.figure(figsize=(20,5))
plt.rcParams.update({'font.size': 23})
plt.plot(total_privacy_level1_robot_vision_times[2:], label='privacy_level1_robot_vision_times')
plt.plot(total_privacy_level1_robot_sound_times[2:], label='privacy_level1_robot_sound_times')
plt.plot(total_privacy_level1_wmu_sound_times[2:], label='privacy_level1_wmu_sound_times')
plt.plot(total_privacy_level2_robot_vision_times[2:], label='privacy_level2_robot_vision_times')
plt.plot(total_privacy_level2_robot_sound_times[2:], label='privacy_level2_robot_sound_times')
plt.plot(total_privacy_level2_wmu_sound_times[2:], label='privacy_level2_wmu_sound_times')
# plt.plot(total_privacy_level1_times[2:-1], label='privacy_level1_times')
# plt.plot(total_privacy_level2_times[2:-1], label='privacy_level2_times')



plt.xticks(default_x_ticks)

# plt.xlabel("Episodes")
# plt.ylabel("Times")
plt.legend()
plt.savefig('dpqn_privacy_level.png')

# plt.show()
plt.clf()

exit(0)

