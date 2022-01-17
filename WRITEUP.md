# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
VM and App Service comparisson

|           | Cost  | Scalability   | Availability | Workflow |
| -         | -     | -             | -            | - |
|App Service|A shared instance runs at 0.011EUR ($0.013) per hour. There is a free tier recommended for DEV/Testing.|App service allows for vertical scaling without downtime. No extra deployment is needed as this is a built in service. Trafic is managed with an integrated load balancer.|Azure does not provide an SLA for Apps under the "Free" or "Shared" tiers.|App Service is PaaS, so it abstracts OS and server configuration away from the developer, making it easier to deploy a simple app.|
|VM         |A B1s instance runs at 0.011EUR ($0.012) per hour. There is no free tier. Adding a standart HDD of 32Gb adds 1.35EUR ($1.54) to the monthly price. |The VM service allows for scaling to multiple instances using VM Scale Sets. Load balancing is achieved through the Azure Load Balancer service.|Azure guarantees an uptime of 95% for a VM configured as done under "cost".|VMs are IaaS, it requires more effort in managing the OS and required software to run an application. Additional configuration may also be required to set up the web server.|

I'm going to use the App Service for my deployment.

- The reason I am going with App Service is because for the project, scaling is not a big concern and the app requires few resources. Python is one of the supported languages for App Service, and since the service won't run for long, cost is not a major concern. I also won't need to configure anything manually and can rely on Azure's configuration.

### Assess app changes that would change your decision.

If the application was expected to gain a large user base soon and the addition of many more features in the near future, a VM would have been a better option. I'd also switch to a VM if there are some advanced security concerns or if I need to control the OS my app runs on.
