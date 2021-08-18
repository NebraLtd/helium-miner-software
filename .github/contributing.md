# How to contriubte

Thanks for your interest in contributing to Nebra. We enforce certain rules on commits with the following goals in mind:

- Be able to reliably auto-generate the `CHANGELOG.md` *without* any human intervention.
- Be able to automatically and correctly increment the semver version number based on what was done since the last release.
- Be able to get a quick overview of what happened to the project by glancing over the commit history.
- Be able to automatically reference relevant changes from a dependency upgrade.

Our CI will run checks to ensure this guidelines are followed and won't allow merging contributions that don't adhere to them. Version number and changelog are automatically handled by the CI build flow after a pull request is merged. You only need to worry about the commit itself.

## Commit structure

Each commit message should consist of a header a body and a footer, structured in the following format:

```
<scope (optional)>: <subject (mandatory)>
--BLANK LINE--
(optional) <body>
--BLANK LINE--
(optional) Connects-to: #issue-number
(optional) Closes: #issue-number
(mandatory) Change-type: major | minor | patch
(optional) Signed-off-by: Foo Bar <foobar@balena.io>
```

Note that:
- Blank lines are required to separate header from body and body from footer. You don't need to add two blank lines if you don't add a body.
- `scope`: If your commit touches a well defined component/part/service please addthe scope tag to clarify. Some examples: `docs`, `images`, `typos`.
- `subject`: The subject should contain a short description of the change. Use the imperative, present tense.
- `body`: A detailed description of changes being made and reasoning if necessary. This may contain several paragraphs.
- `Connects-to`: If your commit is connected to an existing issue, link it by adding this tag with `#issue-number`. Example: `Connects-to: #123`
- `Closes`: If your commit fixes an existing issue, link it by adding this tag with `#issue-number`. Example: `Closes: #123`
- `Change-type`: At least one of your commits on a PR needs to have this tag. You have the flexibility, and it's good practise, to use this tag in as many commits as you see fit; in the end, the resulting change type for the scope of the PR will be folded down to the biggest one as marked in the commits (`major>minor>patch`). Our version numbering adheres to [Semantic Versioning](http://semver.org/).
- `Signed-off-by`: Sign your commits by providing your full name and email address in the format: `Name Surname <email@something.com>`. *This is an optional tag.*