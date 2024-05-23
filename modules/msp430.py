import serial
import csv

# import threading


def init_serial_com(ser, flag):
    # flag = threading.Event()
    try:
        ser.open()
    except serial.SerialException:
        pass

    # reading test
    # while True:
    #     data = ser.readline()
    #     data = data.replace(b"\r", b"").decode("utf-8")
    #     channel_1 = data[:4]
    #     channel_2 = data[4:8]
    #     channel_3 = data[8:]
    #     print(data)
    #     print(
    #         " ch1:" + str(channel_1),
    #         " ch2:" + str(channel_2),
    #         " ch3:" + str(channel_3),
    #     )

    # Data management
    x_value = 0
    channel_1 = 0
    channel_2 = 0
    channel_3 = 0

    fieldnames = ["x_value", "channel_1", "channel_2", "channel_3"]

    with open("./data/data.csv", "w") as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
    while not flag.is_set():
        with open("./data/data.csv", "a") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            info = {
                "x_value": x_value,
                "channel_1": channel_1,
                "channel_2": channel_2,
                "channel_3": channel_3,
            }

            csv_writer.writerow(info)
            x_value += 1
            data = ser.readline()
            data = data.replace(b"\r", b"").decode("utf-8")

            channel_1 = data[:4]
            channel_2 = data[4:8]
            channel_3 = data[8:]

            # cleaned_channel_1 = channel_1.strip()
            # cleaned_channel_2 = channel_2.strip()
            # cleaned_channel_3 = channel_3.strip()

            # channel_1_value = int(cleaned_channel_1)
            # channel_2_value = int(cleaned_channel_2)
            # channel_3_value = int(cleaned_channel_3)

            # channel_1 = channel_1_value / 1023 * 3.3
            # channel_2 = channel_2_value / 1023 * 3.3
            # channel_3 = channel_3_value / 1023 * 3.3

            print(data)
            print(
                "x:" + str(x_value),
                " ch1:" + str(channel_1),
                " ch2:" + str(channel_2),
                " ch3:" + str(channel_3),
            )
    # time.sleep(1)
def button(ser):
    try:
        ser.open()
    except serial.SerialException:
        pass
    try:
        ser.write(b"BUTTON_PRESS\n")
        ser.flush()
    except serial.SerialException as e:
        print(f"Serial port error: {e}")
