import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import math
import numpy as np

from matplotlib.pyplot import figure
from matplotlib.animation import FuncAnimation
from random import randrange

TOTAL_POINTS = 100000 # Total number of plotted points.
SIMULT_POINTS = 100 # Number of points plotted simultaneously.

class Point:
   ratio = 0.5

   def __init__(self, x, y):
      self.x = x
      self.y = y

   def plot(self, plt, size):
      plt.scatter(self.x, self.y, s=size)

   def get_bary(self, point):
      return (Point((Point.ratio * self.x + (1 - Point.ratio) * point.x),
                    (Point.ratio * self.y + (1 - Point.ratio) * point.y)))

def triangle():
   Point.ratio = 0.5
   points = []
   points.append(Point(-100, 0))
   points.append(Point(100, 0))
   points.append(Point(0, 86.6025))
   return points

def diamond():
   Point.ratio = 0.51
   points = []
   points.append(Point(-100, 0))
   points.append(Point(100, 0))
   points.append(Point(0, 86.6025))
   points.append(Point(200, 86.6025))
   return points
   
def pentagon():
   Point.ratio = 1 - 0.381966
   points = []
   points.append(Point(0, 1))
   points.append(Point(np.sin(2*np.pi/5), np.cos(2*np.pi/5)))
   points.append(Point(np.sin(4*np.pi/5), -np.cos(np.pi/5)))
   points.append(Point(-np.sin(4*np.pi/5), -np.cos(np.pi/5)))
   points.append(Point(-np.sin(2*np.pi/5), np.cos(2*np.pi/5)))
   return points

def set_lim(plt, points):
   plt.xlim(min_x(points), max_x(points))
   plt.ylim(min_y(points), max_y(points))

def min_x(points):
   ret = None
   for point in points:
      if ret == None or point.x < ret:
         ret = point.x
   return ret

def max_x(points):
   ret = None
   for point in points:
      if ret == None or point.x > ret:
         ret = point.x
   return ret

def min_y(points):
   ret = None
   for point in points:
      if ret == None or point.y < ret:
         ret = point.y
   return ret

def max_y(points):
   ret = None
   for point in points:
      if ret == None or point.y > ret:
         ret = point.y
   return ret

def generate_coordinates(xcoords, ycoords, points):
   point = Point(0, 86.6025/3) #Point(0, 0)
   for i in range(TOTAL_POINTS):
      point = points[randrange(len(points))].get_bary(point)
      xcoords[i] = point.x
      ycoords[i] = point.y

def animate(i):
   if SIMULT_POINTS * i + 1 > TOTAL_POINTS - 1:
      i = math.floor(TOTAL_POINTS / SIMULT_POINTS)
   graph.set_data(xcoords[:SIMULT_POINTS * i + 1], ycoords[:SIMULT_POINTS * i + 1])
   return graph,

if __name__ == '__main__':

   figures = ["Triangle", "Diamond", "Pentagon"]
   print("What do you want to plot?")
   print("1- " + figures[0])
   print("2- " + figures[1])
   choice = (int(input("3- " + figures[2] + "\n")) - 1) % len(figures)
   
   print("Okay lets plot the " + figures[choice] + ".")
   if (choice == 0):
      points = triangle()
   elif (choice == 1):
      points = diamond()
   elif (choice == 2):
      points = pentagon()
   else:
      points = triangle()
   
   fig = figure(figsize=(16, 12), dpi=80)
   set_lim(plt, points)
   graph, = plt.plot([], [], 'ro', ms=1)
   
   xcoords = [0] * TOTAL_POINTS
   ycoords = [0] * TOTAL_POINTS
   generate_coordinates(xcoords, ycoords, points)
      
   ani = FuncAnimation(fig, animate, interval=1, blit=True, frames=math.floor(TOTAL_POINTS / SIMULT_POINTS))
   # Uncomment those lines to record a video instead of displaying.
   # Don't forget to kill the process to stop the recording. 
   #writervideo = animation.FFMpegWriter(fps=60)
   #ani.save('figure.mp4', writer=writervideo)
   plt.show()
   plt.close()






