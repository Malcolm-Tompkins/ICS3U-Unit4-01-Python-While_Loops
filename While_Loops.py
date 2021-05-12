#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 12, 2021
# Determines sum of all numbers leading up to a number


def main():
    # Input

    user_input = (input("Enter your number: "))

    try:
        user_number = int(user_input)
        loop_counter = 0
        while (loop_counter < user_number):
            total = (user_number / 2) * (1 + user_number)
            loop_counter = loop_counter + 1
        print("{0:,.0f} is the total sum of the previous numbers before {1}"
              .format(total, user_number))

    except Exception:
        print("{} is not an integer".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
