from Input_validation_task import UserInputValidator

instance1 = UserInputValidator()
instance2 = UserInputValidator()

list1 = ["10", "-5", "abc", "42", "0"]
list2 = ["-1", "xyz", "100", "200", "300"]

valid_integers1 = instance1.validate_positive_integer(list1)
valid_integers2 = instance2.validate_positive_integer(list2)

print(instance1.validation_message())
print(instance2.validation_message())