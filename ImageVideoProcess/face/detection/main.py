# https://github.com/Itseez/opencv/tree/master/data/haarcascades
import cv2


def runScript():
    c = input("Foto Seçiniz : ")
    if c == "news":
        sf = 1.1 # 1.05 olduğunda seçimi tam oluşturamıyor
    else:
        sf = 1.05

    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    img = cv2.imread(c + ".jpg")

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray_img,
        scaleFactor=sf,  # 5% düşürerek boyutlandırma
        minNeighbors=5
    )

    print(type(faces))

    # [[157  84 379 379]]
    # row = 157, column = 84, height = 379, width = 379 olan bir dikdörtgende yüz (face) bulundu
    print(faces)

    for x, y, w, h in faces:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

    resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

    # cv2.imshow("Gray", gray_img)
    # cv2.imshow("Gray", img)
    cv2.imshow(c.upper(), resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    runScript()
