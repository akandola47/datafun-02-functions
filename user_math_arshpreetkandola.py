"""Arshpreet Kandola
September 3 2023
Buisness Domain"""

import math

import logging
import pathlib
import platform
import sys
import os
import datetime

def setup_logger(current_file):
       
    logs_dir = pathlib.Path("logs")
    logs_dir.mkdir(exist_ok=True)

    module_name = pathlib.Path(current_file).stem
    log_file_name = logs_dir.joinpath(module_name + ".log")

    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)  # Set the root logger level.

    # Create file handler to write logging messages to a file
    file_handler = logging.FileHandler(log_file_name, "w")
    file_handler.setLevel(logging.DEBUG)

    # Create console handler to write logging messages to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Create formatter and add it to the handlers.
    formatter = logging.Formatter("%(asctime)s.%(name)s.%(levelname)s %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger.
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    python_version_string = platform.python_version()
    today = datetime.date.today()

    logger.info(f"{DIVIDER}")
    logger.info(f"Today is {today} at {datetime.datetime.now().strftime('%I:%M %p')}")
    logger.info(f"Running on: {os.name} {platform.system()} {platform.release()}")
    logger.info(f"Python version:  {python_version_string}")
    logger.info(f"Python path: {sys.prefix}")
    logger.info(f"Working dir: {os.getcwd()}")
    logger.info(f"{DIVIDER}")

    return logger, log_file_name

from util_logger import setup_logger
logger, logname = setup_logger(__file__)

def get_area_of_house_lot(length,width):
     logger.info(f"CALLING get_area_of_house_lot({length,width})")

    try: 
        area = length * width
        logger.info(f"The area of house lot is {area}")
        return area
    except Exception as ex:
        logger.error(f"Error: {ex}")
        return None


 
country_lot = get_area_of_house_lot(2000,5000)
downtown_lot = get_area_of_house_lot(1000,2000)
suburb_lot = get_area_of_house_lot(3000,3000)
farm_lot = get_area_of_house_lot(6000,7000)

logger.info(f"sum of all lots combined = {math.fsum(all_areas)}")
logger.info(f"abs differnce of country and farm lots = {math.fabs(country_lot - farm_lot)}")
logger.info(f"smallest lot = {min{all_lots}}")


logger.info("Explore some functions in the math module")
logger.info(f"math.comb(2000,5000) = {math.comb(2000,5000)}")
logger.info(f"math.perm(5,1) = {math.perm(5,1)}")

if __name__ == "__main__":

    logger.info("Explore some functions in the math module")
    logger.info(f"math.comb(5,1) = {math.comb(5,1)}")
    logger.info(f"math.perm(5,1) = {math.perm(5,1)}")
    logger.info(f"math.comb(5,3) = {math.comb(5,3)}")
    logger.info(f"math.perm(5,3) = {math.perm(5,3)}")
    logger.info(f"math.pi = {math.pi}")
    logger.info(f"math.degrees(2 * math.pi) = {math.degrees(2 * math.pi)}")
    logger.info(f"math.radians(180)         = {math.radians(180)}")
    logger.info("")

    logger.info("TRY: Call get_circle_area_given_radius() function with a different values.")
    get_circle_area_given_radius(5)
    get_circle_area_given_radius(-16)
    get_circle_area_given_radius(math.inf)
    get_circle_area_given_radius('five')
    logger.info("")

    logger.info("TRY: Call get_circle_areas_given_list() function with a list of GOOD values")
    good_list = [5, 10, 25, 30, 45, 50]
    get_circle_areas_given_list(good_list)
    logger.info("")


    logger.info("TRY: Call get_circle_areas_given_list() function with a list that may include BAD values")
    bad_list = [-5, 0, math.inf, '30']
    get_circle_areas_given_list(bad_list)

    print("Done. Please check the log file for more details.")

