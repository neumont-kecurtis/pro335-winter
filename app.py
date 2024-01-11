import click
import psutil
import time
import socket
from influxdb import InfluxDBClient


@click.group()
def cli():
    pass


def write_to_influxdb(datapoints):
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'cpu')
    client.write_points(datapoints)


@cli.command()
def get_network_usage():
    UPDATE_DELAY = 1
    # get the network I/O stats from psutil
    io = psutil.net_io_counters()
    # extract the total bytes sent and received
    bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv

    while True:
        # sleep for `UPDATE_DELAY` seconds
        time.sleep(UPDATE_DELAY)
        # get the stats again
        io_2 = psutil.net_io_counters()
        # new - old stats gets us the speed
        us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv
        # print the total download/upload along with current speeds
        print(f"Upload: {io_2.bytes_sent}   "
            f", Download: {io_2.bytes_recv}   "
            f", Upload Speed: {us / UPDATE_DELAY}/s   "
            f", Download Speed: {ds / UPDATE_DELAY}/s      ", end="\r")
        # update the bytes_sent and bytes_recv for next iteration
        bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv


def get_cpu_stats():
        cpus = psutil.cpu_percent(interval=1, percpu=True)
        print(f'cpus: {cpus}')

        influx_datapoints = []

        for index, cpu in enumerate(cpus):
            print(f'cpu[{index}]: {cpu}')
            influx_datapoints.append(
                {
                    "measurement": "cpu_usage",
                    "tags": {
                        "host": socket.gethostname(),
                        "cpu_number": index
                    },
                    "fields": {
                        "cpu_percent": cpu
                    }
                })
        
        write_to_influxdb(influx_datapoints)


@cli.command()
@click.option('--loop', is_flag=True, default=False, help='Continuously monitor CPU usage')
def get_cpu_usage(loop):
    if loop:
        while True:
            get_cpu_stats()
    else:
        get_cpu_stats()


@cli.command()
def initdb():
    client = InfluxDBClient('localhost', 8086, 'root', 'root')
    client.create_database('cpu')


@cli.command()
def dropdb():
    client = InfluxDBClient('localhost', 8086, 'root', 'root')
    client.drop_database('cpu')


if __name__ == '__main__':
    cli()