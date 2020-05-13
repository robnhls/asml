


class Student:

    # how to instantiate (create) a student
    def __init__(self, name, email, grade="professional", age=29):
        # these can be read and modified by the user/client
        self.name = name
        self.email = email
        self.grade = grade
        self._age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age_value):
        if age_value < 1:
            raise ValueError("Age cannot be less than 0")
    
        if age_value > 150:
            raise ValueError("Currently age cannot be greater than 150. Contact a admin if a problem")

        self._age = age_value

    # instance method
    def send_email(self, title, body):
        ''' send_email to this student

        parameters
            title: title of the email
            body: the main content of the email
        '''

        print("-" * 50)
        print("To:", self.name, self.email)
        print("Title:", title)
        print()
        print(body)
        print("-" * 50)

    # instance method
    def register(self, course_title):
        # fake code to getister for a course
        print("{} is registered for {}".format(self.name, course_title))
        self.send_email("Registration Complete", "You are registered for " + course_title)




def _main():

    

    s1 = Student("rob foulkrod", "rob.foulkrod@nhls.com", age=47)
    s2 = Student("alice jones", "alice@example.com")

    # we may want to dissalow this
    s1.age = 790
    s1.age = -45


    print(type(s1))
    print(s1.name, s1.email)
    print(s2.name, s2.email)

    s1.send_email("Class Status", "You have been removed from that one class because...")

    s2.register("50 ways to write a function")


if __name__ == "__main__":
    _main()

