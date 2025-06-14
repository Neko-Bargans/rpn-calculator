* Add a CICD which execute tests (pytest, flake8, pylint, black), and may even deploy on a dev env and execute E2E tests then
* Currently i am restricting on int but it could easily supports float too
* add monitoring on the /health
* Configure poetry to better "package" this project
* Add a column created_at, updated_at
* use uuid4 for stack ids to reduce risk on unicity of the key
