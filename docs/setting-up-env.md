# Setting Up The Environment

> [!IMPORTANT]
> This project uses `postgres` for its backend database. You must either install this locally or use some managed service such as vercel.

## Setup Environment Variables

- If `PYTHON_ENV` is not set, the app assumes the environment to be a dev env, else it assumes it to be a production env.
- This app automatically loads environment variables from a local file called `.env.production` and `.env.development` according to the setting (as described above).

> [!NOTE]
> You can also choose to not use this file and instead set environment variables before running the app according to your platform.

> [!TIP]
> The list of required environment variables is placed in `.env.example` without the actual values of the variables!
