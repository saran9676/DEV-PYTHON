# List of servers where you want to deploy the application
servers = ['server1', 'server2', 'server3', 'server4']

# Application to deploy
application = 'my_application'

# Path to the application package
path = '/path/to/application/package.zip'

# Assuming you have a deploy function to deploy the application to a server
def deploy_to_server(server, application,path):
    print(f"Deploying {application} to {server}...")  # Simulate deployment process
    # Your deployment logic goes here

# Iterate through the list of servers and deploy the application
for server in servers:
    deploy_to_server(server, application,path)

print("Deployment completed successfully!")
