# py-safe-dict

Safedict was created with the intention of helping developers to easily and securely access dictionary attributes without having to deal with access errors.

## Motivations:
Suppose you have a nested dict like this:

```python
{
    'foo': [
        {
            'code': 123, 
            'date_prod': datetime(2023, 1, 1, 10, 14, 0),
            'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
            'info': {'category': 'FOO', 'description': 'This is FOO'}
        },
        {
            'code': 123, 
            'date_prod': datetime(2023, 1, 1, 10, 16, 0),
            'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
            'info': {'category': 'FOO', 'description': 'This is FOO'}
        },
        {
            'code': 123, 
            'date_prod': datetime(2023, 1, 1, 10, 22, 0),
            'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
            'info': {'category': 'FOO', 'description': 'This is FOO'}
        },
        
    ],

    'bar': [
        {
            'code': 123, 
            'date_prod': datetime(2023, 1, 1, 10, 14, 0),
            'date_in_wh': datetime(2023, 2, 14, 9, 30, 0),
            'info': None
        },
    ],

    'fizz': []
}
```


If you want to get nested attributes, you should probably use:
```python
my_dict['foo'][0]['info']['category'] # -> FOO
```

What happens if you try to get *'extra'*:

```python
my_dict['foo'][0]['info']['extra'] # -> KeyError: 'extra'
```

With SafeDict, oyu can easily access attribute with a cool syntax!

## Examples

```python
# Simple attribute access
value = SafeDict(**test_dict_base) >> 'foo' >> 'bar'

# Attribute access with sequences
value = SafeDict(**test_dict) >> 'foo' >> [0] >> 'info'

# Attribute access with None objects

```



# Acknowledgements

thanks to [Airscript](https://github.com/airscripts) for the inspiration of this project!