import cv2


def convert_to_gray(image):
    """
    カラー画像をグレースケールへ変換する
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    return gray


def save_image(image, output_path):
    """
    画像を保存する
    """

    cv2.imwrite(str(output_path), image)


def convert_to_binary(gray_image):
    """
    グレースケール画像を二値化する
    """

    _, binary = cv2.threshold(
        gray_image,
        150,
        255,
        cv2.THRESH_BINARY
    )

    return binary


def detect_contours(binary_image):
    """
    二値画像から輪郭を取得する
    """

    contours, hierarchy = cv2.findContours(
        binary_image,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    return contours