
servers = ['server1', 'server2', 'server3', 'server4']
application = 'my_application'
path = '/path/to/application/package.zip'
def deploy_to_server(server, application,path):
    print(f"Deploying {application} to {server}...") 
for server in servers:
    deploy_to_server(server, application,path)

print("Deployment completed successfully!")
