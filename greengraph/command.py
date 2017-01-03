from argparse import ArgumentParser
from .graph import Greengraph
from matplotlib import pyplot as plt

def process():
    parser = ArgumentParser(description = "Determine starting and ending locations")
    
    parser.add_argument('--begin', '-b', help = 'The starting location for the map.')
    parser.add_argument('--end', '-e', help = 'The end location for the map.')
    parser.add_argument('--steps', '-s', help = 'The number of steps you would like to use in the calculation')
    parser.add_argument('--out', '-o', help = 'Location to save the graph to')
    
    arguments = parser.parse_args()
    
    mygraph = Greengraph(arguments.begin , arguments.end)
    data = mygraph.green_between(arguments.steps)
    fig = plt.plot(data)
    fig = plt.savefig(arguments.out)
    
if __name__ == "__main__":
    process()