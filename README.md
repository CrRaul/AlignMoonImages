# Align Moon Images

Run: python3 main.py input

This is an easy Python program that I wrote to create a Lunar eclipse timelapse without using an equatorial mount.

The most important step: pictures, that’s why I’ve took one every 5 minutes for 2 hours during the partial Lunar eclipse that occurred on 16 July 2019.

An equatorial mount helps to automatically track objects in the sky. So, not having one, in this case, the Moon would be in different positions in each frame. To solve this I wrote this script that cuts the images and at the end, the Moon will be in the center of each frame.


I can describe the logic behind it in a few steps:

1. Upload edited( color adjustment – Lightroom) images;
2. Convert them to Black and White;
3. On BW images apply a Hough Transform and save the center of detected circles;
4. Crop the original images according to the outputs from step 3;
5. Export cropped images;


![gi](https://github.com/CrRaul/centerCropRoundObj/blob/master/output_MiOQEV.gif)\
