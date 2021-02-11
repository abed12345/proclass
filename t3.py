class Parent(object):
	def altered(self):
		print "parent Alt"
class child(Parent):
	def altered(self):
		print 5
		super(child, self).altered()
son= child()

son.altered()