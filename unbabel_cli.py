import json
from datetime import datetime, timedelta
from collections import deque
import argparse

def read_events(input_file):
    """
    Reads JSON lines from the input file and parses them into a list of events.
    
    Args:
    input_file (str): Path to the input file containing JSON events.

    Returns:
    list: List of parsed events.
    """
    events = []
    #Read the file 
    with open(input_file, 'r') as file:
        # Iterate trougth each line in the file
        for line in file:
            try:
                # Convert the line to a json and append it to the array
                event = json.loads(line.strip())
                events.append(event)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in line: {line}")
                print(f"Error details: {e}")
    return events


def calculate_moving_average(events, window_size):
    """
    Calculates the moving average delivery time for events over a specified window size.

    Args:
    events (list): List of event dictionaries.
    window_size (int): Window size in minutes for moving average calculation.

    Returns:
    list: List of dictionaries with timestamps and their corresponding moving averages.
    """
    moving_averages = []  # List to store the moving averages
    timestamps = deque()  # Deque to store timestamps within the current window
    total_duration = 0  # Running total of durations within the current window

    for event in events:
        # Parse the timestamp from the event and convert it to the desired date format
        event_timestamp = datetime.strptime(event['timestamp'], "%Y-%m-%d %H:%M:%S.%f")
        
        # Add all the event's duration to the total duration 
        total_duration += event['duration']
        
        # Append the parsed timestamp to the deque
        timestamps.append(event_timestamp)



        # Remove events from the deque that are outside the window size converted to time format
        while timestamps and (event_timestamp - timestamps[0] > timedelta(minutes=window_size)):
             # Subtract the duration of the oldest event (outside the window) from the total duration
            total_duration -= events.pop(0)['duration']
            # Remove the oldest(first) timestamp from the deque
            timestamps.popleft()

        # Calculate the moving average by diving the total duration by the number of events inside the moving average window 
        if timestamps:
            moving_average = total_duration / len(timestamps)
        else:
            # if there are no events the moving average is set to 0
            moving_average = 0
        
        # Append the calculated moving average to the results list 
        # including the date in the desired format and the moving average
        moving_averages.append({
            "date": event_timestamp.strftime("%Y-%m-%d %H:%M:00"),
            "average_delivery_time": moving_average
        })

    return moving_averages

def main():
    
    # Setup command line argument parsing
    parser = argparse.ArgumentParser(description='Calculate moving average delivery time from events.')
    # Specify which command-line arguments the script accepts.
    parser.add_argument('--input_file', type=str, required=True, help='Path to the input file containing events')
    parser.add_argument('--window_size', type=int, required=True, help='Window size in minutes for moving average calculation')
    parser.add_argument('--output_file', type=str, default='output.json', help='Path to the output file to save the results (default: output.json)')
    # processes the command-line arguments
    args = parser.parse_args()

    # Read events from the input file using the args defined in the comand-line
    events = read_events(args.input_file)

    # Calculate the moving averages using the args defined in the comand-line and in the input-file
    moving_averages = calculate_moving_average(events, args.window_size)

    # Write the moving averages to the output file
    with open(args.output_file, 'w') as output_file:
        # Output each average as a JSON object
        for average in moving_averages:
            # Write the file to the output file which will be called output.josn of not specified the name in the comand-line
            output_file.write(json.dumps(average) + '\n')
            print(json.dumps(average))  # Output each average as JSON

if __name__ == "__main__":
    main()
