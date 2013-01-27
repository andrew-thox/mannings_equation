import unittest
from mannings import ManningsEquation

class ManningsTests(unittest.TestCase):
	"""Tests Mannings Equation calculations, uses dummy arguments if arg not necessary"""
	def setup(self):
		pass

	def test_cross_section(self):
		'''Calculates cross section based on  y(depth), b(width of channel).'''
		m = ManningsEquation(2.4, 12.3, 1, 1, 1)
		self.assertEqual(29.52, m.cross_section)

	def test_wetted_perimeter(self):
		'''Calculates cross section based on y(depth), b(width of channel).'''
		m = ManningsEquation(212, 96, 1, 1, 1)
		self.assertEqual(520, m.wetted_perimeter)

	def test_hydraulic_radius(self):
		'''Calculate hydraulic radius based on y(depth), b(width of channel).'''
		m = ManningsEquation(25.5,60, 1, 1, 1)
		self.assertEqual(13.7837837838, round(m.hydraulic_radius,10))

	def test_avg_velocity(self):
		'''Calculates velocity based on k, n(manning coefficient), s(slope), y(depth), b(width of channel)'''
		m=ManningsEquation(529,10.9,0.012,0.05,1.49)
		self.assertEqual(492419.89, round(m.average_velocity,2))

	def test_flowrate_discharge(self):
		'''Calculates flowrate based on k, n(manning coefficient), s(slope), y(depth), b(width of channel)'''
		m=ManningsEquation(5,10,0.012,0.05,1.49)
		self.assertEqual(51.143, round(m.flowrate,3))


if __name__ == '__main__':
    unittest.main()
