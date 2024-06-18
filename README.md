

---

## Overview 

This project calculates the moving average delivery time from events stored in a specified input file. The events are expected to be in a specific JSON format, where each event is stored as a separate JSON object in a new line.

---

## Prerequisites

- Python 3.7 or higher

---

## Setup



### Step 1: Clone the repository

```bash
git clone https://github.com/your_username/your_repository.git
cd your_repository
```
### Step 2: Create and activate a virtual environment

For Unix/Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```
---

## Usage

### Command-line Arguments

The script accepts the following command-line arguments:

```bash
--input_file: Path to the input file containing events (required).
--window_size: Window size in minutes for moving average calculation (required).
--output_file: Path to the output file where moving averages will be saved (optional). If not specified, defaults to output.json.
```



---

##  Input File Format

The input file should be a JSON file with each line containing a single event in the following format:
```bash
{"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159", "translation_id": "5aa5b2f39f7254a75aa4", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 31}
```

---

## Output


The output is a JSON file containing moving average delivery times, formatted as:
```bash
  {"date": "2024-06-18 14:00:00", "average_delivery_time": 20}
  {"date": "2024-06-18 15:00:00", "average_delivery_time": 25}
```

---

## Example
Calculate moving averages for events in events.json with a window size of 60 minutes and save results to output.json:


```bash

python unbabel_cli.py --input_file events.json --window_size 60 --output_file output.json

```



If you omit --output_file, the results will be saved to output.json by default:

```bash
python unbabel_cli.py --input_file events.json --window_size 10
```

---


##  Testing

Ensure the input file (events.json) contains events in the expected JSON format.
Run the script with different window sizes and verify the output against expected results.

---

##  Considerations

### Input Format: 
The script assumes each event is stored as a separate JSON object in a new line. If your input format differs, modifications may be required in the read_events function.

### Error Handling: 
The script includes basic error handling for JSON decoding errors. Further error scenarios should be considered based on your use case.

### Performance: 
Evaluate performance implications, especially for large input files or frequent calculations.



