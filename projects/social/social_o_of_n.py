import random

class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f'User {i+1}')

        # Create friendships
        # for N friendships
        N = num_users * avg_friendships // 2
        while N > 0:
            # pick a couple of people at random
            pair = random.sample(range(1, self.last_id + 1), 2)
            # if they are not friends, make it so and decrement N
            if pair[1] not in self.friendships[pair[0]]:
                N -= 1
                self.add_friendship(pair[0], pair[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # BFTs starting at user_id, return first path to every reachable person
        q = [[user_id]]
        while q:
            path = q.pop(0)
            person = path[-1]
            # add the person and the path to the person
            for friend in self.friendships[person]:
                if friend not in visited and friend != user_id:
                    q.append(path + [friend])
                    visited[friend] = path + [friend]

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.users)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    sg2 = SocialGraph()
    num_users = 1000
    avg_friends = 5
    sg2.populate_graph(num_users, avg_friends)
    avg_portion_connections = 0

    count_connections = 0
    count_connection_degrees = 0

    for i in range(1, num_users + 1):
        connections = sg2.get_all_social_paths(i)
        avg_portion_connections += len(connections) / num_users
        for connection in connections.values():
            count_connections += 1
            count_connection_degrees += len(connection) - 1
    
    percent = 100 * avg_portion_connections / num_users
    print(f'percentage of other users in network: {percent:.2f}%')

    print(f'count_connections: {count_connections}')
    print(f'count_connection_degrees: {count_connection_degrees}')
    avg_degrees = count_connection_degrees / count_connections
    print(f'avg_dgrees {avg_degrees}')

    
