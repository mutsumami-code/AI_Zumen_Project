import cv2


def get_contour_area(contour):
    """
    輪郭の面積を取得する
    """

    area = cv2.contourArea(contour)

    return area