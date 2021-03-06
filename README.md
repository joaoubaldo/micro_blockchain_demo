# Micro blockchain demo

An interactive tool I built to play around with _blockchain_ concepts.

## Quick install and usage (using virtualenv)
```
virtualenv demo_env
demo_env/bin/pip install git+https://github.com/joaoubaldo/micro_blockchain_demo.git
demo_env/bin/micro_blockchain_demo
```

## Quick run with docker
```
docker run -ti python:2.7 bash -c 'apt-get update && apt-get install -y git && pip install git+https://github.com/joaoubaldo/micro_blockchain_demo.git && micro_blockchain_demo'
```

## Usage
Once inside the interactive command line, type `?` or `help` to see all available options.

### Example:

- a) Append 100 random blocks to the chain b) print them all c) run integrity check d) tamper a random block e) rerun the integrity check:
```
> populate 100
> print
> check
> tamper
> check
> quit
```


## Running tests
`python -m unittest -v tests`


