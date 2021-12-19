import cv2


def show():
    # img = cv2.imread("galaxy.jpg", 1)
    #
    # print(type(img))
    # print(img)
    # print(img.shape)
    # print(img.ndim)

    img = cv2.imread("galaxy.jpg", 0)

    print(type(img))
    print(img)
    print(img.shape)
    print(img.ndim)

    # resized_image = cv2.resize(img, (1000, 500))
    # resized_image = cv2.resize(img, (500, 1000))
    resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
    # cv2.imshow("Galaxy", img)
    cv2.imshow("Galaxy", resized_image)
    cv2.imwrite("Galaxy_Resized.jpg", resized_image)

    # 0 değeri kullanmak daha mantıklı
    # 5000 milisaniye = 5 saniye
    cv2.waitKey(5000)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    show()
