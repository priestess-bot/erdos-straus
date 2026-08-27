# T6 Gate 0 Signed Manifest Attestation Boundary (2026-08-27)

## Change

The Gate 0 job now creates a GitHub/Sigstore provenance attestation for the
verified `ci-run-manifest-v1.json` on successful pushes to `main`. The action
is pinned to the verified `actions/attest` v4.2.2 commit, and only the Gate 0
job receives `id-token`, `attestations`, and `artifact-metadata` write
permissions.

The attestation subject is the raw manifest file, not the later upload
artifact container. It binds the subject digest to the GitHub OIDC workflow
identity and source revision, and can be independently checked with the GitHub
CLI attestation verifier.

## First Verified Attested Run

GitHub Actions run `33075094312` completed both `gate-zero` and
`live-audit-snapshot` successfully at exact HEAD
`2da9e6e5accd26766a48ecf574b3961b819a2df1`, tree
`ce710473d8b03f98f458cc2e65156be0af5949c6`. The raw manifest artifact has

```text
sha256:c78e1374ff38c3bc53de9094eda0b89cb9a24a49e67c591164a1e2dd4d18bec5
```

which matches both the artifact API digest and the attestation subject. A
fresh `gh attestation verify` constrained the repository, signer workflow,
source digest, `refs/heads/main`, and GitHub-hosted runner, and returned a
verified SLSA provenance statement with a Rekor transparency-log timestamp.
The manifest itself reports `status=PASS`, the same HEAD/tree pair, and nine
completed Gate 0 commands.

## Previous External Evidence

The last pre-attestation green run was `33060237359` at exact HEAD
`7c122327751e1dbf864351828e8023dd0033412a`. Its manifest artifact raw digest
was

```text
sha256:2f33e491ab70be30e8c55df0e03182b5078e191d3488e1c86bd569f556e9a9d2
```

and its live snapshot correctly reported that HEAD as verified. It had no
signed attestation, had 90-day retention, and therefore remained only an
external trust-anchor candidate.

## Authority Boundary

A signed Gate 0 manifest proves provenance of that exact subject. It does not
by itself prove that an independent reviewer approved the workflow policy, and
a repository commit must not authorize itself merely by changing both policy
and expected pins. A V7 consumer must still constrain the repository, signer
workflow, source revision, subject digest, and reviewed workflow/verifier
digests, and should rely on branch governance or an external approval for the
policy decision.

The attestation also does not create a complete terminal schedule, source E1,
producer, admission, queue authority, or a theorem-status upgrade. Those
obligations remain independent.
