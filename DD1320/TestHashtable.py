import unittest
from DictionaryWrapper import Hashtable
from hashtable import Hashtable, HashNode


class TestStringMethods(unittest.TestCase):
    # Förberedning av testdata
    def setup(self):
        d1 = Hashtable()
        k1 = "Carl XVI Gustaf"
        v1 = 1946
        k2 = "Region Blekinge"
        v2 = ["Karlshamn", "Karlskrona", "Olofström", "Ronneby", "Sölvesborg"]
        return d1, k1, k2, v1, v2

    # TEST: Lagra en nyckel i en dictionary och söka efter den
    def test_store1(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        self.assertEqual(d1.search(key1), value1)

    # TEST: Lagra två nycklar i en dictionary och söka efter dem
    def test_store2(self):
        d1, key1, key2, value1, value2 = self.setup()
        d1.store(key1, value1)
        d1.store(key2, value2)
        self.assertEqual(d1.search(key1), value1)
        self.assertEqual(d1.search(key2), value2)

    # TEST: Sök efter en nyckel i en tom dictionary
    def test_key_error(self):
        d1, key1, key2, value1, value2 = self.setup()
        with self.assertRaises(KeyError):
            d1.search(key1)

    # TEST: Lagra en nyckel i en hashtabell och söka efter den
    def test_hashtable_store(self):
        htable = Hashtable(10)
        key = "test_key"
        value = "test_value"
        htable.store(key, value)
        self.assertEqual(htable.search(key), value)

    # TEST: Lagra två nycklar med samma hash och söka efter dem
    def test_hashtable_collision(self):
        htable = Hashtable(10)
        key1 = "test_key"
        value1 = "test_value_1"
        key2 = "new_key"
        value2 = "test_value_2"
        # Dessa två nycklar kommer ha samma hash
        htable.store(key1, value1)
        htable.store(key2, value2)
        self.assertEqual(htable.search(key1), value1)
        self.assertEqual(htable.search(key2), value2)


if __name__ == '__main__':
    unittest.main()