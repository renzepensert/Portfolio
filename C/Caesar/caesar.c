#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/*  Created by Rens Groot on 09/02/2020
*   Program that encrypts messages using Caesar’s cipher
*/

int main(int argc, string argv[])
{
    // checks if user used 1 command-line argument
    if (argc != 2)
    {
        printf("Usage: ./caesar k\n");
        return 1;
    }
    else
    {
        // get plaintext from user
        string plain_text = get_string("Enter text to encipher: \n");

        // stores key in a string
        string numkey = argv[1];

        // transforms key to integer
        int key = atoi(numkey);

        // modulus to handle keys above 26
        key = key % 26;

        printf("ciphertext: ");

        // encipher
        for (int i = 0, length = strlen(plain_text); i < length; i++)
        {
            // adds key to uppercase letters
            if (plain_text[i] >= 'A' && plain_text[i] <= 'Z')
            {
                int upper = (((int) plain_text[i]) + key) % 90;
                if (upper == 0)
                {
                    upper = upper + 90;
                }
                else if (upper < 65)
                {
                    upper = upper + 64 ;
                }
                printf("%c", (char)upper);
            }
            // adds key to lowercase letters
            else if (plain_text[i] >= 'a' && plain_text[i] <= 'z')
            {
                int lower = (((int) plain_text[i]) + key) % 122;
                if (lower == 0)
                {
                    lower = lower + 122;
                }
                else if (lower < 97)
                {
                    lower = lower + 96;
                }
                printf("%c", (char)lower);
            }
            // print all the other characters like they were entered by the user
            else
            {
                printf("%c", plain_text[i]);
            }
        }
        printf("\n");
        return 0;
        printf("plaintext: %s \n", plain_text);
    }

}