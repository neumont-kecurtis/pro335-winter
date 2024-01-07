# pro335-winter

# This contains all the code to get started with the project for PRO 335

## use 1_test_python.ps1 to see what version of python is installed
## use 2_create_venv.ps1 to create a virtual env
## use 3_activate_venv.ps1 to activate the virtual env
## use 4_install_requirements.ps1 to get the requirements installed
## use 5_download_influxdb.ps1 to get the correct versions of InfluxDb and Chronograf
## use 6_influx_init.ps1 to create the database for cpu stats
## use 7_cpu_stats.ps1 to insert some cpu stats into influxdb
## use 8_influx_dropdb.ps1 to drop the cpu stats measurements (optional)

## app.py is the core application for this project - python app.py [command]

## influx_start.ps1 and chronograf.ps1 will start the InfluxDb Services
### use CTRL-C to kill those processes
## influx_cli.ps1 will connect you to the influxdb database CLI (command line interface)
### type "exit" to leave the CLI
### type "show databases" to show the list of databases available
### type "use cpu" to use the cpu database, or any database
### type "select * from cpu_usage" to see the cpu stats from the python application

##