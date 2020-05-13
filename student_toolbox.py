


class Student:

    # class Data/attributes are the same for EVERY instance
    fromLine = "Automated Student Email Service"

    # how to instantiate (create) a student
    def __init__(self, name, email, grade="professional", age=29):
        # these can be read and modified by the user/client
        self.name = name
        self.email = email
        self.grade = grade
        self._age = None
        self.age = age


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
        print("From:", Student.fromLine)
        print("Title:", title)
        print()
        print(body)
        print("-" * 50)

    # instance method
    def register(self, course_title):
        # fake code to getister for a course
        print("{} is registered for {}".format(self.name, course_title))
        self.send_email("Registration Complete", "You are registered for " + course_title)

    @classmethod
    def change_from_line(cls, new_from_line):
        if len(new_from_line) == 0:
            raise ValueError("fromLine must be a non-zero length string")

        cls.fromLine = new_from_line

    @staticmethod  #static Method has not extra parameters (no cls, no self)
    def create(name):
        student = Student(name, name+"@example.com")
        return student


def _main():

    Student.change_from_line("Automated Whosit")

    s1 = Student("rob foulkrod", "rob.foulkrod@nhls.com", age=47)
    s2 = Student("alice jones", "alice@example.com")
    s3 = Student.create("John.the.linter")


    s3.send_email("Need help coding", "Here is some sample code I found. And I need some help")


    # we may want to dissalow this
    # s1.age = 790 # yes it causes an error
    # s1.age = -45 # yes is also causes an error
    s1.age = 48

    # s1._age = 1000 # this is allowed, but a generally accepted bad idea

    print("current Age", s1.age)

    print(type(s1))
    print(s1.name, s1.email)
    print(s2.name, s2.email)

    s1.send_email("Class Status", "You have been removed from that one class because...")

    s2.register("50 ways to write a function")


if __name__ == "__main__":
    _main()

