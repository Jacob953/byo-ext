# HARNESS_NAME

> Template: copy this directory to `harnesses/<name>/`, replace all prompts,
> and remove this notice. This template contains no runnable implementation.

Describe the framework or runtime this harness integrates and what the
experiment is intended to explore. State that it is an experimental community
integration.

## Maintainers

Replace with the GitHub handles of contributors who maintain this harness.

## Compatibility

Record the kagent version or commit, framework version, and supported platform
you have used. Distinguish verified behavior from planned support.

Use the [kagent BYO guide](https://github.com/kagent-dev/website/blob/main/docs-site/content/kagent/1.x/agents/bring-your-own-agent.md)
for the contract appropriate to your target version. Explain how your harness
implements the A2A service, readiness, and configuration requirements.

## Prerequisites and configuration

List the tools and cluster prerequisites needed to build and run this harness.
Document runtime configuration, how credentials are supplied, and any external
service costs. Include example values only.

## Build

Replace the commented Dockerfile with your implementation. From this directory,
the build command is:

```sh
docker build --tag byo-ext/HARNESS_NAME:local .
```

Replace `HARNESS_NAME` with the lowercase directory name. CI runs this build on
Linux AMD64 with no extra arguments or credentials. Keep dependencies and build
inputs inside this directory or fetch pinned dependencies during the build.
Update `.dockerignore` for your framework's local artifacts.

## Run with kagent

Include manifests or exact setup commands for the kagent version you target.
Explain how to make the built image available to the cluster and configure the
harness entrypoint. Identify values the reader must replace.

## Try it

Provide one minimal invocation and the expected behavior. Describe the manual
verification you performed, including versions. CI checks only that the harness
builds.

## Limitations

Document unsupported features, known issues, and work in progress.

## Cleanup

Provide commands to remove the resources created by the setup example.
