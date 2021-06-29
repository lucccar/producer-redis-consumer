import os

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
output_path = os.getenv('OUTPUT_FILE_PATH', 'consumer/output.txt')
