#!/usr/bin/env python

class Decision_tree:
	def __innit__(self):
		pass
	
	def update(self, distances, where_is_human, how_far_is_human, ): # this takes all inputs from all sensors etc.
		state_var = 0
		d_threshold = 1
		if (state_var) == 0:
			if where_is_human == None or how_far_is_human == None:
				state_var = 1
			if distances[0] < d_threshold:
				state_var = 2
		 
		elif(state_var) == 1:
			pass
		elif(state_var) == 2:
			pass
		elif(state_var) == 3:
			pass
		elif(state_var) == 4:
			pass
		else:
			pass
		
