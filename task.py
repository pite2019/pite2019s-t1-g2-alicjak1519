class Car():

	def __init__(self):
		print("START")
		self.wheel_angle = 0
		self.speed = 0
	
	def __del__(self):
		print("STOP")

	def act(self, event):
		print("obstacle - 1, pedestrian - 2, turning - 3")
		input(event)
		
		if event == 1:
			self.wheel_angle += 90
			self.speed = 10
		elif event == 2:
			self.speed = 0
		else:
			self.speed -= 5
			self.wheel_angle += 90


car1 = Car()


for i in range(0,3):

	print("obstacle - 1, pedestrian - 2, turning - 3")
	event = input()
	car1.act(event)
	print("Actual speed is: {}".format(car1.speed))
	print("Actual wheel angle is: {}".format(car1.wheel_angle))

	

