/*
 *      program that applies filters to BMPs
 *      Rens Groot
 *      13122304
 */

#include "helpers.h"
#include <math.h>

// convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            int green = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            int blue = round((image[i][j].rgbtRed + image[i][j].rgbtBlue + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtRed = red;
            image[i][j].rgbtGreen = green;
            image[i][j].rgbtBlue = blue;
        }
    }
    return;
}

// convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            // make sure the colorvalues don't exceed 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
            return;
}

// reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int tempRed[height][width];
    int tempGreen[height][width];
    int tempBlue[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            tempRed[i][j] = image[i][j].rgbtRed;
            tempGreen[i][j] = image[i][j].rgbtGreen;
            tempBlue[i][j] = image[i][j].rgbtBlue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tempRed[i][width -j - 1];
            image[i][j].rgbtGreen = tempGreen[i][width -j - 1];
            image[i][j].rgbtBlue = tempBlue[i][width -j - 1];
        }
    }
    return;
}

// blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int tempRed[height][width];
    int tempGreen[height][width];
    int tempBlue[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (i > 0 && i < height - 1)
            {
                // the middle pixels (not borders or corners)
                if (j > 0 && j < width - 1)
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed + image[i - 1][j].rgbtRed
                    + image[i][j + 1].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j + 1].rgbtRed
                    + image[i - 1][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed + image[i - 1][j + 1].rgbtRed) / 9.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen + image[i - 1][j].rgbtGreen
                    + image[i][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen
                    + image[i - 1][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen + image[i - 1][j + 1].rgbtGreen) / 9.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue + image[i - 1][j].rgbtBlue
                    + image[i][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue
                    + image[i - 1][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue + image[i - 1][j + 1].rgbtBlue) / 9.0);
                }
            }
            // top row
            if (i == 0)
            {
                // upper left corner
                if (j == 0)
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed
                    + image[i][j + 1].rgbtRed  + image[i + 1][j + 1].rgbtRed) / 4.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen
                    + image[i][j + 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen) / 4.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue
                    + image[i][j + 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue) / 4.0);
                }
                // upper right corner
                else if (j == width - 1)
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed
                    + image[i][j - 1].rgbtRed + image[i + 1][j - 1].rgbtRed) / 4.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen
                    + image[i][j - 1].rgbtGreen + image[i + 1][j - 1].rgbtGreen) / 4.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue
                    + image[i][j - 1].rgbtBlue + image[i + 1][j - 1].rgbtBlue) / 4.0);
                }
                // the rest of the top row
                else
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed
                    + image[i][j + 1].rgbtRed + image[i][j - 1].rgbtRed + image[i + 1][j + 1].rgbtRed
                    + image[i + 1][j - 1].rgbtRed) / 6.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen
                    + image[i][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i + 1][j + 1].rgbtGreen
                    + image[i + 1][j - 1].rgbtGreen) / 6.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue
                    + image[i][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i + 1][j + 1].rgbtBlue
                    + image[i + 1][j - 1].rgbtBlue) / 6.0);
                }
            }
            // last row
            if (i == height - 1)
            {
                // bottom left corner
                if (j == 0)
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed
                    + image[i][j + 1].rgbtRed  + image[i - 1][j + 1].rgbtRed) / 4.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen
                    + image[i][j + 1].rgbtGreen + image[i - 1][j + 1].rgbtGreen) / 4.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue
                    + image[i][j + 1].rgbtBlue + image[i - 1][j + 1].rgbtBlue) / 4.0);
                }
                // bottom right corner
                else if (j == width - 1)
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed
                    + image[i][j - 1].rgbtRed + image[i - 1][j - 1].rgbtRed) / 4.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen
                    + image[i][j - 1].rgbtGreen + image[i - 1][j - 1].rgbtGreen) / 4.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i-1][j].rgbtBlue
                    + image[i][j - 1].rgbtBlue + image[i - 1][j - 1].rgbtBlue) / 4.0);
                }
                // the rest of the bottom row
                else
                {
                    tempRed[i][j] = round((image[i][j].rgbtRed + image[i - 1][j].rgbtRed
                    + image[i][j + 1].rgbtRed + image[i][j - 1].rgbtRed + image[i - 1][j + 1].rgbtRed
                    + image[i - 1][j - 1].rgbtRed) / 6.0);

                    tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i - 1][j].rgbtGreen
                    + image[i][j + 1].rgbtGreen + image[i][j - 1].rgbtGreen + image[i - 1][j + 1].rgbtGreen
                    + image[i - 1][j - 1].rgbtGreen) / 6.0);

                    tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i - 1][j].rgbtBlue
                    + image[i][j + 1].rgbtBlue + image[i][j - 1].rgbtBlue + image[i - 1][j + 1].rgbtBlue
                    + image[i - 1][j - 1].rgbtBlue) / 6.0);
                }
            }
            // left column
            if (j == 0 && i > 0 && i < height - 1)
            {
                tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed
                + image[i][j + 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j + 1].rgbtRed
                + image[i + 1][j + 1].rgbtRed) / 6.0);

                tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen
                + image[i][j + 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j + 1].rgbtGreen
                + image[i + 1][j + 1].rgbtGreen) / 6.0);

                tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue
                + image[i][j + 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j + 1].rgbtBlue
                + image[i + 1][j + 1].rgbtBlue) / 6.0);
            }
            // right column
            if (j == width - 1 && i > 0 && i < height - 1)
            {
                tempRed[i][j] = round((image[i][j].rgbtRed + image[i + 1][j].rgbtRed
                + image[i][j - 1].rgbtRed + image[i - 1][j].rgbtRed + image[i - 1][j - 1].rgbtRed
                + image[i + 1][j - 1].rgbtRed) / 6.0);

                tempGreen[i][j] = round((image[i][j].rgbtGreen + image[i + 1][j].rgbtGreen
                + image[i][j - 1].rgbtGreen + image[i - 1][j].rgbtGreen + image[i - 1][j - 1].rgbtGreen
                + image[i + 1][j - 1].rgbtGreen) / 6.0);

                tempBlue[i][j] = round((image[i][j].rgbtBlue + image[i + 1][j].rgbtBlue
                + image[i][j - 1].rgbtBlue + image[i - 1][j].rgbtBlue + image[i - 1][j - 1].rgbtBlue
                + image[i + 1][j - 1].rgbtBlue) / 6.0);
            }
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = tempRed[i][j];
            image[i][j].rgbtGreen = tempGreen[i][j];
            image[i][j].rgbtBlue = tempBlue[i][j];
        }
    }
    return;
}
