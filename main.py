global ADD
ADD = lambda x,y, x1,y1:(x+x1,y+y1)


class Circle:
	def __init__(self, radius=50, x=0, y=0):
		self.radius = radius
		self.x = x
		self.y = y

		self.pendingForces = [0,0]
		self.speed = [0,0]

	def update(self):
		#Do stuff here to calculate the next x and y
		self.speed[0] += self.speed[0]
		self.speed[1] += self.speed[1]

		self.x += speed[0]
		self.y += speed[1]

	def applyForce(self ,force)#'force' is Vector2D object
		#Add a force to
		self.pendingForces[0] += force.x()
		self.pendingForces[1] += force.y()



class Vector2D:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def get(self):
		return self.x, self.y
	def applyToXY(self, x, y):
		return ADD(self.x, self.y, x, y)

	def x(self):
		return self.x
	def y(self):
		return self.y
