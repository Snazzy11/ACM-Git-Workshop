# Password Manager (CPS 240 Project)

A simple JavaFX password manager app.
<!-- TOC -->
* [Password Manager (CPS 240 Project)](#password-manager-cps-240-project)
  * [Setup](#setup)
  * [Features](#features)
  * [Project Structure](#project-structure)
  * [Code Style](#code-style)
  * [How to Run](#how-to-run)
    * [For IntelliJ Users](#for-intellij-users)
  * [Git Usage](#git-usage)
<!-- TOC -->
## Setup
Refer to `How to Run` which is farther down

## Features
- Add passwords with associated website urls
- Edit, delete, and generate passwords
- Password strength detection
- Secure AES encryption of stored passwords
- Save data to files persistently
- Relatively complex GUI with multiple components
- Uses several design patterns
- Threading
- Leaked password detection
- Password recovery if master password is forgotten

## Project Structure
``` text
src/
    app/
        Main.java  // Launches the app
    components/
        PasswordManagerGUI  // Main driver for the UI of the app
        *JavaFX visuals built as induvidual components*
        WARNING: We SHOULD be building multiple components. There should be multiple files here, not a couple big ones.
    controller/
        *Interface between frontend and backend*
    model/
        *Data models for objects which need to be represented from storage*
    util/
        *Backend processing*
        WARNING: Methods here should never be called by the frontend.
data/
    backups/
        *Automatic backups of password list*
        .gitkeep // Tells git to keep the directory even when no files are present
    *data and output files*
    backup_key.dat // Holds the master key, encrypted with a secret recovery key given to the user
    master_password.dat // Holds the hash of the master password,  and the hash of the secuirty question answer
    password_statistics.dat // Holds statistics about the user's passwords
    passwords.csv // Primary password storage
    rockyou.txt // List of leaked passwords
    security_question.txt // Plaintext of the user's security question
```

## Code Style
- Use JavaDocs everywhere. 
  - Typing `/**` and pressing enter should auto-generate a JavaDoc. 
  - **Every** method and class should have documentation unless that particular function is so obvious and simple that it is not necessary.
  - Each JavaDoc should include at minimum:
    - A description of the method and what it computes/does
    - A description of what each parameter is and is for
    - A description of the return value
    - If an exception is important to its functionality, describe it in the Javadoc as well
  - Comments inside of functions which describe their behavior are also encouraged
- Use `camelCase`
- Classes with data should have private data fields and force usage of getter and setter functions
- Leaving `TODO`s in the code is fine, but they should be resolved or removed regularly

## How to Run
1. Open this project in your IDE.
2. Ensure you have Zulu sdk WITH JavaFX
3. Run `Main.java` in the `app` package.
4. A starter JavaFX window should appear.

### For IntelliJ Users
You should create a run configuration.
1. With the project open, click the hamburger icon
2. Under the `File` tab, click `Project Structure`
3. Under the `SDK` area, make sure you are using Zulu with JavaFX
4. At the top of the app, by the run button, click the dropdown menu that says current file
5. Click `edit configurations`
6. Add a new configuration with the plus button
7. Click `Application`
8. Click `Modify Options` and then select `Add VM Options`
9. Add `--enable-native-access=javafx.graphics` to the VM options
10. Select the LoginApp.java in the app package as the class to run.
11. If you have issues getting this to work, skip to 13-i
12. Use this run configuration to run the project from now on
13. Steps after this may or may not be necessary. Use if you have issues
    1. I was not able to run my program after pulling. To fix:
       1. File -> Project Structure -> Modules
       2. Click src folder and press sources button
       3. The src folder should become blue and problem is fixed

## Git Usage
Go to the issues page to pick out individual tasks.
_Always_ make a branch to push your code to. 
If you are not sure what you are doing, contact the group lead.