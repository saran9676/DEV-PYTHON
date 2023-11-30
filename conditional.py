import sys
deployment_environment = sys.argv[1]
operation=sys.argv[2]
deployment_branch = sys.argv[3]

# Check deployment conditions
if deployment_environment == "production" and deployment_branch == "main":
    print("Deploying to production environment from main branch")
elif deployment_environment == "staging" and deployment_branch == "feature-branch":
    print("Deploying feature branch to staging environment")
elif deployment_environment == "development" and deployment_branch=="hot-fix":
    print("Deploying to development environment")
else:
    print("Deployment conditions not met. No deployment action specified.")