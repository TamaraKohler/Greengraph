from argparse import ArgumentParser
from .graph import Greengraph
from matplotlib import pyplot as plt

mygraph = Greengraph('New York', 'Chicago')
data = mygraph.green_between(20)

def process():
    parser = ArgumentParser(description = "Compute the green space between two cities")
    
    parser.add_argument('--begin', '-b', help = 'The starting location (for example London)')
    parser.add_argument('--end', '-e', help = 'The end location (for example Oxford)')
    parser.add_argument('--steps', '-s', help = 'The number of steps you would like to use in the calculation (for example 10)')
    parser.add_argument('--out', '-o', help = 'Location to save the graph to (for example graph.png)')
    
    arguments = parser.parse_args()
    
    mygraph = Greengraph(arguments.begin , arguments.end)
    data = mygraph.green_between(arguments.steps)
    plt.plot(data)
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    
if __name__ == "__main__":
    process()