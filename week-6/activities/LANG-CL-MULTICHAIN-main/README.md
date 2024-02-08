# LCEL

This lab covers LCEL, or LangChain Expression Language.

## Instructions
- The provided code for this lab contains a general outline for creating a chain that is comprised of other chains. There are 2 "sub-chains".
    1. The first chain takes a movie name as input and produces a list of actors who appear in that movie.
    2. The second chain takes a list of actors and returns movies which have at least 3 of these actors in its cast.
- The final chain combines these 2 chains such that it can take in a movie as input and return a list of movies which share at least 3 common actors.
- LCEL, or LangChain Expression Language, provides a unified interface for chain creation.
```

## Extra Reading
- Take a look at the official [Python Langchain Docs](https://python.langchain.com/docs/expression_language/get_started)
- Documentation on [Multiple Chains](https://python.langchain.com/docs/expression_language/cookbook/multiple_chains)

## Shouldn't Modify (But Look at for Context)
- [src/main/app.py](src/main/app.py) (Can also run this for manual testing)
- [src/test/test_lab.py](src/test/test_lab.py)
- [src/main/example.py](src/main/example.py) (Can also run to see an example of multi-chaining)

## Should Modify
- [src/main/lab.py](src/main/lab.py) - look out for TODO statements
