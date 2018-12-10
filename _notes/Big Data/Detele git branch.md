##  Delete Git a Branch (local or remote)

To delete a local branch

```sh
git branch -d <local_branch>
```

To remove a remote branch (if you know what you are doing!)

```sh
git push origin :<remote_branch>
```

or simply use the new syntax (v1.7.0)

```sh
git push origin --delete <remote_branch>
```