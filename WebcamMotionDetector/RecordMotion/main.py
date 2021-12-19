from datetime import datetime

import cv2
import pandas
import time


def captureVideo():
    df = pandas.DataFrame(columns=["Start", "End"])
    first_frame = None
    video = cv2.VideoCapture(0)
    check, frame = video.read()
    status_list = [None, None]
    times = []
    status = 0

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
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            if first_frame is None:
                first_frame = gray
                continue

            delta_frame = cv2.absdiff(first_frame, gray)
            thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

            (_, cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cnts:
                if cv2.contourArea(contour) < 10000:  # 100 x 100 px
                    continue
                status = 1
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

            status_list.append(status)
            if status_list[-1] == 1 and status_list[-2] == 0:
                times.append(datetime.now())

            if status_list[-1] == 0 and status_list[-2] == 1:
                times.append(datetime.now())

            # time.sleep(3)
            cv2.imshow("Gray Frame", gray)
            cv2.imshow("Delta Frame", delta_frame)
            cv2.imshow("Thresh Delta Frame", thresh_frame)
            cv2.imshow("Color Frame", frame)

            # 2000 milisaniye = 2 saniye aralıkla yakalar
            # Değer 1 milisaniye yani cv2.waitKey(1) yaparsak sürekli yakalama yapar
            key = cv2.waitKey(2000)

            # q'ya basılmazsa waitKey değeri kadar döngüde video yakalamaya devam eder
            if key == ord('q'):
                if status == 1:
                    times.append(datetime.now())
                break

    else:
        print("Kamera Bulunamadı!")

    print(status_list)
    print(times)

    for i in range(0, len(times), 2):
        df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

    df.to_csv("Times.csv")

    print(a)
    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    captureVideo()
