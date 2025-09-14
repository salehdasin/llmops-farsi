import logging

logging.basicConfig(level=logging.INFO, filename='llm.log')

def log_input_output(input_data, output_data):
    logging.info(f"Input: {input_data}")
    logging.info(f"Output: {output_data}")
