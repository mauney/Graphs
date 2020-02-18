
def get_parents(ancestors, node):
    parents = []
    for pair in ancestors:
        if pair[1] == node:
            parents.append(pair[0])
    return parents


def earliest_ancestor(ancestors, starting_node):
    # make a tree from the starting_node

    # create an empty queue and an empty paths list
    q = []
    paths = []
    # add a path to the starting node to the queue
    q.append([starting_node])
    # while the queue is not empty
    while q:
        # dequeue the first path
        path = q.pop(0)
        # grab the last ancestor from the path
        current = path[-1]
        # add a path to all neighbors to the back of the queue
        # if no ancestors, store path
        parents = get_parents(ancestors, current)
        if parents:
            for parent in parents:
                q.append(path + [parent])
        else:
            paths.append(path)

    # find length of longest path(s)
    max_len = max(len(path) for path in paths)
    # if the tree consists solely of the starting_node, return -1
    if max_len <= 1:
        return -1

    # return the last node with the lowest value from theses paths
    max_len = max(len(path) for path in paths)
    oldest = [path[-1] for path in paths if len(path) == max_len]
    return min(oldest)
