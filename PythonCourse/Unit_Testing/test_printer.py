from unittest import TestCase
from printer import Printer, PrinterError

class TestPrinter(TestCase):

	# setUp method is inherited from TestCase
	# Not making this a classmethod ensures this will it will setup once
	def setUp(self):
		self.printer = Printer(pages_per_s=2.0,capacity=300)

	# def tearDown(self): in case you want to do something after the tests

	def test_printer_within_capacity(self):
		message = self.printer.print(25)
		print(message)
		self.assertEqual(f"Printer 25 in 12.50 seconds", message)

	def test_print_outside_capacity(self):
		with self.assertRaises(PrinterError):
			self.printer.print(301)

	def test_print_exact_capacity(self):
		self.printer.print(self.printer._capacity)

	def test_printer_speed(self):
		pages = 10
		expected = "Printer 10 in 5.00 seconds"
		result = self.printer.print(pages)
		self.assertEqual(result, expected)


