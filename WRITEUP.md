# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
VM and App Service comparisson
- Cost: VMs are more expensive to run than Azure App Service, although a VM stops generating costs when it is switched off and unused. App Service generates costs even when unused.
- Scalability: App Services are somewhat less versitile in terms of scaling. App Services are limited on memory and cpu cores.
- Availability: VMs can be set up to handle scaling, availability and redundancy using load balancers and scale sets. Azure SLA guarantees 99.9% availability for single instance VMs but 99.95% for App Services.
- Workflow: Because VMs are IaaS, it requires more effort in managing the OS and required software to run an application. App Service as a PaaS, abstracts that away from the developer, making it easier to deploy a simple app.

I'm going to use the App Service for my deployment.

- The reason I am going with App Service is because for the project, scaling is not a big concern and the app requires few resources. Python is one of the supported languages for App Service, and since the service won't run for long, cost is not a major concern.

### Assess app changes that would change your decision.

If the application was expected to gain a large user base soon and the addition of many more features in the near future, a VM would have been a better option. I'd also switch to a VM if there are some advanced security concerns or if I need to control the OS my app runs on.