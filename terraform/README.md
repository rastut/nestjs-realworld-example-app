# Terraform modules
This folder contains the different terraform modules to deploy into production. I decided to use GCP as a cloud provider for this app. The application runs in the Cloud Run service and uses a CloudSQL Postgres instance as a DB.

In the folder extras, you will find some infra that is not full related with the app itself, but is needed in order to deploy the app. In that case, there is a module to create a Google Container Registry.

Otherwise, in the root of the terraform folder you will find all the modules needed to deploy the app. Requirements and minimal versions are in the `versions.tf` file.

To run the modules:

```
terraform init
terraform plan
terraform apply
```

Please verify the output of your plan before applying any change.


If you don't have Terraform installed, I recommend to install tfswitch. Is a version manager for Terraform and works quite well

Mac:
```
brew install warrensbox/tap/tfswitch
```
Linux

```
curl -L https://raw.githubusercontent.com/warrensbox/terraform-switcher/release/install.sh | bash
```
```
sudo snap install tfswitch
```