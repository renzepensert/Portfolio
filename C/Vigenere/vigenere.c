#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

/*  Created by Rens Groot on 09/02/2020
*   Program that encrypts messages using Vigenère’s cipher
*/

int main(int argc, string argv[])
{
    // tests if user uses one command-line argument
    if (argc != 2)
    {
        printf("Usage: ./vigenere k");
        return 1;
    }
    else
    {
        string input_key = argv[1];

        // gives length of key
        int key_length = strlen(input_key);
        int key[key_length];

        // tests if key only consists of letters
        for (int a = 0; a < key_length; a++)
        {
            if (isalpha(input_key[a]) == 0)
            {
                printf("Usage: ./vigenere k\n");
                return 1;
            }
        }
        // transforms the key to integer and stores them in an array
        // A => 0   a => 0  B => 1  b => 1  etc..
        for (int i = 0; i < key_length; i++)
        {
            if (isupper(input_key[i]) == 0)
            {
                key[i] = ((int)input_key[i]) - 97;
            }
            else
            {
                key[i] = (int)input_key[i] - 65;
            }
        }
        // stores text input of user in string inputText
        string input_text = get_string("Enter text to encipher: \n");

        // gives length of input
        int input_text_length = strlen(input_text);
        int output_key[input_text_length];

        // counter which won't count up when the character isn't a letter
        int counter = 0;

        printf("ciphertext: ");

        // encipher
        for (int c = 0; c < input_text_length; c++)
        {
            // encipher uppercase letters
            if (isupper(input_text[c]) > 0)
            {
                output_key[c] = ((int) input_text[c] + key[(counter % key_length)]) % 90;
                counter = counter + 1;
                if (output_key[c] == 0)
                {
                    output_key[c] = output_key[c] + 90;
                }
                else if (output_key[c] < 65)
                {
                    output_key[c] = output_key[c] + 64;
                }
            }
            // encipher lowercase letters
            else if (islower(input_text[c]) > 0)
            {
                output_key[c] = ((int) input_text[c] + key[(counter % key_length)]) % 122;
                counter = counter + 1;
                if (output_key[c] == 0)
                {
                    output_key[c] = output_key[c] + 122;
                }
                else if (output_key[c] < 97)
                {
                    output_key[c] = output_key[c] + 96;
                }
            }
            // all other characters
            else
            {
                output_key[c] = (int) input_text[c];
            }
            // prints ciphertext
            printf("%c", (char) output_key[c]);
        }
        printf("\n");
        printf("plaintext: %s \n", input_text);
        return 0;
    }
}