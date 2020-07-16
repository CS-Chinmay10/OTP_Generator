import random , datetime

"""This generator asks for how many digits you want to include in your OTP."""
digits = "0123456789"
str_otp = ""
num_of_otp_digits = int(input("How many otp digits do you want: "))

while True:
    for i in range(num_of_otp_digits):
        str_otp += digits[random.randint(0 , len(digits) - 1)]
    with open("otps.txt" , "r") as fread:
        if str_otp in fread.read():     # Check to see if otp is already sent
            continue
    with open("otps.txt" , "a") as fwrite:
        print(str_otp)
        comp_date_time = str(datetime.datetime.utcnow())
        date_time = comp_date_time[:len(comp_date_time) - 7]                  # After sending otp make a copy of it in
        fwrite.write(date_time + " | " + str_otp + "\n")                      # file otps.txt for future reference
        break
"""Also, otps once generated are stored in the text file to avoid generating identical otps.
Date and time is also given for more concise information."""