import random

class Human_:
    """Base class for humans"""
    def setrandomgender(self, allow_other=False, **kwargs):
        if type(kwargs.get('custom_gender')) != dict:
            self.base_genders = [{'Male': ['He', 'Him']}, {'Female': ['She', 'Her']}]
        elif type(kwargs.get('custom_gender')) == dict:
            tmp = kwargs.get('custom_gender')
            if len(list(tmp)) == 1:
                self.gender = list(tmp)[0]
            else:
                self.gender = random.choice(list(tmp))
                self.refer_to_me_as = tmp[self.gender]

class Human(Human_):
    def __init__(self):
        self.age = random.randint(1, 101)
        self.gender