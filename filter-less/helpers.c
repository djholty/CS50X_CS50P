#include "helpers.h"
//#include "math.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;
            float grey = (blue + green + red) / 3.0;
            grey = round(grey);
            image[i][j].rgbtBlue = grey;
            image[i][j].rgbtGreen = grey;
            image[i][j].rgbtRed = grey;

        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalBlue = image[i][j].rgbtBlue;
            int originalGreen = image[i][j].rgbtGreen;
            int originalRed = image[i][j].rgbtRed;

            float sepiaRed = .393 * originalRed + .769 * originalGreen + .189 * originalBlue;
            float sepiaGreen = .349 * originalRed + .686 * originalGreen + .168 * originalBlue;
            float sepiaBlue = .272 * originalRed + .534 * originalGreen + .131 * originalBlue;

            sepiaRed = round(sepiaRed);
            sepiaGreen = round(sepiaGreen);
            sepiaBlue = round(sepiaBlue);

            // assign the pixel colors the new sepia color, or if it's above 255, then 255
            image[i][j].rgbtBlue = fminf(sepiaBlue, 255.0);
            image[i][j].rgbtGreen = fminf(sepiaGreen, 255.0);
            image[i][j].rgbtRed = fminf(sepiaRed, 255.0);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        float halfway = width / 2.0;
        halfway = floor(halfway); // this covers the case where the width is odd is length and also works for even length widths
        for (int j = 0 ; j < halfway; j++)
        {
            RGBTRIPLE temp; // create temporary pixel
            temp = image[i][j]; // save the first pixel on left in temp
            image[i][j] = image[i][width - 1 - j]; // assign last pixel to first pixel on left
            image[i][width - 1 - j] = temp;//assign opposite pixel to temp
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //create a temporary image array so that when you modify the pixels of the actual image, it doesn't alter pixels up ahead
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    //now iterate through the pixels of the copy, then alter the pixels of the actual image


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // UpperLeft is i-1, j-1
            // Upper is i-1, j
            // UpperRight is i-1, j+1
            // Left is i, j-1
            // Pixel in question is i,j
            // Right is i, j+1
            // LowerLeft is i+1, j-1
            // Lower is i+1, j
            // LowerRight is i+1, j+1

            //initialise the variables at 0 for each pixel
            float counter = 0;
            int totalBlue = 0;
            int totalGreen = 0;
            int totalRed = 0;

            // Check the UpperLeft pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            int row = i - 1;
            int col = j - 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }

            // Check the Upper pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i - 1;
            col = j;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }

            // Check the UpperRight pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i - 1;
            col = j + 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }
            // Check the Left pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i;
            col = j - 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }
            // Check the Current pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i;
            col = j;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }
            // Check the Right pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i;
            col = j + 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }

            // Check the LowerLeft pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i + 1;
            col = j - 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }
            // Check the Lower pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i + 1;
            col = j;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }
            // Check the LowerRight pixel, if it exists, add the value of its pixels for the final averaging and assignment to the pixel
            row = i + 1;
            col = j + 1;
            if (row > -1 && row < height && col > -1 && col < width)
            {
                int blue = copy[row][col].rgbtBlue;
                int green = copy[row][col].rgbtGreen;
                int red = copy[row][col].rgbtRed;
                totalBlue += blue;
                totalGreen += green;
                totalRed += red;
                counter++;
            }

            //do the calculations of the average for each color of the surrounding pixels and assign to the image pixel
            printf("%d\t%f\n", totalBlue, counter);

            float avgblue, avggreen, avgred;
            avgblue = totalBlue / counter;
            //printf("%f\n", avgblue);
            avgblue = round(avgblue);
            //printf("%f\n", avgblue);
            avggreen = totalGreen / counter;
            avggreen = (int)(round(avggreen));
            avgred = totalRed / counter;
            avgred = (int)(round(avgred));


            image[i][j].rgbtBlue = avgblue;
            //printf("%d\n", image[i][j].rgbtBlue);
            image[i][j].rgbtGreen = avggreen;
            image[i][j].rgbtRed = avgred;
        }
    }

    return;
}
