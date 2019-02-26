
# coding: utf-8

# In[1]:


import numpy as np
from collections import defaultdict


# In[2]:


# 1 means acessible. 0 means not inaccessible

floor = np.array([[1, 1, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1], [0, 0, 1, 1]])
print (floor)


# In[3]:


def test_neighbours(array, i, j):
    '''
    The function is to find out neigbhours that are assessible 
    Input: array - numpy array, i - index, j - index
    Return: neighbours that are accessible - list of tuples
    ''' 
    good_neighbours = []
    neighbours = [[i-1, j], [i+1, j], [i, j-1], [i, j+1]]
    for vertex in neighbours:
        if test_vertex(array, vertex[0], vertex[1]):
            good_neighbours.append((vertex[0], vertex[1]))
    return good_neighbours


# In[4]:


def test_vertex (array, i, j):
    '''
    The function is to find out whether a specific vertex is assessible 
    Input: array - numpy array, i - index, j - index
    Return: true or false
    ''' 
    height = array.shape[0]
    width = array.shape [1]
    if 0<=i<height:
        if 0<=j< width:
            if array[i][j] == 1:
                return 1
    return 0


# In[5]:


def create_graph(array):
    '''
    This is to create graph for further analysis
    Input: array - numpy array
    Return: list of all coordinates in arrary with their accessible neighbours
    '''
    height = array.shape[0]
    width = array.shape [1]
    graph_ = defaultdict(set)
    for i in range (0, height):
        for j in range (0, width):
            graph_[(i, j)] = test_neighbours(array, i, j)
    return graph_


# In[9]:


def identify_route(array, starting_point, ending_point):
    '''
    This is to identify route from starting point to ending point
    Input: array - numpy array, starting_point - coordinate as tuple, 
           ending_point - coordinate as tuple,
    Return: route from starting point to ending point - list of tuples
    '''
    
    visited = []
    route = []

    stack = [starting_point]
    height = floor.shape[0]
    width = floor.shape [1]

    while stack:
        node = stack.pop()
        visited.append(node)
        route.append(node)
        if node == ending_point:
            return route
        else:
            for sub_node in graph[node]: 
                if sub_node not in visited:
                    visited.append(sub_node)
                    stack.append(sub_node)
    return 'No route available'


# In[10]:


graph = defaultdict(set)
graph = create_graph(floor)
graph


# In[11]:


route = identify_route(floor, (0,0), (3,3))
print(route)

