import boto3
import time

# Initialize AWS DynamoDB client
dynamodb = boto3.resource('dynamodb', region_name='your_region_name')
table_name = 'your_table_name'
table = dynamodb.Table(table_name)

# Function to add sensor readings to DynamoDB table
def add_sensor_reading(timestamp, sensor1_value, sensor2_value, sensor3_value, sensor4_value):
    try:
        # PutItem operation to add a new item to the table
        table.put_item(
            Item={
                'timestamp': timestamp,
                'sensor1': sensor1_value,
                'sensor2': sensor2_value,
                'sensor3': sensor3_value,
                'sensor4': sensor4_value
            }
        )
        print("Sensor readings added successfully.")
    except Exception as e:
        print(f"Error adding sensor readings: {e}")

# Simulate live sensor readings and update the DynamoDB table dynamically
while True:
    # Replace these values with actual sensor readings
    timestamp = int(time.time())  # Current timestamp
    sensor1_value = 25.5  # Example value for sensor 1
    sensor2_value = 30.0  # Example value for sensor 2
    sensor3_value = 60.0  # Example value for sensor 3
    sensor4_value = 100.0  # Example value for sensor 4
    
    # Add sensor readings to DynamoDB table
    add_sensor_reading(timestamp, sensor1_value, sensor2_value, sensor3_value, sensor4_value)
    
    # Delay for 1 second (adjust as needed)
    time.sleep(1)