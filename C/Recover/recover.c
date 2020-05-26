#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <getopt.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage ./recover file\n");
        return 1;
    }

    char *infile = argv[optind];

    // reads input file and gives an error when the file can't be read
    FILE *inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        fprintf(stderr, "Could not open %s.\n", infile);
        return 2;
    }

    unsigned char buffer[BLOCK_SIZE];
    char filename[8];

    // initial value of outpointer
    FILE *outptr = NULL;

    // counter for the filename of the photo
    int counter = 0;

    // runs as long as you can read a block of 512 bytes, so stops at EOF
    while (fread(buffer, BLOCK_SIZE, 1, inptr) == 1)
    {
        // checks if the first blocks are those of a JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // closes the output file when it finds a new JPEG file
            if (outptr != NULL)
            {
                fclose(outptr);
                // counter for the filename of the photo
                counter++;
            }
            // create a JPEG file to write the blocks into
            sprintf(filename, "%03i.jpg", counter);
            outptr = fopen(filename, "w");
        }
        // writes blocks into the outpointer file as long as one is opened
        if (outptr != NULL)
        {
            fwrite(buffer, BLOCK_SIZE, 1, outptr);
        }
    }
    // closes the inpointer and outpointer
    fclose(inptr);
    fclose(outptr);
    return 0;
}
