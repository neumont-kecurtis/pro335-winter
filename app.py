import click
import psutil
import socket
from influxdb import InfluxDBClient


@click.group()
def cli():
    pass


def write_to_influxdb(datapoints):
    client = InfluxDBClient('localhost', 8086, 'root', 'root', 'cpu')
    client.write_points(datapoints)


@cli.command()
def get_cpu_usage():
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
def initdb():
    client = InfluxDBClient('localhost', 8086, 'root', 'root')
    client.create_database('cpu')


@cli.command()
def dropdb():
    client = InfluxDBClient('localhost', 8086, 'root', 'root')
    client.drop_database('cpu')


if __name__ == '__main__':
    cli()