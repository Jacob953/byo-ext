# Maintenance and review

## Repository maintainers

`@kagent-dev/maintainers` reviews new harnesses and owns shared documentation,
templates, CI, and repository policy.

## Harness maintainers

Contributors maintain their own harnesses. Each harness README names its
maintainers by GitHub handle, and the catalog links to that README. Harness
maintainers handle issues, dependency updates, and compatibility notes for
their experiment.

List harness owners in `.github/CODEOWNERS` when they have the repository
permissions GitHub requires. GitHub code owners must have explicit write access;
listing a contributor in a README does not grant repository access. Until an
owner is eligible, the repository maintainers remain the code owners for that
path.

For an eligible owner, add a rule after the default rule:

```text
/harnesses/my-harness/ @contributor-handle
```

The default rule continues to cover the catalog and shared files. GitHub uses the
last matching rule. A harness rule routes reviews to its owners; a new harness
also changes the shared catalog and ownership file, which route reviews to the
repository maintainers.

If a harness no longer has an active maintainer, make that clear in its README
and catalog entry before recruiting a replacement. This repository does not
promise a support or release schedule for experiments.

## GitHub setup to apply later

The scaffold is prepared locally. These settings need a separate GitHub
configuration step after the initial files are pushed:

- Keep the repository internal until its visibility is explicitly reconsidered.
- Confirm that `@kagent-dev/maintainers` has write access so CODEOWNERS works.
- Enable GitHub Actions with permission to use the actions referenced by the
  workflows. Builds need no repository secrets or registry credentials.
- Enable the [DCO app](https://github.com/apps/dco) for this repository and confirm
  that its check appears on a pull request. A sign-off policy alone does not
  enforce DCO.
- Protect `main` with pull requests, at least one approval, and code owner review.
  Require the **Harness builds** summary check and the DCO check after their names
  have been verified in an actual run. Dismiss stale approvals and block force pushes
  and branch deletion.
- If the repository later becomes public, review contributor access and fork
  workflow settings before inviting outside contributions.

CODEOWNERS requests reviews; branch protection or rulesets enforce them. No
GitHub settings are changed by these files.
