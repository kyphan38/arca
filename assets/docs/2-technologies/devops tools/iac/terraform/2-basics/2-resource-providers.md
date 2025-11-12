# resource providers

## Providers

Context

- Terraform supports multiple providers
- Depending on what type of infrastructure we want to launch, we have to use appropriate providers accordingly

Definitions: A provider is a plugin that lets Terraform manage an external API

Command: `terraform init`

- When we run terraform init, plugins required for the provider are automatically downloaded and saved locally to a .terraform directory

## Resource

Definition: Resource block describes one or more infrastructure objects

Examples

- resource aws_instance
- resource iam_user

## Resource Block

Definitions

- A resource block declares a resource of a given type ("aws_instance") with a given local name ("myec2")
- Resource type and Name together serve as an identifier for a given resource and so must be unique

Note: You can only use the resource that are supported by a specific provider
