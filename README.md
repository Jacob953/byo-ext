# BYO harness experiments

This repository is a place for the kagent community to contribute and explore
bring-your-own (BYO) harnesses. Each harness is an isolated experiment under
`harnesses/<name>/`, maintained by its contributors.

These experiments may eventually be proposed as official kagent integrations.
Inclusion here does not make a harness an official integration or commit kagent
maintainers to supporting it. Compatibility and limitations belong in each
harness's README.

## Explore or contribute

- Browse the [harness catalog](harnesses/README.md).
- Start with the [harness template](templates/harness/README.md) and
  [contribution guide](CONTRIBUTING.md).
- See [maintenance and review](MAINTAINERS.md) for ownership and review expectations.
- Follow kagent's [BYO integration guide](https://github.com/kagent-dev/website/blob/main/docs-site/content/kagent/1.x/agents/bring-your-own-agent.md)
  for the current runtime contract. Document the kagent version your harness targets.

There are no harness implementations yet. The template is a README and Dockerfile
scaffold, not a working agent.

## Repository layout

```text
harnesses/<name>/     Self-contained harness source, dependencies, and usage docs
templates/harness/   Starting point for a new contribution
.github/             Contribution templates, ownership, and CI
```

Each harness supplies a Dockerfile. CI builds changed harnesses without publishing
images. It does not certify runtime behavior,
kagent compatibility, or production readiness.

The repository is currently internal while it is being set up. Access follows
the organization's repository access policy.

## Community

Contributions use the [Apache-2.0 license](LICENSE) and require
[DCO sign-offs](CONTRIBUTING.md#sign-off-your-commits). Follow the
[Code of Conduct](CODE_OF_CONDUCT.md), including kagent's guidance on AI-assisted
contributions. See [SECURITY.md](SECURITY.md) for private vulnerability reporting.
