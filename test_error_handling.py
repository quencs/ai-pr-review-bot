import unittest
from unittest.mock import patch, MagicMock

# Assuming PaymentProcessor and custom exceptions are defined in payment_processor.py
from payment_processor import PaymentProcessor, PaymentError, InsufficientFundsError, InvalidPaymentMethodError

class TestPaymentProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = PaymentProcessor()

    def test_successful_payment(self):
        result = self.processor.process_payment(100, "valid_card")
        self.assertTrue(result)

    @patch('payment_processor.PaymentProcessor.check_funds')
    def test_insufficient_funds(self, mock_check_funds):
        mock_check_funds.return_value = False
        with self.assertRaises(InsufficientFundsError):
            self.processor.process_payment(100, "valid_card")

    def test_invalid_payment_method(self):
        with self.assertRaises(InvalidPaymentMethodError):
            self.processor.process_payment(100, "invalid_method")

    def test_zero_amount_payment(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(0, "valid_card")

    def test_negative_amount_payment(self):
        with self.assertRaises(ValueError):
            self.processor.process_payment(-50, "valid_card")

    # Additional tests for edge cases can be added here

    @patch('payment_processor.ExternalService.process')
    def test_integration_service_call(self, mock_service):
        mock_service.return_value = True
        result = self.processor.call_external_service("valid_data")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()