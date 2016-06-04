import time

class StatsMiddleware(object):
	def process_request(self, request):
		# "Store the start time when the request comes in."
		request.start_time = time.time()

	def process_template_response(self, request, response):

		# "Calculate and output the page generation duration"
		# Get the start time from the request and calculate how long
		# the response took.
		duration = time.time() - request.start_time

		response.context_data["load_time"] = duration
		return response
