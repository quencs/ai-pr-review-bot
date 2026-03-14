import unittest
from payment_processor import PaymentProcessor, PaymentError

class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PaymentProcessor()

    def test_valid_payment(self):
        result = self.processor.process_payment(user='user1', amount=100)
        self.assertTrue(result)

    def test_invalid_amount(self):
        with self.assertRaises(PaymentError):
            self.processor.process_payment(user='user1', amount=-50)

    def test_missing_user(self):
        with self.assertRaises(PaymentError):
            self.processor.process_payment(user=None, amount=50)

    def test_insufficient_funds(self):
        self.processor.set_balance(user='user1', balance=20)
        with self.assertRaises(PaymentError):
            self.processor.process_payment(user='user1', amount=50)

    def test_payment_gateway_error(self):
        self.processor.set_gateway_error(True)
        with self.assertRaises(PaymentError):
            self.processor.process_payment(user='user1', amount=50)

    def test_database_failure(self):
        self.processor.set_database_failure(True)
        with self.assertRaises(PaymentError):
            self.processor.process_payment(user='user1', amount=50)

if __name__ == '__main__':
    unittest.main()