#!/usr/bin/env python3

import cv2
def main():
            img = cv2.imread('../images/atlascar.png')
            h, w, c = img.shape
            cx = int(w/2)
            cy = int(h/2)
            cv2.circle(img, (cx, cy), 50, (0, 255, 0), 5)
            cv2.putText(img,
  text = "PSR",
  org = (cx-20, cy-20),
  fontFace = cv2.FONT_HERSHEY_DUPLEX,
  fontScale = 3.0,
  color = (125, 246, 55),
  thickness = 3
)
            cv2.imshow('AtlasCar', img)
            if cv2.waitKey(0) == ord('q'):
                exit



if __name__ == '__main__':
    main()