import matplotlib.pyplot as plt
import numpy as np

# Function Definition
# *args: variable length arguments equivalent to varargs in JAVA
# and is generally a list of variable length arguments passed in function call
# **kwargs: key word variable length arguments which is a dictionary of key value
# pairs passed as arguments in function call


def blog_posts(title, *args, **kwargs):
    print("Title:", title)

    for i in range(len(args)):
        print("Post_{}:".format(i), args[i])

    for post_title, post_value in kwargs.items():
        print("SubPost_Title:", post_title, '\n \a', post_value)


blog_posts("Computer Science", 'CS is awesome', 'I am software developer', 'I am also a Data Scientist',
           Beginning='c++', Professional='Python', Intermmediate='Modern Web Development')


# graph_me = [[2,6,8,9,10,45,78],[np.random.randint(20,100,7]]
# *graph_me makes graph_me to break as x1 and y1 2 parts into x and y respectively in plotter


def plotter(x,y):
    plt.scatter(x,y)
    plt.show()


x1 = [2,6,8,9,10,45,78]
y1 = np.random.randint(20,100,7)

graph_me = [x1,y1]

plotter(*graph_me)





