#!/usr/bin/env python3

# Created by: Jackson Naufal
# Created on: Feb 2022
# This is a diameter of a pizza  calculator in inches TAU

import constants


def main():
    # This is a calculator that calculates the cost of a pizza
    diameter = int(input("Enter the diameter in inches of your pizza here! (Inch): "))

    # process
    sub_total = (
        constants.labour_cost
        + constants.rent_cost
        + (constants.COST_PER_INCH * diameter)
    )
    total = constants.HST * sub_total

    # output
    print(
        "The cost of a {0} inch pizza (TAX INCLUDED) is  ${1:,.2f}".format(
            diameter, total
        )
    )
    print("\nDone.")


if __name__ == "__main__":
    main()
