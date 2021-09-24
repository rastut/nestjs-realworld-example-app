# Seeder script

This repo contains the seeder script from the second task. The script has been developed and tested with python3.9. Dependencies can be installed via makefile.
The script will populate all the tables from the sample app. It can be configured via environment variables.

```
make install
```

These are the parameters available. Seeder_counter is the number of inserts per table.

```
    export DB_USER=postgres
    export DB_PASSWORD=password
    export DB_DATABASE=nestjestsampleapp
    export DB_HOST=localhost
    export SEED_COUNTER=1000
```

To invoke the script:

```
python main.py
```
```
make run
```

I would love to add `argparse` to the script, but no time for it :(.