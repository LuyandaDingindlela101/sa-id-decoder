#    CREATE A PROGRAM THAT WILL: 
#    .1) TAKE IN A USERS NAME
#    .2) TAKE IN A USERS ID NUMBER
#         FROM THAT ID NUMBER DETERMINE:
#         .1) DATE OF BIRTH
#         .2) AGE
#         .3) GENDER
#         .4) CITIZENSHIP (SA citizen / permanent resident)
#         .5) VALID (the Luhn algorithm)

#    IMPORT THE datetime OBJECT SO WE CAN USE IT LATER
from datetime import datetime


#    FUNCTION WILL RETURN THE USERS DATE OF BIRTH
def get_dob(id_sequence):
    #    CREATE A LIST THAT HOLDS ALL THE MONTHS OF THE YEAR
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    #    GET THE day BY GETTING THE LAST TWO DIGITS OF THE id_sequence
    day = id_sequence[4:]
    #    GET THE month BY GETTING THE THIRD AND FOURTH DIGITS OF THE id_sequence
    month = id_sequence[2:4]
    #    GET THE year BY GETTING THE FIRST TWO DIGITS OF THE id_sequence
    year = 2000 + int(id_sequence[:2])

    this_year = datetime.today().year

    if year > this_year:
        year = "19" + id_sequence[:2]

    return "day: " + day + ", month: " + months[int(month) - 1] + ", year: " + str(year)


#    FUNCTION WILL RETURN THE USERS GENDER
def get_gender(id_sequence):
    #    CONVERT THE id_sequence TO NUMBERS
    id_sequence = int(id_sequence)

    #    IF THE id_sequence IS BETWEEN 0 AND 4999, THEN THE USER IS A FEMALE
    if 0 <= id_sequence <= 4999:
        return "female"
    #    IF THE id_sequence IS ABOVE 5000, THEN THE USER IS A MALE
    else:
        return "male"


#    FUNCTION WILL RETURN THE USERS AGE
def get_age(year_of_birth):
    #  TURN year_of_birth INTO A LIST SO WE CAN ACCESS THE YEAR AT THE LAST INDEX
    year_of_birth = int(year_of_birth.split()[-1])

    #    GET THE CURRENT YEAR, THEN SUBTRACT THE USERS year_of_birth
    return datetime.now().year - year_of_birth


#    FUNCTION WILL RETURN THE USERS CITIZENSHIP STATUS
def get_citizenship(id_sequence):
    #    CONVERT THE id_sequence TO A NUMBER AND IF THE id_sequence IS 0, THEN THE USER IS A CITIZEN
    if int(id_sequence) == 0:
        return "citizen"
    #    IF NOT, THEN THE USER IS A PERMANENT RESIDENT
    else:
        return "permanent resident"


#    FUNCTION WILL TEST IF AN ID NUMBER IS VALID OR NOT USING THE LUHN ALGORITHM 
def test_id_valid(id_number):
    index = 0
    #    CREATE THE result_list LIST TO HOLD ALL THE NUMBERS TO BE SUMMED UP
    result_list = []

    #    LOOP THROUGH THE id_number TO GET ACCESS TO EACH INDIVIDUAL number
    for number in id_number:
        #    HERE WE SEPARATE THE ODD AND EVEN INDEXED NUMBERS
        #    THIS GIVES US ALL THE EVEN INDEXED NUMBERS
        if index % 2 == 0:
            result_list.append(int(number))
        else:
            #    HERE, WE TAKE EACH INDIVIDUAL number AND MULTIPLY IT BY 2
            number = int(number) * 2

            #    NOW, WE CHECK IF THE NUMBER IS A DOUBLE DIGIT BY CHECKING IF IT IS GREATER THAN 10 OR NOT
            if number >= 10:
                #    IF IT IS GREATER THAN TEN, CONVERT IT TO A STRING SO WE CAN ACCES EACH NUMBER
                number = str(number)
                #    CONVERT THE NUMBERS BACK TO IND=TEGERS, THEN ADD THEM TOGETHER
                number = int(number[0]) + int(number[1])
                #    NOW ADD THE number TO THE result_list
                result_list.append(int(number))
            #    IF THE NUMBER IS A LESS THAN 10, THEN JUST ADD IT TO THE result_list
            else:
                result_list.append(int(number))

        #    HERE, WE INCREASE THE VALUE OF index ON EACH ITERATION OF THE LOOP
        index = index + 1

    #    GET THE SUM OF THE result_list
    result = sum(result_list)

    #    IF THE sum MODULO 10 IS == 0, THEN THE id_number IS VALID
    if result % 10 == 0:
        return "valid"
    #    IF NOT, THEN THE id_number IS NOT VALID
    else:
        return "invalid"


def decode_id(id_number):
    #    FIRST WE GET THE USERS NAME AND ID NUMBER
    #    WE MAKE SURE NOT TO CONVERT TO CONVERT THE id_number SO THAT WE CAN GET THE DIFFERENT PARTS OF THE STRING
    #    CHECK IF THE id_number IS EQUAL TO 13 NUMBERS
    if len(id_number) == 13:
        if test_id_valid(id_number) == "valid":
            print(get_dob(id_number[:6]))
            get_age(get_dob(id_number[:6]))
            print(get_gender(id_number[6:10]))
            print(get_citizenship(id_number[10]))
        else:
            return "your id number id invalid"
    else:
        print("The provided id number does not meet the requirements")
        #    CALL THE decode_id() FUNCTION SO THE USER CAN START OVER AND RE-ENTER THEIR DETAILS
        decode_id()


decode_id()
