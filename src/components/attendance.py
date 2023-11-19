# TODO
# 1 - Will take present student names with date
# 2 - Create a folder if not exists named attendance
# 3 - In that folder a file named attendance.csv (columns = id, roll_number, name, date) { in that the id , name and roll numebr will be populated beforehand}
# 4 - The script will open the file and append the data for each date (if not exists) on each run (if duplicate date then take union of new and old data and replace the column)

import os
import sys
import pandas as pd
from datetime import datetime
from src.logger import logging
from src.exception import CustomException
from typing import List

def mark_attendance(attendance: List) -> None:
    """
    Marks attendance of students
    :param attendance: Roll number of students present
    :return: None
    """
    try:
        logging.info("Marking attendance")

        # Get the date
        date = datetime.now().strftime("%d-%m-%Y")
        attendance_file = os.path.join(os.getcwd(), "attendance", "attendance.csv")

        # If attendance file does not exist, create it
        if not os.path.exists(attendance_file):
            logging.info("Creating attendance file")
            attendance_df = pd.DataFrame(columns=["id", "roll_number", "name", date])
            attendance_df.to_csv(attendance_file, index=False)

        # Read the attendance file
        attendance_df = pd.read_csv(attendance_file)

        # Check if the date column exists
        if date not in attendance_df.columns:
            attendance_df[date] = 0

        # Mark attendance
        attendance_df.loc[attendance_df["roll_number"].isin(attendance), date] = 1

        # Save the attendance file
        attendance_df.to_csv(attendance_file, index=False)

    except Exception as e:
        logging.error(f"Error in mark_attendance: {e}")
        raise CustomException(e, sys)