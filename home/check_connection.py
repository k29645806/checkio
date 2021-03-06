network = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")
first = "scout2"
second = "scout3"

network_1 = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")
first_1 = "dr101"
second_1 = "sscout"

network_2 = ("a-b","c-d","b-c")
first_2 = "a"
second_2 = "d"

def cvtNetwork(network):
    network_list = []
    for conn in network:
        network_list.append(conn.split('-'))
    network = map(set,network_list)
    return network


def checkIfConnected(connection,group):
    connection, group = set(connection), set(group)
    inGroup = group.intersection(connection)
    if inGroup:
        new_group = group | connection
        return True, new_group
    else:
        return False, group

def is_intersection(group):
    for i,subGroupA in enumerate(group):
        for subGroupB in group[i+1::]:
            isGroup, _ = checkIfConnected(subGroupA,subGroupB)
            if isGroup:
                return True
                break
    return False

def groupTogether(network):
    while is_intersection(network):
        index, group = 0, {}
        for conn in network:
            while True:
                try:
                    inGroup, newGroup = checkIfConnected(conn,group[index])
                    if inGroup:
                        group[index] = newGroup
                        break
                    else:
                        index += 1
                except KeyError:
                    group[index] = conn
                    break
        network = group.values()
    return network

def check_connection(network, first, second):
    network = cvtNetwork(network)
    network = groupTogether(network)
    for subGroup in network:
        if (first in subGroup) and (second in subGroup):
            return True
            break
    return False


print check_connection(network_1,first_1,second_1)



#----------------------------------------------------------------------------#
'''
network = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")
first = "scout2"
second = "scout3"

network_1 = ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
     "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super")
first_1 = "dr101"
second_1 = "sscout"

network_2 = ("a-b","c-d","b-c")
first_2 = "a"
second_2 = "d"

def check_connection(network, first, second):

    def checkIfConnected(connection,group):
        connection, group = set(connection), set(group)
        inGroup = group.intersection(connection)
        if inGroup:
            new_group = group | connection
            return True, new_group
        else:
            return False, group

    network_list = []
    for conn in network:
        network_list.append(conn.split('-'))
    print network_list,'\n'

    group = {}
    for conn in network_list:
        index = 0
        while True:
            try:
                inGroup, newGroup = checkIfConnected(conn,group[index])
                if inGroup:
                    group[index] = newGroup
                    break
                else:
                    index += 1
            except KeyError:
                group[index] = conn
                break
    print group
    # Check subGroup if there is connection




    for subGroup in group.values():
        if (first in subGroup) and (second in subGroup):
            return True
            break
    return False

print check_connection(network_2, first_2, second_2)
'''
