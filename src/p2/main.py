#!/usr/bin/env python
import warnings

import os
from p2.crew import p2

from datetime import datetime


# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)


warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "Inteligencia artificial en la atención sanitaria",
        "current_year": str(datetime.now().year),
    }

    # Create and run the crew
    result = p2().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")


if __name__ == "__main__":
    run()
