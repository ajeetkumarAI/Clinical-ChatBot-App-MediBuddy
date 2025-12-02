*** Begin Patch
*** Update File: README.md
@@
# Clinical-ChatBot-App-MediBuddy — Quick Git & SSH Guide

This file contains concise, copy-pastable steps to set up SSH for GitHub (on Windows using Git Bash) and common Git commands you will use when working with this repository.

Prerequisites
- Git and Git Bash installed.
- A GitHub account with access to the repository.

1) Generate or confirm an SSH key

If you don't already have an SSH key, generate one (use your email):

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
# accept defaults or specify a path like ~/.ssh/id_ed25519
```

2) Start ssh-agent and add your key (Git Bash)

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If `ssh-add` errors with "Could not open a connection to your authentication agent", re-run the `eval` line, then `ssh-add` again.

3) Copy the public key and add it to GitHub

```bash
cat ~/.ssh/id_ed25519.pub | clip.exe
```

- Go to: https://github.com/settings/ssh/new
- Paste the key, give it a descriptive title (e.g., "Work laptop - Git Bash"), and save.

4) Verify the SSH connection

```bash
ssh -T git@github.com
```

Expected response on success:

```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

5) Set the repository remote to SSH and push

```bash
git remote set-url origin git@github.com:ajeetkumarAI/Clinical-ChatBot-App-MediBuddy.git
git push -u origin main
```

Git basics (common commands)

- Stage all changes:
```bash
git add .
```
- Stage a single file:
```bash
git add path/to/file
```
- Check working tree status:
```bash
git status
```
- Commit staged changes:
```bash
git commit -m "Short descriptive message"
```
- Create and switch to a new branch:
```bash
git checkout -b feature/your-feature-name
```
- Switch branch:
```bash
git checkout main
```
- Push branch and set upstream:
```bash
git push -u origin feature/your-feature-name
```
- Push current branch:
```bash
git push
```
- Pull remote changes for current branch:
```bash
git pull
```

Troubleshooting
- If a push returns a 403 permission error, confirm which GitHub account you are authenticating as (you may have cached HTTPS credentials for a different account). Clearing Windows Credential Manager entries for GitHub or switching to SSH usually resolves this.
- If `clip.exe` is not available, run `cat ~/.ssh/id_ed25519.pub` and copy the output manually into the GitHub UI.
- If `ssh -T git@github.com` returns "Permission denied", ensure the public key was added to the correct GitHub account.

Want me to commit this update?
- I can run the staging/commit and (optionally) push commands for you if you want — tell me to proceed. Note: pushing may fail if your GitHub authentication is still the wrong account; use the SSH steps above first.

--
File: `README.md`
+# SSH setup for pushing to GitHub
+
+Follow these steps in **Git Bash** to add an SSH key, register it with GitHub, switch the repository remote to SSH, and push your branch.
+
+Prerequisites:
+- Git Bash installed (on Windows).
+- A GitHub account with access to the target repository.
+
+1. Start the ssh-agent and add your private key
+
+```bash
+eval "$(ssh-agent -s)"
+ssh-add ~/.ssh/id_ed25519
+```
+
+2. Copy the public key to the Windows clipboard
+
+```bash
+cat ~/.ssh/id_ed25519.pub | clip.exe
+```
+
+3. Add the public key to GitHub
+- Open: `https://github.com/settings/ssh/new`
+- Paste the clipboard contents into the key field and give it a title (e.g., "Work laptop - Git Bash").
+
+4. Verify the SSH connection to GitHub
+
+```bash
+ssh -T git@github.com
+```
+
+Expected response (first-time):
+```
+Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
+```
+
+5. Switch the repository remote to the SSH URL and push
+
+```bash
+git remote set-url origin git@github.com:ajeetkumarAI/Clinical-ChatBot-App-MediBuddy.git
+git push -u origin main
+```
+
+Git basics (add / commit / branch / push)
+
+Use these common commands after editing or adding files.
+
+- Stage changes (all files):
+
+```bash
+git add .
+```
+
+- Stage a specific file:
+
+```bash
+git add path/to/file.py
+```
+
+- Check status:
+
+```bash
+git status
+```
+
+- Commit staged changes with a message:
+
+```bash
+git commit -m "Describe your changes here"
+```
+
+- Create and switch to a new branch:
+
+```bash
+git checkout -b feature/your-feature-name
+```
+
+- Switch back to an existing branch:
+
+```bash
+git checkout main
+```
+
+- Push a branch to origin and set upstream:
+
+```bash
+git push -u origin feature/your-feature-name
+```
+
+- Push current branch to origin (after setting remote to SSH):
+
+```bash
+git push
+```
+
+- Pull latest changes from origin for the current branch:
+
+```bash
+git pull
+```
+
+Notes and troubleshooting:
+- If `ssh-add` returns "Could not open a connection to your authentication agent", re-run the `eval "$(ssh-agent -s)"` command and then `ssh-add` again.
+- If `clip.exe` is not available, run `cat ~/.ssh/id_ed25549.pub` and copy the output manually.
+- If you still see a permission error when pushing, confirm the public key was added to the GitHub account that has write access to the repository.
+
+If you want, I can also commit and push this `README.md` update for you.
*** End Patch
