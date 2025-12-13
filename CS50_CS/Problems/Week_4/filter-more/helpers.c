#include "helpers.h"
#include <math.h>
#include <stdlib.h>

typedef uint8_t BYTE;

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE numbers = image[i][j];
            int blue = numbers.rgbtBlue;
            int green = numbers.rgbtGreen;
            int red = numbers.rgbtRed;
            int average = round((blue + green + red) / 3.0);
            image[i][j].rgbtRed = image[i][j].rgbtGreen = image[i][j].rgbtBlue = average;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int counter = width - 1;
    int row = 0;
    for (int i = 0; i < height; i++)
    {
        while (counter > row)
        {
            RGBTRIPLE temp = image[i][row];
            RGBTRIPLE first = image[i][row];
            image[i][row] = image[i][counter];
            image[i][counter] = temp;
            row++;
            counter--;
        }
        counter = width - 1;
        row = 0;
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumblue = 0;
            int sumgreen = 0;
            int sumred = 0;
            int row = i - 1;
            int column = j - 1;
            float counter = 0.0;
            for (int m = 0; m < 3; m++)
            {
                for (int n = 0; n < 3; n++)
                {
                    if (row <= height - 1 && row >= 0 && column >= 0 && column <= width - 1)
                    {
                        sumblue += image[row][column].rgbtBlue;
                        sumgreen += image[row][column].rgbtGreen;
                        sumred += image[row][column].rgbtRed;
                        counter++;
                    }
                    column++;
                }
                row++;
                column -= 3;
            }
            int averageblue = round(sumblue / counter);
            int averagegreen = round(sumgreen / counter);
            int averagered = round(sumred / counter);
            new[i][j].rgbtBlue = averageblue;
            new[i][j].rgbtGreen = averagegreen;
            new[i][j].rgbtRed = averagered;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE new[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
            int green[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
            int red[9] = {0, 0, 0, 0, 0, 0, 0, 0, 0};
            int row = i - 1, column = j - 1, counter = 0;
            for (int m = 0; m < 3; m++)
            {
                for (int n = 0; n < 3; n++)
                {
                    if (row <= height - 1 && row >= 0 && column >= 0 && column <= width - 1)
                    {
                        blue[counter] = image[row][column].rgbtBlue;
                        green[counter] = image[row][column].rgbtGreen;
                        red[counter] = image[row][column].rgbtRed;
                    }
                    counter++;
                    column++;
                }
                row++;
                column -= 3;
            }
            int gx[9] = {-1, 0, 1, -2, 0, 2, -1, 0, 1};
            int gy[9] = {-1, -2, -1, 0, 0, 0, 1, 2, 1};
            int xblue = 0, xgreen = 0, xred = 0, yblue = 0, ygreen = 0, yred = 0;
            for (int w = 0; w < 9; w++)
            {
                xblue += blue[w] * gx[w];
                xgreen += green[w] * gx[w];
                xred += red[w] * gx[w];
                yblue += blue[w] * gy[w];
                ygreen += green[w] * gy[w];
                yred += red[w] * gy[w];
            }
            int newblue = round(sqrt(xblue * xblue + yblue * yblue));
            if (newblue > 255)
                newblue = 255;
            int newgreen = round(sqrt(xgreen * xgreen + ygreen * ygreen));
            if (newgreen > 255)
                newgreen = 255;
            int newred = round(sqrt(xred * xred + yred * yred));
            if (newred > 255)
                newred = 255;
            new[i][j].rgbtBlue = newblue;
            new[i][j].rgbtGreen = newgreen;
            new[i][j].rgbtRed = newred;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = new[i][j];
        }
    }
    return;
}
