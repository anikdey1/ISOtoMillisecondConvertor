# This script is meant to be run from the terminal; it is not meant to be imported.

from datetime import datetime as dt


def main():
	iso_timestamp = input("Enter the timestamp in ISO format: ")

	# This parses and stores the date in datetime format.
	date_time_timestamp = dt.strptime(iso_timestamp, '%Y-%m-%dT%H:%M:%S.%fZ')

	# This stores the timestamp of Unix start time.
	unix_start_timestamp = dt(1970, 1, 1)
	# This stores the time passed since Unix start time.
	timestamp_delta = date_time_timestamp - unix_start_timestamp

	# This counts the total seconds in amount of time passed.
	second_timestamp = timestamp_delta.total_seconds()
	# This converts seconds into milliseconds and removes the decimal part. 
	millisecond_timestamp = round(second_timestamp * 1000)

	print("The timestamp in millisecond format is:", millisecond_timestamp)


if __name__ == '__main__':
	main()
