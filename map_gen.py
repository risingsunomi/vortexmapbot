"""
Class that handles generating circle and points of vortex map

Need to map points to how the "map" should be from vortex

https://youtu.be/bU0sT2XZkX0
"""

import numpy as np
import matplotlib.pyplot as plt

class MapGen:
    def __init__(self, points=9, point_radius=0.5, line_paths=[(1,1)]):
        if points < 3:
            raise ValueError("Points must be equal to or more than 3")
        self.points = points
        self.line_paths = line_paths
        self.point_radius = point_radius
        self.circle_points = None

    def get_cmap(self):
        """
        Get a color map to randomize lines
        """
        return plt.cm.get_cmap('hsv', len(self.line_paths))
        

    def build_plot(self):
        theta = np.linspace(0, 2*np.pi, self.points, endpoint=False)
        x = self.point_radius * np.cos(theta)
        y = self.point_radius * np.sin(theta)
        self.circle_points = np.c_[x,y]

        fig, ax = plt.subplots(1)
        ax.scatter(self.circle_points[:, 0], self.circle_points[:, 1])

        cir_x = self.circle_points[:, 0]
        cir_y = self.circle_points[:, 1]

        # get top point of circle and number it from there
        max_y_idx = np.where(cir_y == max(cir_y))[0][0]

        before_x = cir_x[:max_y_idx]
        before_x = before_x[::-1]
        after_x = cir_x[max_y_idx+1:]
        after_x = after_x[::-1]

        before_y = cir_y[:max_y_idx]
        before_y = before_y[::-1]
        after_y = cir_y[max_y_idx+1:]
        after_y = after_y[::-1]

        # ocp - ordered circle points
        ocp_x = np.concatenate((before_x,after_x))
        ocp_x = np.append(ocp_x, [cir_x[max_y_idx]])
        ocp_y = np.concatenate((before_y,after_y))
        ocp_y = np.append(ocp_y, [cir_y[max_y_idx]])
        
        ocp_points = np.c_[ocp_x, ocp_y]

        pointcnt = 1
        for i in range(len(ocp_points)):
            ax.annotate(pointcnt, (ocp_points[:, 0][i], ocp_points[:, 1][i]))
            pointcnt += 1
        
        # plot line paths
        lncnt = 0
        # last_line = [] 
        for line_path in self.line_paths:
            # get px and py to label each point
            px = [ocp_points[:, 0][line_path[0]-1], ocp_points[:, 0][line_path[1]-1]]
            py = [ocp_points[:, 1][line_path[0]-1], ocp_points[:, 1][line_path[1]-1]]

            cmap = self.get_cmap()

            print(px, py)
            
            ax.plot(px, py, marker = 'o', color=cmap(lncnt))

            lncnt += 1
        
        ax.set_aspect('equal')
        plt.show()