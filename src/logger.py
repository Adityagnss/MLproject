'''

Python machine learning (ML) projects, we use logger files for several reasons:

• Auditing and debugging: 

Log files provide a record of important events in the application, allowing developers to identify 
and troubleshoot issues. By capturing detailed information about errors, warnings, and informative messages, 
we can reproduce and fix problems more efficiently.

• Compliance and regulatory requirements:

In industries like finance, healthcare, or government, logging is often mandated by 
regulations (e.g., HIPAA, GDPR) to maintain transparency and accountability.

• Monitoring and performance tracking: 

Log files can contain metrics and statistics about model performance, training, and 
inference, enabling us to monitor the system's behavior and make data-driven decisions.

In Python, we use the built-in logging module, which provides a flexible and customizable way to handle logging. The basic components of a logger setup include:

• Logger: The central instance that emits log messages. 

• Handler: Responsible for sending log records to a specific location 
(e.g., file, console, network). • Formatter: Formats and styles the log records, controlling the output format and content.

'''



import logging

import os

from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m+__%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)


if __name__ == "__main__":
    logging.info("logging has been started")