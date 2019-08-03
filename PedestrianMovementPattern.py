
## @package PedestrianMovementPattern
#

import numpy as np
import Vector
import Geometry
import os
import sys
import json
from DynamicObstacles import DynamicObstacle
import MovementPattern


def ped_movement(env):
	H_pix2meter = np.array([
		[2.8128700e-02, 2.0091900e-03, -4.6693600e+00],
		[8.0625700e-04, 2.5195500e-02, -5.0608800e+00],
		[3.4555400e-04, 9.2512200e-05,  4.6255300e-01]
	])
	H_meter2pix = np.linalg.inv(H_pix2meter)

	with open('obsmat.json', 'r') as f:
		obsmat = json.load(f)
		time_offset = obsmat[str(env.cmdargs.ped_id_to_replace)][0]['time'] if env.cmdargs.ped_id_to_replace > 0 else 0
		for ped_id in obsmat:
			if ped_id != str(env.cmdargs.ped_id_to_replace):
				continue

			path_list = []
			firstpoint = obsmat[ped_id][0]
			path_list.append((-1000, -1000, firstpoint['time']-time_offset))
			for waypoint in obsmat[ped_id]:
				#pos = Geometry.apply_homography(H_meter2pix, (waypoint['pos_x'], waypoint['pos_y']))
				pos = (waypoint['pos_x'], waypoint['pos_y'])
				# Rotate 90 degrees to match video
				path_list.append((pos[1], pos[0], waypoint['time']-time_offset))

			# Get obstacles offscreen after they finish their path
			path_list.append((-1000, -1000, path_list[-1][2]+0.01))

			ped_mover = MovementPattern.PathMovement(path_list, loop=False)
	return ped_mover
