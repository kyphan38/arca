# authentication authorization

## Authentication and Authorization

Definitions

- Authentication is the process of verifying who a user is
- Authorization is the process of verifying what they have access to

Example: Alice is a user in AWS with no access to any service

Conclusion: Terraform needs access credentials with relevant permissions to create and manage the environments

Note: Depending on the provider, the type of access credentials would change

- AWS: Access keys and secret keys
- Github: Tokens
