#********************************************************************************************************************
#Exemplary circles and ellipses detection from source:
# stackoverflow.com/questions/32797073/opencv-speed-traffic-sign-detection/32798574#32798574
#written in C, translated to Python
#********************************************************************************************************************
# IplImage* img = NULL;
# if ((img = cvLoadImage(argv[1]))== 0)
# {
#     printf("cvLoadImage failed\n");
# }
#
# IplImage* gray = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);
# CvMemStorage* storage = cvCreateMemStorage(0);
#
# cvCvtColor(img, gray, CV_BGR2GRAY);
#
# // This is done so as to prevent a lot of false circles from being detected
# cvSmooth(gray, gray, CV_GAUSSIAN, 7, 9);
#
# IplImage* canny = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,1);
# IplImage* rgbcanny = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,3);
# cvCanny(gray, canny, 40, 240, 3);
#
# CvSeq* circles = cvHoughCircles(gray, storage, CV_HOUGH_GRADIENT, 2, gray->height/8, 120, 10, 2, 25);
# cvCvtColor(canny, rgbcanny, CV_GRAY2BGR);
#
# for (size_t i = 0; i < circles->total; i++)
# {
#      // round the floats to an int
#      float* p = (float*)cvGetSeqElem(circles, i);
#      cv::Point center(cvRound(p[0]), cvRound(p[1]));
#      int radius = cvRound(p[2]);
#
#      // draw the circle center
#      cvCircle(rgbcanny, center, 3, CV_RGB(0,255,0), -1, 8, 0 );
#
#      // draw the circle outline
#      cvCircle(rgbcanny, center, radius+1, CV_RGB(0,0,255), 2, 8, 0 );
#
#      printf("x: %d y: %d r: %d\n",center.x,center.y, radius);
# }
#
# cvNamedWindow("circles", 1);
# cvShowImage("circles", rgbcanny);
#
# cvSaveImage("out.png", rgbcanny);
# cvWaitKey(0);




IplImage* img = NULL;
if ((img = cvLoadImage(argv[1]))== 0)
{
    printf("cvLoadImage failed\n");
}

IplImage* gray = cvCreateImage(cvGetSize(img), IPL_DEPTH_8U, 1);
CvMemStorage* storage = cvCreateMemStorage(0);

cvCvtColor(img, gray, CV_BGR2GRAY);

// This is done so as to prevent a lot of false circles from being detected
cvSmooth(gray, gray, CV_GAUSSIAN, 7, 9);

IplImage* canny = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,1);
IplImage* rgbcanny = cvCreateImage(cvGetSize(img),IPL_DEPTH_8U,3);
cvCanny(gray, canny, 40, 240, 3);

CvSeq* circles = cvHoughCircles(gray, storage, CV_HOUGH_GRADIENT, 2, gray->height/8, 120, 10, 2, 25);
cvCvtColor(canny, rgbcanny, CV_GRAY2BGR);

for (size_t i = 0; i < circles->total; i++)
{
     // round the floats to an int
     float* p = (float*)cvGetSeqElem(circles, i);
     cv::Point center(cvRound(p[0]), cvRound(p[1]));
     int radius = cvRound(p[2]);

     // draw the circle center
     cvCircle(rgbcanny, center, 3, CV_RGB(0,255,0), -1, 8, 0 );

     // draw the circle outline
     cvCircle(rgbcanny, center, radius+1, CV_RGB(0,0,255), 2, 8, 0 );

     printf("x: %d y: %d r: %d\n",center.x,center.y, radius);
}

cv2.imshow('circles', im)
cv2.waitKey()