#
#
# for width in range(113, 234+1):
#     for height in range(50, 188+1):
#
#         b = mean_mask - matplot_gray[width, height]
#         # print(np.sqrt(abs(b)))
#
#         if (b < 0):
#
#             if (matplot_gray[width, height] + (np.sqrt(abs(b)) * 5)) > 255:
#                 matplot_gray[width, height] = 255
#                 continue
#
#             matplot_gray[width, height] += (np.sqrt(abs(b)) * 5)
#         else:
#             if (matplot_gray[width, height] - (np.sqrt(abs(b)) * 5)) < 0:
#                 matplot_gray[width, height] = 0
#                 continue
#             matplot_gray[width, height] -= (np.sqrt(abs(b)) * 5)if (matplot_gray[width, height] - (np.sqrt(abs(b)) * 5)) < 0:
#                 matplot_gray[width, height] = 0
#                 continue
#             matplot_gray[width, height] -= (np.sqrt(abs(b)) * 5)
#
# # 내가 원하는 영역 지정.
# for width in range(113, 234+1):
#     for height in range(50, 188+1):
#         for bgr in range(0, 2+1):
#             matplot_copy[width, height, bgr] = 255- matplot[width, height, bgr]