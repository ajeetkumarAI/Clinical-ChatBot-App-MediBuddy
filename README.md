
# Clinical-ChatBot-App-MediBuddy — Quick Git & SSH Guide

Short, copy-paste steps for setting up SSH (on Windows using Git Bash) and everyday Git commands for this repository.

## Prerequisites

- Git and Git Bash installed
- A GitHub account with access to this repository

## 1) Create or locate your SSH key

If you don't have an SSH key, generate one (replace with your email):

```bash
ssh-keygen -t ed25519 -C "<emailid>@gmail.com"
# Accept defaults (press Enter) to store at ~/.ssh/id_ed25519
```

## 2) Start the ssh-agent and add your key (Git Bash)

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

If you see `Could not open a connection to your authentication agent`, re-run the `eval` line and then `ssh-add` again.

## 3) Copy the public key and add it to GitHub

```bash
cat ~/.ssh/id_ed25519.pub | clip.exe
```

- Open: https://github.com/settings/ssh/new
- Paste the key, give it a title (e.g., "Work laptop - Git Bash"), and save.

If `clip.exe` is not available, run `cat ~/.ssh/id_ed25519.pub` and copy the output manually.

## 4) Verify the SSH connection

```bash
ssh -T git@github.com
```

Expected response on success:

```
Hi <your-username>! You've successfully authenticated, but GitHub does not provide shell access.
```

## 5) Point the repo to SSH and push

```bash
git remote set-url origin git@github.com:ajeetkumarAI/Clinical-ChatBot-App-MediBuddy.git
git push -u origin main
```

## Git basics (common commands)

- Stage all changes:

```bash
git add .
```

Before staging and committing, create and switch to a feature branch (recommended):

```bash
git checkout -b feature/your-feature-name
```

If you already staged changes, you can still create the branch before committing; staged changes remain.


- Stage a specific file:

```bash
git add path/to/file
```

- Show status:

```bash
git status
```

- Commit with message:

```bash
git commit -m "Short descriptive message"
```

- Create and switch to a new branch:

```bash
git checkout -b feature/your-feature-name
```

- Switch branches:

```bash
git checkout main
```

- Push a branch and set upstream:

```bash
git push -u origin feature/your-feature-name
```

- Push current branch:

```bash
git push
```

- Pull remote changes:

```bash
git pull
```
