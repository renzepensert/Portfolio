/*
 *  Implements Game of Fifteen (generalized to d x d)
 *  Rens Groot
 *  13122304
 */

#define _XOPEN_SOURCE 500
#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9
#define COLOR "\033[32m"

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// variables
int tile_number;
string empty_tile;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }
    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }
    // open log
    FILE *file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }
    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }
        // prompt for move
        int tile = get_int("Tile to move: ");

        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }
        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }
        // sleep thread for animation's sake
        usleep(50000);
    }
    // close log
    fclose(file);

    // success
    return 0;
}
// clears screen using ANSI escape sequences
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}
// greets player
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(2000000);
}
// initializes the game's board with tiles numbered 1 through d*d - 1
// (i.e., fills 2D array with values but does not actually print them)
void init(void)
{
    int tile_number = (d * d) -1;

    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            // set tiles value
            board[i][j]= tile_number - j - (d * i);
            if (d % 2 == 0)
            {
                board[d-1][d-2] = 2;
                board[d-1][d-3] = 1;
            }
            // set the 0 value to 99 to prefend the outer values from moving
            if (board[i][j] == 0)
            {
                board[i][j] = 99;
            }
        }
    }
}
// prints the board in its current state
void draw(void)
{
    // the swappable character
    empty_tile = " _  ";
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            // prints swappable character
            if (board[i][j] == 99)
            {
                printf("%s", empty_tile);
            }
            // prints tile value
            else
            {
                printf("%2i  ", board[i][j]);
            }
        }
        printf("\n");
    }
}
// if tile borders empty space, moves tile and returns true, else returns false
bool move(int tile)
{
    for (int i = 0; i < d; i++)
    {
        for (int j = 0; j < d; j++)
        {
            if (tile == board[i][j])
            {
                if (board[i + 1][j] == 99)
                {
                    board[i + 1][j] = board[i][j];
                    board[i][j] = 99;
                    return true;
                }
                else if (board[i - 1][j] == 99)
                {
                    board[i - 1][j] = board[i][j];
                    board[i][j] = 99;
                    return true;
                }
                else if (board[i][j + 1] == 99)
                {
                    board[i][j + 1] = board[i][j];
                    board[i][j] = 99;
                    return true;
                }
                else if (board[i][j - 1] == 99)
                {
                    board[i][j - 1] = board[i][j];
                    board[i][j] = 99;
                    return true;
                }
            }
        }
    }
    return false;
}
// returns true if game is won (i.e., board is in winning configuration), else false
bool won(void)
{
    for (int i = 0; i < d -1; i++)
    {
        for (int j = 0; j < d - 1; j++)
        {
            if (board[i][j] != board[i+1][j] - d)
            {
                return false;
            }
            if (board[i][j] != board[i][j+1] - 1)
            {
                return false;
            }
        }
    }
    return true;
}
