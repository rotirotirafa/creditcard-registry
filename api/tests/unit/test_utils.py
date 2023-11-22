import unittest
import bcrypt
import hashlib
from api.src.utils import hash_credit_card_number, check_creditcard_hash, hash_pw, verify_password_hash


class TestHashingFunctions(unittest.TestCase):
    def test_hash_credit_card_number(self):
        # Test hash_credit_card_number function
        card_number = "1234567890123456"
        expected_hash = hashlib.sha256((card_number + "123").encode('utf-8')).hexdigest()
        self.assertEqual(hash_credit_card_number(card_number), expected_hash)

    def test_check_creditcard_hash(self):
        # Test check_creditcard_hash function
        card_number = "1234567890123456"
        expected_hash = hashlib.sha256((card_number + "123").encode('utf-8')).hexdigest()
        self.assertEqual(check_creditcard_hash(card_number), expected_hash)

    def test_hash_pw(self):
        # Test hash_pw function
        password = "password123"
        hashed_pw = hash_pw(password)
        self.assertTrue(bcrypt.checkpw(password.encode('utf-8'), hashed_pw))

    def test_verify_password_hash(self):
        # Test verify_password_hash function
        password = "password123"
        self.assertTrue(verify_password_hash(password))

if __name__ == '__main__':
    unittest.main()
