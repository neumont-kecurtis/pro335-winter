invoke-webrequest https://dl.influxdata.com/influxdb/releases/influxdb-1.8.10_windows_amd64.zip -UseBasicParsing -OutFile influxdb-1.8.10_windows_amd64.zip
Expand-Archive .\influxdb-1.8.10_windows_amd64.zip -DestinationPath 'influxdb\'
mv influxdb-1.8.10_windows_amd64.zip influxdb\

invoke-webrequest https://dl.influxdata.com/chronograf/releases/chronograf-1.10.2_windows_amd64.zip -UseBasicParsing -OutFile chronograf-1.10.2_windows_amd64.zip
Expand-Archive .\chronograf-1.10.2_windows_amd64.zip -DestinationPath 'chronograf\'
mv chronograf-1.10.2_windows_amd64.zip chronograf\