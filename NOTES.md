# Notes

I will add some notes to make easier the reviewing process.

* First task: I modified the `ormconfig`, added dependencies as `pg` and `typeorm-extension`. I added `db:create` and `db:drop` scripts into package.json

* Second task: Seeding script can be found in the utils/seeder folder. It contains a makefile, dockerfile, and the script itself. The script can be configured with env vars, I didn't have time to implement `argparse` to use inputs for the script. It uses `faker` and `psycopg2` libraries. The script is also included in the `docker-compose file of the next task. It has also a readme with some instructions. Also, there is a Dockerfile for the application.

* Third task: Local environment can the docket-compose file found in the root of the project. The local environment includes the app, the database, and the seeder script. Instructions on how to run the environment are at the end of the README.md file.

* Fourth task: The benchmark script is in the utils/benchmark folder. The benchmark script has been written using the `Locust` framework. You will need to install it to run the benchmark. 
It contains the benchmark script and a makefile. Instructions on how to run it can be found in the `README.md`. If you want to test the script start the backend without seeding the database and run it locally through the local endpoint.

* Fifth task: The infrastructure is located in the Terraform folder, it has two modules the main one is for deploy the full infrastructure for the app, and the extra contains a GCR registry that is the one that will be used to create the registry that will hold the image. Backend files are commented as buckets for statements that are not set up in this exercise. 
The pipeline has been done with Drone, I wanted to use GitHub actions but I am a bit more familiar with Drone. The file with the pipeline is `.drone.yml`. As you can imagine running the pipeline you need a Drone instance that is not included in this task. 

Thanks for the opportunity to take this test. Probably, things can be better and improved but take this as a first iteration.