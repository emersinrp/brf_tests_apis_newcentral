import logging

# Configurar logger para erros
error_logger = logging.getLogger('locust_errors')
error_logger.setLevel(logging.ERROR)
error_handler = logging.FileHandler('locust_errors.log')
error_handler.setLevel(logging.ERROR)
error_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)

# Configurar logger para sucessos
success_logger = logging.getLogger('locust_success')
success_logger.setLevel(logging.INFO)
success_handler = logging.FileHandler('locust_success.log')
success_handler.setLevel(logging.INFO)
success_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
success_handler.setFormatter(success_formatter)
success_logger.addHandler(success_handler)
