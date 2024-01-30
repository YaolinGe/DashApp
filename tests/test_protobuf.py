import sys
from src.controller import sensor_data_pb2


def read_protobuf(filePath):
    # Create an instance of the generated protobuf class
    sensor_data_list = sensor_data_pb2.SensorDataList()

    # Read data from the file
    with open(filePath, "rb") as file:
        sensor_data_list.ParseFromString(file.read())

    # Convert protobuf data to a Python structure (like a list or dict)
    # Example: converting to a list of tuples
    data = [(data_entry.time_span, data_entry.value) for data_entry in sensor_data_list.data]
    return data


if __name__ == "__main__": 
    filePath = sys.argv[1]
    data = read_protobuf(filePath)
    print(data)
    