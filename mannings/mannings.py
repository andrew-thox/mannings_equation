# coding: utf-8
from __future__ import division
import math

class ManningsEquation(object):
	'''	Gauckler–Manning formula, used to estimate flow in an open channel.
		A = Flow cross-sectional area, determined normal (perpendicular) to the bottom surface.
		b = Channel bottom width.
		F = Froude number.
		g = acceleration due to gravity = 32.174 ft/s2 = 9.8066 m/s2.
		k = unit conversion factor = 1.49 if English units = 1.0 if metric units.
		n = Manning coefficient.  n is a function of the culvert material, such as plastic, concrete, brick, etc.
		P = Wetted perimeter.  P is the contact length (in the cross-section) between the water and the culvert.
		Q = Discharge or flowrate.
		R = Hydraulic radius of the flow cross-section
		S = Slope of channel bottom or water surface.  Vertical distance divided by horizontal distance.
		V = Average velocity of the water.
		y = Water depth measured normal (perpendicular) to the bottom of the culvert.  
			If the culvert has a small slope (S), then entering the vertical depth introduces only minimal error.'''

	def __init__(self,y,b,n,S,k=1.0,g=9.8066):
		self.cross_section = self.__calculate_cross_section(b,y)
		self.wetted_perimeter = self.__calculate_wetted_perimeter(b,y)
		self.hydraulic_radius = self.__calculate_hydraulic_radius(self.cross_section, self.wetted_perimeter)
		self.average_velocity = self.__calculate_average_velocity(self.cross_section,k,n,self.hydraulic_radius,S)
		self.froude_number = self.__calculate_froude_number(self.average_velocity, g, y, S)
		self.flowrate =  self.__calculate_flowrate(self.average_velocity, self.cross_section)

	def __calculate_cross_section(self, b, y):
		A=y*b
		return A
	def __calculate_wetted_perimeter(self, b, y):
		P=(2*y)+b
		return P
	def __calculate_hydraulic_radius(self, A, P):
		R=A/P
		return R
	def __calculate_average_velocity(self,A,k,n,R,S):
		V=(k/n)*A*(R**(2/3))*(S**(1/2))
		return V
	def __calculate_froude_number(self,V,g,y,S):
		F=V/math.sqrt(g*y*math.cos(math.tan(-1)*S))
		return F
	def __calculate_flowrate(self,V,A):
		Q=V/A
		self.Q = Q
		return Q