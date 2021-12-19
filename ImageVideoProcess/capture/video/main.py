import cv2
import time


def captureVideo():
    video = cv2.VideoCapture(0)
    check, frame = video.read()

    # False     = Kamera Bulunamadı
    # True      = Kamera Bulundu
    print(check)

    # Kamera bulunduysa matris olarak video boyutları
    # Kamera bulunamadıysa None değeri döner
    print(frame)

    a = 0
    if check:
        while True:
            a += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # time.sleep(3)
            cv2.imshow("Capturing", gray)

            # 2000 milisaniye = 2 saniye aralıkla yakalar
            # Değer 1 milisaniye yani cv2.waitKey(1) yaparsak sürekli yakalama yapar
            key = cv2.waitKey(2000)

            # q'ya basılmazsa waitKey değeri kadar döngüde video yakalamaya devam eder
            if key == ord('q'):
                break
    else:
        print("Kamera Bulunamadı!")

    print(a)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    captureVideo()
