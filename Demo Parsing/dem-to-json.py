from csgo.parser import DemoParser
import json
import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help='input demo file to processes')
    args = parser.parse_args()

    try:
        # Set parse_rate to a power of 2 between 2^0 and 2^7. It indicates the spacing between parsed ticks. Larger numbers result in fewer frames recorded. 128 indicates a frame per second on professional game demos.
        demo_parser = DemoParser(demofile=args.input, demo_id=args.input.replace(".dem",""), parse_rate=128)

        # Parse the demofile, output results to dictionary with df name as key
        data = demo_parser.parse()

        with open(args.input.replace(".dem",".json"), 'w') as outfile:
            json.dump(data, outfile)
    except:
        print("Error")
