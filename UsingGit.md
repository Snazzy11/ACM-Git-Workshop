# Starting Up Git

# First Time Setup
## 1. Install Git

Verify installation:

```bash
git --version
```

If you see a version number its installed. If not, get git
```
On Mac: git-scm.com
On Windows: https://git-scm.com/download/win
On Linux: apt install git
```

## Setup Option 1
### Manual auth
In order to push to Git, you need to be authenticated.

Run:
```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```
Use the same email as your GitHub account.

Verify with:
```bash
git config --global --list
```

### Set Up SSH

We use SSH because it can be simpler than configuring a token.
1. Generate SSH Key
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
Press Enter through all prompts.
Add SSH Key to Agent
```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Copy Public Key
```bash
cat ~/.ssh/id_ed25519.pub
```
Copy the output.
Add to GitHub

    Go to GitHub → Settings

    SSH and GPG keys

    Click New SSH Key

    Paste your key

    Save

Test Connection
```bash
ssh -T git@github.com
```
You should see:

`Hi username! You've successfully authenticated...`

If you see this message, you're done.

## Setup Option 2
You need GitHub CLI: https://cli.github.com/

Login with `gh auth login`


## During the Workshop
1. Clone the Repository

Use the SSH URL provided (it should start with git@github.com:).

```bash
git clone git@github.com:ORG_NAME/REPO_NAME.git
cd REPO_NAME
```

2. Create Your Branch

Never work directly on main.

```
git checkout -b your-team-name-feature
```

This creates a new branch and switches you to it. 
Remember that what makes git so great is that it protects you from breaking things.

3. Make Your Changes

Edit files normally.
4. Stage Your Changes

git add .

This prepares your changes for commit.
5. Commit Your Changes

git commit -m "Describe what you changed"

Good commit messages explain why, not just what.

Example:

Add input validation to prevent crash on empty string

6. Push Your Branch

git push -u origin your-team-name-feature

The -u sets the upstream so future pushes only require:

git push

7. Open a Pull Request

    Go to the repository on GitHub

    Click Compare & pull request

    Submit

And you should be done and set up at this point

### Commands you might need
```bash
git clone
git checkout -b branch-name
git add .
git commit -m "message"
git push -u origin branch-name
```

### Troubleshooting
Check your remote
`git remote -v`

If you see https://, you are using the wrong protocol.
To fix it:

`git remote set-url origin git@github.com:ORG_NAME/REPO_NAME.git`

Check Current Branch
`git branch`

The * shows your active branch.

Check Status
`git status`

This tells you what Git thinks is happening.
Notes

    Do not commit directly to main

    Dont panic, Git tracks everything

    You cannot permanently destroy the project with normal commands

