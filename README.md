# Micro blockchain demo

An interactive tool I built to play around with _blockchain_ concepts.

## Quick install and usage (using virtualenv)
```
virtualenv demo_env
demo_env/bin/pip install git+https://github.com/joaoubaldo/micro_blockchain_demo.git
demo_env/bin/micro_blockchain_demo
```

## Usage
Once inside the interactive command line, type `?` or `help` to see all available options.

### Example:

- 1) Append 100 random blocks to the chain 2) print them all  3) run integrity check 4) tamper a random block 5) rerun the integrity check:
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


