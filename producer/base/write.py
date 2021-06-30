"""Basic setup of the task that will be enqueued and got by the consumer worker.
"""

from producer.constants import output_path
import json

def write_txt(jsn):
    """Base task the the consumer worker will do: write a recieved json in a output file

    Args:
        jsn (json): A json... what else?
    """
    with open(output_path, "w") as file:
        file.write(json.dumps(jsn))
