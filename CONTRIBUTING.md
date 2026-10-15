# Contributing

Community members own and maintain their harness experiments. Keep each
contribution self-contained under `harnesses/<name>/` so it can evolve
independently of other harnesses.

Read the [Code of Conduct](CODE_OF_CONDUCT.md) before contributing. Contributions
are licensed under [Apache-2.0](LICENSE).

## Add a harness

1. Open a harness proposal issue describing the integration and who will maintain
   it. Discuss the scope with the repository maintainers before a substantial implementation.
2. Copy the template from the repository root:

   ```sh
   cp -R templates/harness harnesses/my-harness
   ```

   Choose a descriptive lowercase name using letters, digits, and hyphens.
3. Replace the template prompts with your source, dependency declarations,
   a working Dockerfile, kagent setup, and a minimal manual usage example.
   Name at least one maintainer by GitHub handle in the harness README.
4. Document the kagent version or commit and framework versions you have used,
   including anything that is incomplete or unverified.
5. Add the harness to [the catalog](harnesses/README.md). Repository maintainers
   can add eligible owners to [CODEOWNERS](.github/CODEOWNERS).
6. Build from a clean checkout, record the command and result in your PR,
   and request review.

Use a branch or fork that your repository access permits. While the repository
is internal, external contributions depend on the organization's access policy.

## Keep experiments independent

Keep source, dependencies, lockfiles where supported, and deployment examples
inside the harness directory. Do not import code from another harness or require
a sibling checkout. Use published dependencies or fetch pinned dependencies as
part of the build.

Each README should explain prerequisites, configuration, credentials supplied at
runtime, build and deployment steps, a small usage example, cleanup, and known
limitations. Include only example values for credentials.

The required harness check is whether it builds. This repository does not
require harness linting, unit tests, end-to-end tests, or model calls in CI.
Contributors can keep development tests within their own harness, but they are
not additional repository acceptance gates. Describe any manual verification
you performed without claiming behavior you have not checked.

## Build contract and CI

Every harness supplies `harnesses/<name>/Dockerfile`. The harness directory is
the entire build context. From the repository root, the CI build is equivalent
to:

```sh
docker build --tag byo-ext/my-harness:local harnesses/my-harness
```

Builds run on a Linux AMD64 GitHub-hosted runner, with Docker's default build
target and no extra build arguments or credentials. Put required defaults in
the Dockerfile. Fetch public dependencies during the build as needed; model
credentials and external service calls belong at runtime. Keep local credentials
out of the build context with `.dockerignore`.

The [build workflow](.github/workflows/build-harnesses.yml) builds changed
harnesses on pull requests and pushes to `main`. Changes to workflow or CI script
files rebuild every harness. A manual workflow run also builds all harnesses.
Documentation-only changes outside a harness do not trigger image builds.
A change within a harness, including its documentation, builds that harness.

The template lives outside `harnesses/` and is not built. A new harness whose
Dockerfile is missing or still contains only template comments will fail its
build. CI builds images without publishing them.

The stable summary check is named **Harness builds**. It succeeds when every
selected build succeeds or there are no harnesses to build, and fails if
selection or a build fails.

## Review and ownership

Harness maintainers handle fixes, dependency updates, documentation, and support
for their experiment. `@kagent-dev/maintainers` reviews new harnesses and changes
to shared repository infrastructure. Existing harness owners review changes to
their harness where possible.

Changes to the catalog or ownership file are shared repository changes and
should receive repository maintainer review. See [MAINTAINERS.md](MAINTAINERS.md)
for how ownership is recorded.

To propose an experiment as an official integration, start a separate discussion
with the kagent maintainers. Acceptance into this repository does not imply
acceptance into kagent.

## Sign off your commits

Every commit requires a Developer Certificate of Origin
([DCO](https://developercertificate.org/)) sign-off:

```sh
git commit -s -m "Add my harness"
```

The sign-off certifies that you have the right to contribute the change under
the project's license. It is a `Signed-off-by: Name <email>` commit trailer.

## Issues and security

Use the issue templates for harness proposals and bugs. Include the harness
name and relevant versions when reporting a problem. Follow
[SECURITY.md](SECURITY.md) for vulnerabilities.
