# -*- coding: utf-8 -*-
import cv2

import numpy as np
import time


def abc():
    imagepath = '123.jpg'
    imagepath = 'all_01.jpg'
    image = cv2.imread(imagepath)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # cv2.imshow("Image Title",img2)
    # cv2.waitKey(0)

    faces = face_cascade.detectMultiScale(img2, scaleFactor=1.15, minNeighbors=5, minSize=(5, 5), )
    # faces = face_cascade.detectMultiScale(img2, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

    print("发现{0}个人脸!".format(len(faces)))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + w), (0, 255, 0), 2)

    cv2.imshow("Image Title", image)
    cv2.waitKey(0)


def mathc_img(image, Target, value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7, 249, 151), 2)
    cv2.imshow('Detected', img_rgb)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def pp():
    # 0号摄像头，也可以1、2，lsusb查看
    cap = cv2.VideoCapture(0)

    # 设置分辨率
    cap.set(3, 1280)
    cap.set(4, 1024)
    time.sleep(2)  # 必须要此步骤，否则失败
    cap.set(15, -8.0)

    # 只能是如下选择分辨率.
    # 160.0 x 120.0
    # 176.0 x 144.0
    # 320.0 x 240.0
    # 352.0 x 288.0
    # 640.0 x 480.0
    # 1024.0 x 768.0
    # 1280.0 x 1024.0

    # fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    # fourcc = cv2.cv.FOURCC(*'CVID')
    # out = cv2.VideoWriter(filePath, fourcc, fps, size)

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame, 0)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2BGR)
            # cv2.imshow('iframe', gray)
            cv2.imshow('iframe', frame)
            # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # cv2.imshow('iframe', gray)
            # out.write(gray)
            # cv2.waitKey(0)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    # out.release()
    cv2.destroyAllWindows()


def getCam():
    # 创建摄像头对象
    # 使用opencv自带的Videocapture()函数定义摄像头对象,0表示第一个摄像头,一般是笔记本内摄像头
    cap = cv2.VideoCapture(0)
    # 逐帧显示实现视频播放
    while (1):
        # 一帧一帧获取图像
        # cap.read() 返回一个布尔值（True/False）。如果帧读取的是正确的，
        # 就是True。所以最后你可以通过检查他的返回值来查看视频文件是否已经到了结尾
        ret, frame = cap.read()
        # 一帧一帧显示图像
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cap.destroyAllWindows()


image = 'all_01.jpg'
Target = ('guo.jpg')
value = 0.9
# mathc_img(image,Target,value)

# abc()
# pp()
getCam()
