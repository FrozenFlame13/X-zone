import webapp2

class ButtonHandler(webapp2.RequestHandler):
	def get(self):
		p=open("button.html","r")
		self.response.write(p.read())


app = webapp2.WSGIApplication([
	('/',ButtonHandler)
], debug=True)
