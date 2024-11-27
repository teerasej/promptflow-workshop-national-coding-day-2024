---
resources: examples/connections/azure_openai.yml, examples/flows/standard/web-classification
category: deployment
weight: 60
---

# Deploy flow using Azure App Service

This example demos how to deploy a flow using Azure App Service.

[Azure App Service](https://learn.microsoft.com/azure/app-service/) is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends.
The scripts (`deploy.sh` for bash and `deploy.ps1` for powershell) under this folder are here to help deploy the docker image to Azure App Service.

We will use [web-classification](../../../flows/standard/web-classification/README.md) as example in this tutorial.

## Build a flow as docker format app

Note that all dependent connections must be created before building as docker.
```bash
# create connection if not created before
pf connection create --file ../../../connections/azure_openai.yml --set api_key=<your_api_key> api_base=<your_api_base> --name open_ai_connection
```

Use the command below to build a flow as docker format app:

```bash
pf flow build --source ../../../flows/standard/web-classification --output dist --format docker
```


## Deploy with Azure App Service
The two scripts will do the following things:
1. Create a resource group if not exists.
2. Build and push the image to docker registry.
3. Create an app service plan with the give sku.
4. Create an app with specified name, set the deployment container image to the pushed docker image.
5. Set up the environment variables for the app.

Example command to use bash script:
```shell
bash deploy.sh --path dist -i <image_tag> --name my-app-23d8m -r <docker registry> -g <resource_group>
```

Example command to use powershell script:
```powershell
.\deploy.ps1 -Path dist -i <image_tag> -n my-app-23d8m -r <docker registry> -g <resource_group>
```
Note that the `name` will produce a unique FQDN as AppName.azurewebsites.net.

See the full parameters by `bash deploy.sh -h` or `.\deploy.ps1 -h`.

## View and test the web app
The web app can be found via [azure portal](https://portal.azure.com/)

![img](assets/azure_portal_img.png)

After the app created, you will need to go to https://portal.azure.com/ find the app and set up the environment variables
at (Settings>Configuration) or (Settings>Environment variables), then restart the app.

![img](assets/set_env_var.png)

Browse the app at Overview and see the test page:

![img](assets/test_page.png)

You can also test the app by sending a POST request to the app like:
```shell
curl http://<Default-domain-of-app-service>/score --data '{"url":"https://play.google.com/store/apps/details?id=com.twitter.android"}' -X POST  -H "Content-Type: application/json"
```


Tips:
- Reach deployment logs at (Deployment>Deployment Central) and app logs at (Monitoring>Log stream).
- Reach advanced deployment tools at  (Development Tools>Advanced Tools).
- Reach more details about app service at [Azure App Service](https://learn.microsoft.com/azure/app-service/).
