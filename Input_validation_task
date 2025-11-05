class UserInputValidator:
    def validate_positive_integer(self, string_list):
        self.temp_list = []
        for item in string_list:
            if item.isdigit() and int(item) > 0:
                self.temp_list.append(int(item))
        return self.temp_list

    def validation_message(self):
        if self.temp_list:
            return f"Validation complete. {len(self.temp_list)} valid integers found: {self.temp_list}"
        else:
            return "No valid positive integers found."