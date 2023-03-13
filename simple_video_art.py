import cv2 as cv

video_file = 'data_PETS09-S2L1-raw.webm'

video = cv.VideoCapture(video_file)

if video.isOpened():
    fps = video.get(cv.CAP_PROP_FPS)
    wait_msec = int(1 / fps * 1000)

    while True:
        valid, img = video.read()
        if not valid:
            break

        edge = cv.Laplacian(img, -1)
        edge = 255 - edge
        #img = cv.bitwise_and(img, edge)
        cv.imshow('Video Player', edge)

        key = cv.waitKey(wait_msec)
        if key == 27: # ESC
            break

    cv.destroyAllWindows()
