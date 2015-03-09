## Flask Example: Blueprint on Arbitrary Endpoint

This uses Nginx to proxy an endpoint back to a simple Flask application. In this example, the endpoint is `herp/`.

The Flask Blueprint relies on an environment variable to determine that endpoint. This typically is specified in a run script, or a supervisor config. In this example, the run.sh file exports the `URL_PREFIX` variable, and the Blueprint in `simple_app.py` picks that up and uses it, if it's been provided. If that environment variable has *not* been set, then it simple defaults to an empty prefix, and is mounted at the root (`/`).

The included nginx config is set to run on port 5100. The Flask app will run on port 5000, which is the Flask default. See `app.py` to change that.

### Instructions:

1. Add the `app.nginx.conf` file to your Nginx server's configuration, either by including it in the nginx.conf file (`include /path/to/file.conf;`), or by copying the file into the `sites-enabled/` directory, etc.

2. Create a virtual environment, and `pip install Flask`, or use an existing one that already has Flask installed.

3. Restart Nginx. Verify that it reloaded correctly. troubleshoot any errors with `(sudo) nginx -t`.

4. Activate the virtualenv, and run the app:

```
$ /path/to/venv/bin/activate
(venv)$ cd /path/to/app
(venv)$ ./run.sh
```

5. Open your browser to [http://localhost:5100/herp/](http://localhost:5100/herp/).

