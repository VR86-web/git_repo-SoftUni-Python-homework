from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbol(Exception):
    pass


class InvalidNameError(Exception):
    pass


class InvalidEmailStart(Exception):
    pass


class CannotBeUpper(Exception):
    pass


class TooManyDots(Exception):
    pass


VALID_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_SYMBOLS_COUNT = 4
MIN_SECOND_PART_SYMBOL_COUNT = 6

email = input()

pattern_name = r"\w+"

while email != "End":
    if email.count("@") > 1:
        raise MoreThanOneAtSymbol("Email should contain only one @ symbol!")
    elif "@" not in email:
        raise MustContainAtSymbolError("Email must contain @!")
    elif len(email.split("@")[0]) <= MIN_NAME_SYMBOLS_COUNT:
        raise NameTooShortError("Name must be more than 4 characters")
    elif email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + d  for d in VALID_DOMAINS)}")
    elif findall(pattern_name, email.split("@")[0])[0] != email.split("@")[0]:
        raise InvalidNameError("Name must contain only letters, digits and underscores!")
    elif email[0].isnumeric():
        raise InvalidEmailStart("Email cannot start with digit!")
    elif email[0].isupper():
        raise CannotBeUpper("Email cannot start with upper letter!")
    elif email.count(".") > 2:
        raise TooManyDots("Email cannot contain more than 2 dots")

    print("Email is valid")

    email = input()