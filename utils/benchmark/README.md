# Benchmark script for locust

This benchmark script uses locust as performance testing framework. For more information about locust please refer to the oficial [documentation](https://docs.locust.io/en/stable/)

Before running the script you should install have installed python, and install the dependencies via pip. Dependencies can be installed, via the makefile.

```
make install
```

Once that all the dependencies are installed, you can run this test using the following command.

```
locust --headless --print-stats -f api_benchmark.py -H http://localhost:3000 -u 1000 -r 1 -t 300s
```

This will execute the api_benchmark with 1000 users with 1 user/second spawning during 300 seconds. Locust provide also a web UI to configure and visualize the data from the benchmark. Use the following command to run it in UI mode:

```
locust -f api_benchmark.api
```

You can use also the make commands for run in UI or headless mode.

```
make run-headless
make run-ui
```
