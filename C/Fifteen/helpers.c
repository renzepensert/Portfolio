/*
 *  program that finds a number among numbers
 *  Rens Groot
 *  13122304
 */

#include <cs50.h>
#include <stdio.h>
#include "helpers.h"

// binairy search function
bool search(int value, int values[], int n)
{
    int start = 0;
    int end = n - 1;
    int middle = (start + end) / 2;
    while (start <= end)
    {
        if (value == values[middle])
        {
            return true;
        }
        else if (value < values[middle])
        {
            end = middle - 1;
            middle = (start + end) / 2;
        }
        else if (value > values[middle])
        {
            start = middle + 1;
            middle = (start + end) / 2;
        }
        else
        {
            return false;
        }
    }
    return false;
}
// bubblesorts array of n values
void sort(int values[], int n)
{
    for (int i = 0; i < (n - 1); ++i)
    {
        for (int j = 0; j < n - 1 - i; ++j )
        {
            if (values[j] > values[j+1])
            {
                int temp = values[j+1];
                values[j+1] = values[j];
                values[j] = temp;
            }
        }
    }
    return;
}
