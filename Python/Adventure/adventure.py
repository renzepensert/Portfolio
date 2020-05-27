"""adventure.py: A program to play Crowther’s Adventure game"""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"


# import the Room class from room.py
from room import Room


class Adventure():

    # create rooms and synonyms for the appropriate 'game' version.
    def __init__(self, game):

        # rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        # synonyms is a dicionary that stores all the synonyms and their corresponding commands
        self.synonyms = {}

        # load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # game always starts in room number 1, so we'll set it after loading
        assert "1" in self.rooms
        self.current_room = self.rooms["1"]

    # load rooms from filename in two-step process
    def load_rooms(self, filename):

        # open the file which contains room information
        with open(filename) as f:

            # read the first paragraph of the file
            for info in f:

                # format by strip and split
                info = info.strip("\n")
                info = info.split("\t")

                # stops the loop when the room information ends
                if info[0] == "":
                    break

                # stores the room id, room name and room description into a dictionary
                self.rooms[info[0]] = Room(info[0], info[1], info[2])

            # read the second paragraph for directions
            for dest in f:

                # format by strip and split
                dest = dest.strip("\n")
                dest = dest.split("\t")

                # stops the loop when the room directions information ends
                if dest[0] == "":
                    break

                # checks the total amount of elements in the dest line
                list_length = len(dest)

                # the amount of direction elements in the dest line
                amount_direction = (list_length - 1) / 2

                # go through all the source rooms, directions and destination rooms
                for i in range(int(amount_direction)):

                    # the first element is the source room
                    source_room = self.rooms[dest[0]]

                    # stores the destination rooms
                    destination_room = self.rooms[dest[2+2*i]]

                    # use the add_connection method to store the direction and destination room in the self.connection dictionary
                    source_room.add_connection(dest[1+2*i].lower(), destination_room)

        # assertion, game has to start in the room named "Outside building"
        assert self.rooms["1"].room_name == "Outside building"

    # pass along the description or room name of the current room
    def get_description(self):

        # if it is the first time user enters this room, return room description
        if self.current_room.already_visited() == False:
            return self.current_room.room_des

        # if the user entered this room before, return room name
        else:
            return self.current_room.room_name

    # move to a different room by changing "current" room, if possible
    def move(self, direction):

        # checks if the room has a connection into the direction prompted by the user
        if self.current_room.has_connection(direction) == True:

            # sets the current room to visited
            self.current_room.set_visited()

            # sets the current room to the new room
            self.current_room = self.current_room.get_connection(direction)

            # uses the is_forced method to move when the movement is forced
            self.is_forced()

            # print the description when is_forced is false
            if self.is_forced() == False:
                print(self.get_description())

            return True

        # when the room has no connection into the direction prompted by the user
        print("Invalid command.")
        return False

    # method to return the room description
    def get_long_description(self):
        return self.current_room.room_des

    # checks if the room has a connection called forced and use the forced move
    def is_forced(self):

        if self.current_room.has_connection("forced"):
            print(self.get_long_description())
            self.move("forced")
            return True

        return False

    # load the synonyms file
    def load_synonyms(self):
        with open("data/Synonyms.dat") as synonymfile:
            for synonym in synonymfile:

                # format the synonyms
                synonym = synonym.lower()
                synonym = synonym.strip("\n")
                synonym = synonym.split("=")

                # call the add_synonyms method to store the synonyms in a dictionary
                self.add_synonyms(synonym[0], synonym[1])

    # stores synonyms in the dictionary
    def add_synonyms(self, synonym, command):

        self.synonyms[synonym] = command


if __name__ == "__main__":

    from sys import argv

    # check command line arguments
    if len(argv) not in [1, 2]:
        print("Usage: python adventure.py [name]")
        exit(1)

    # load the requested game or else Tiny
    if len(argv) == 1:
        game_name = "Tiny"
    elif len(argv) == 2:
        game_name = argv[1]

    # create game
    adventure = Adventure(game_name)

    # welcome user
    print("Welcome to Adventure.\n")

    # print very first room description
    print(adventure.get_description())

    # load the synonyms and put them into a dictionary
    adventure.load_synonyms()

    # prompt the user for commands
    while True:

        # prompt
        command = input("> ").lower()

        # handles synonyms
        if command in adventure.synonyms:
            command = adventure.synonyms[command]

        # list with direction commands
        direction_commands = ["north", "east", "south", "west", "in", "out", "up", "down", "forced"]

        # list with game commands
        game_commands = ["quit", "help", "look"]

        if command in direction_commands:
            adventure.move(command)
        elif command in game_commands:
            pass
        else:
            print("Invalid command.")

        # prints the available commands when user types help
        if command.lower() == "help":
            print("You can move by typing directions such as EAST/WEST/IN/OUT")
            print("QUIT quits the game.")
            print("HELP prints instructions for the game.")
            print("LOOK lists the complete description of the room and its contents")

        # prints the description when user types look
        if command.lower() == "look":
            print(adventure.get_long_description())

        # quit, stops the game
        if command == "quit":
            break