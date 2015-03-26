# Cattle Python API and Client

A Python client for Cattle

## Installing

    pip install cattle

## Running as command line client

```bash
export CATTLE_URL=http://localhost:8080/v1

cattle --help

# curl -s http://localhost:8080/v1/widgets?foo=bar
cattle list-widget --foo=bar

# curl -s -X POST http://localhost:8080/v1/widgets -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
cattle create-widget --foo=bar

# curl -s -X PUT http://localhost:8080/v1/widgets/42 -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
cattle update-widget --id=42 --foo=bar

# curl -s -X DELETE http://localhost:8080/v1/widgets/42
cattle delete-widget --id=42
```

### Environment variables

|Name             | Description    | Example                                 |
|-----------------|----------------|-----------------------------------------|
|CATTLE_URL        | URL of the API | http://localhost:8080/v1                |
|CATTLE_ACCESS_KEY | Access Key     | 4C27AB31828A4E469C09                    |
|CATTLE_SECRET_KEY | Secrey Key     | fDxEzyxdFMWbmugstPpzykj2qA84Tn9DPDiAc3Sb|

The above environment variables can be passed as arguments on the command line such as `--url`, `--access-key`, and `--secret-key`.

### Bash Autocompletion

Add the below to your `.bashrc` or similar profile script:
```
eval "$(register-python-argcomplete cattle)"
```

## Using API

```python

import cattle

client = cattle.Client(url='http://localhost:8080/v1',
                       access_key='4C27AB31828A4E469C09',
                       secret_key='fDxEzyxdFMWbmugstPpzykj2qA84Tn9DPDiAc3Sb')

# curl -s http://localhost:8080/v1/widgets?foo=bar
client.list_widget(foo='bar')

# curl -s -X POST http://localhost:8080/v1/widgets -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
client.create_widget(foo='bar')

# curl -s -X PUT http://localhost:8080/v1/widgets/42 -H 'Content-Type: application/json' -d '{ "foo" : "bar" }'
widget = client.by_id_widget('42')
client.update(widget, foo='bar')

# curl -s -X DELETE http://localhost:8080/v1/widgets/42
widget = client.by_id_widget('42')
client.delete(widget)

# Links
# curl -s -X DELETE http://localhost:8080/v1/widgets/42/foobars
widget = client.by_id_widget('42')
widget.foobars()
```

## Contact
For bugs, questions, comments, corrections, suggestions, etc., open an issue in [rancherio/rancher](//github.com/rancherio/rancher/issues) with a title starting with `[cattle-cli] `.

Or just [click here](//github.com/rancherio/rancher/issues/new?title=%5Bcattle-cli%5D%20) to create a new issue.


## License

MIT Style
