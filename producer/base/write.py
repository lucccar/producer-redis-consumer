    """Basic setup of the task that will be enqueued and got by the consumer worker.
    """

from producer.constants import output_path

def write_txt(json):
    """Base task the the consumer worker will do: write a recieved json in a output file

    Args:
        json (json): A json... what else?
    """
    with open(output_path, "w") as file:
        file.write(json)
