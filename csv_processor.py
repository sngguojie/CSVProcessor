# csv_processor.py

import sys
import os
import csv

class CSV_Processor:
	"""
	The CSV Processor takes a csv file as input and outputs a csv file, after processing the file with a csv manipulation file
	"""
	def __init__(self, input_path, output_path):
		self.input_path = input_path
		self.output_path = output_path
		self.is_valid = self.checkfiles()

	def __unicode__(self):
		"""
		returns the unicode representation of the csv processor
		"""
		result = unicode(self.input_path) +', '+ unicode(self.output_path)
		return result


	def run(self):
		"""
		Runs the processor to produce the output
		"""
		if not self.is_valid:
			raise ValueError('Paths are not valid')
		
		from manipulators.run import all_functions
		input_file = open(self.input_path, 'rb')
		input_csv = csv.reader(input_file, delimiter=',')
		output_file = open(self.output_path, 'wb')
		output_csv = csv.writer(output_file, delimiter=',')
		all_functions(input_csv, output_csv)

	
	def checkfiles(self):
		def check(file_path):
			file_exist = os.path.isfile(file_path)
			if not file_exist:
				raise ValueError(file_path + ' does not exist')
			return file_exist

		in_valid = check(self.input_path)
		out_valid = check(self.output_path)
		
		return in_valid and out_valid



if __name__ == "__main__":
	args = sys.argv[1:]
	input_path = args[0]
	output_path = args[1]
	csv_processor = CSV_Processor(input_path, output_path)
	csv_processor.run()