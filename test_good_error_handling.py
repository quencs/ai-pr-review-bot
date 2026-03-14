import unittest

class TestPaymentProcessor(unittest.TestCase):
    
    def setUp(self):
        # Code to set up the initial state before each test
        self.processor = PaymentProcessor()

    def test_process_payment_success(self):
        # Test a successful payment process
        amount = 100.00
        result = self.processor.process_payment(amount)
        self.assertTrue(result)
    
    def test_process_payment_failure_invalid_amount(self):
        # Test payment process with an invalid amount
        amount = -50.00
        with self.assertRaises(ValueError):
            self.processor.process_payment(amount)

    def test_process_payment_network_error(self):
        # Test handling of a network error during payment processing
        amount = 100.00
        self.processor.simulate_network_error = True
        with self.assertRaises(NetworkError):
            self.processor.process_payment(amount)

    def test_multiple_payments(self):
        # Test integration scenario with multiple payments
        amounts = [100.00, 200.00, 300.00]
        results = [self.processor.process_payment(amount) for amount in amounts]
        self.assertEqual(results, [True, True, True])
    
    def test_edge_case_zero_amount(self):
        # Test edge case for zero amount payment
        amount = 0.00
        with self.assertRaises(ValueError):
            self.processor.process_payment(amount)

    def tearDown(self):
        # Clean up code after each test
        pass

if __name__ == '__main__':
    unittest.main()