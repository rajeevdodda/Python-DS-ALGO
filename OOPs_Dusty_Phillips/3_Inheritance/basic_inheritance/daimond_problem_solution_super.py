class BaseClass:
    num_base_calls = 0

    def __init__(self):
        print("Base class initiated")

    def call_me(self):
        print("Calling method on base class")
        self.num_base_calls += 1


class LeftSubClass(BaseClass):
    num_left_calls = 0

    def __init__(self):
        super().__init__()
        print("left sub class initiated")

    def call_me(self):
        super().call_me()
        print("Calling method on left base class")
        self.num_left_calls += 1


class RightSubClass(BaseClass):
    num_right_calls = 0

    def __init__(self):
        super().__init__()
        print("right sub class initiated")

    def call_me(self):
        print("Calling method on right base class")
        self.num_right_calls += 1


class SubClass(LeftSubClass, RightSubClass):
    num_sub_calls = 0

    def call_me(self):
        super().call_me()
        print("Calling method on sub class")
        self.num_sub_calls += 1


s = SubClass()
s.call_me()
print(s.num_sub_calls, s.num_right_calls, s.num_left_calls, s.num_base_calls)
