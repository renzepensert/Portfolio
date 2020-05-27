"""room.py: A class that creates room objects and handles their connections"""

__author__ = "Rens Groot"
__studentNumber__ = "13122304"


class Room():

    # create room objects
    def __init__(self, room_id, room_name, room_des):

        # room identification number
        self.room_id = room_id

        # room name
        self.room_name = room_name

        # room description
        self.room_des = room_des

        # dictionary of the rooms connections
        self.connection = {}

        # sets the initializion of visited to false
        self.visited = False

    # stores direction and room in the dictionary
    def add_connection(self, direction, room):

        self.connection[direction] = room

    # checks whether there is a connection in the dictionary under that name
    def has_connection(self, direction):

        if direction in self.connection:
            return True
        return False

    # returns the room the user is directing to
    def get_connection(self, direction):

        if direction in self.connection:
            return self.connection[direction]

    # marks room as visited
    def set_visited(self):

        self.visited = True

    # returns True if room is already visited, returns False if room is not visited
    def already_visited(self):

        if self.visited == True:
            return True
        return False