from my_module import string_to_bool

class TestStringToBool(object):

    def test_lower_yes(self):
        assert string_to_bool("yes")
    
    def test_odd_yes(self):
        assert string_to_bool("Yes")
    
    def test_upper_yes(self):
        assert string_to_bool("YeS")
    
    def test_positive_int(self):
        assert string_to_bool("1")
    
    def test_true(self):
        assert string_to_bool("true")
    
    def test_true_trailling_space(self):
        assert string_to_bool("true ")
    
    def test_true_leading_space(self):
        assert string_to_bool(" true")
    