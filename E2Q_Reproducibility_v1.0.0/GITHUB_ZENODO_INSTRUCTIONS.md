# Upload E2Q to GitHub and Zenodo

Recommended GitHub repository name: `e2q-vqc-noise-sensitivity`

## 1. Upload to GitHub

### Easiest web-browser method

1. Sign in to GitHub.
2. Create a **new public repository** named `e2q-vqc-noise-sensitivity`.
3. Because this project already contains `README.md`, `.gitignore`, and licenses, create the GitHub repository **without adding another README, .gitignore, or license**.
4. Open the empty repository and choose **Add file -> Upload files**.
5. Unzip `E2Q_Reproducibility_v1.0.0.zip` on your computer and upload the **contents of the folder**, not the outer ZIP as the only repository file.
6. Commit to `main` with a message such as `Initial E2Q reproducibility release`.
7. Check that GitHub displays the README and a **Cite this repository** option from `CITATION.cff`.

### Git command-line method

From inside the unzipped project folder:

```bash
git init
git branch -M main
git add .
git commit -m "Initial E2Q reproducibility release"
git remote add origin https://github.com/YOUR-USERNAME/e2q-vqc-noise-sensitivity.git
git push -u origin main
```

Before pushing, create the empty GitHub repository in the browser, or use GitHub CLI if you already use it.

## 2. Connect the GitHub repository to Zenodo

1. Sign in to Zenodo.
2. Connect your GitHub account to Zenodo if it is not already connected.
3. In Zenodo, open the profile menu and choose **GitHub**.
4. Click **Sync now**.
5. Find `e2q-vqc-noise-sensitivity` and enable the repository toggle.
6. Do this **before creating the GitHub release** so Zenodo can automatically archive it.

## 3. Create the immutable GitHub release

On GitHub:

1. Open the repository -> **Releases** -> **Draft a new release**.
2. Create tag: `v1.0.0`.
3. Release title: `E2Q reproducibility package v1.0.0`.
4. Paste the contents of `RELEASE_NOTES_v1.0.0.md` into the release notes.
5. Publish the release (do not mark it as a prerelease).

GitHub releases are tied to Git tags, so `v1.0.0` freezes the exact repository state used for the archived release.

## 4. Let Zenodo archive the release

After the GitHub release is published:

1. Return to Zenodo -> profile -> **GitHub** -> your enabled repository.
2. Wait for the `v1.0.0` release to finish processing.
3. Open the DOI/record created by Zenodo.
4. Verify title, authors, version, license, description, and keywords against `ZENODO_METADATA.md`.
5. Confirm the record files correspond to GitHub tag `v1.0.0`.

Zenodo assigns a DOI when the record is published/archived. For the manuscript, cite the **DOI of the specific v1.0.0 record** so reviewers can retrieve exactly the frozen files used for the paper.

## 5. Put the DOI back on GitHub

Once Zenodo gives you the DOI:

1. Edit the top of `README.md` on the `main` branch and add a Zenodo DOI badge/link if desired.
2. You may also add the DOI to `CITATION.cff` on `main`.
3. Do **not** retag or move `v1.0.0`. The release tag should remain immutable.
4. If you need the DOI embedded inside a future archived source bundle, make a new version/release such as `v1.0.1` rather than rewriting `v1.0.0`.

## 6. Update the manuscript

Replace the current generic Online Resource/repository wording with the exact links after publication:

```text
Code availability
The code and reproducibility notebook are available from GitHub at
https://github.com/YOUR-USERNAME/e2q-vqc-noise-sensitivity and are archived
as version 1.0.0 on Zenodo at https://doi.org/10.5281/zenodo.XXXXXXX.

Data availability
The frozen processed evidence tables, calibration provenance, benchmark
configuration, and figures used in this study are archived with the same
versioned Zenodo release: https://doi.org/10.5281/zenodo.XXXXXXX.
```

Use the actual **version DOI** returned by Zenodo. Do not copy the DOI of another manuscript/project.

## 7. Future changes

- Typo/README-only changes can be committed to `main` without changing the archived `v1.0.0` tag.
- Any change to code, notebook, processed evidence, or benchmark files that you want readers to cite should receive a new GitHub release/tag (for example `v1.0.1` or `v1.1.0`).
- Zenodo versions receive separate persistent identifiers linked across versions, which preserves the exact files associated with each cited release.

## Alternative: manual Zenodo upload

If you do not want GitHub-Zenodo integration, you can create a new Zenodo upload manually and upload the release ZIP as a **Software** record. The GitHub integration is preferable here because it automatically associates the DOI with a tagged, immutable GitHub release.
