# **py-safe-dict**

This project was created with the intention of helping developers to easily and securely access dictionary attributes without having to deal with access errors.

</br>
</br>

# Motivations:
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

With SafeDict, you can easily access attributes with a cool syntax!

</br>
</br>


# Usage

How to use it:

1. wrap your ```dict``` with Safedict:
```python
my_safe_dict = SafeDict(**my_dict)
```

2. Map the path with the ```>>``` operator, using the key as string or index as list of int:
```python
my_safe_dict >> 'foo' >> ...
```

3. The last key must be mapped with ```>=```:
```python
... >= 'category' 
```

### **NOTE**
You can choose to end up with the operator ```>>```. In this case, you will have:
- A ```SafeDict``` type if the attribute is a sub-instance of a ```dict``` 
- A ```SafeSequence``` type if the attribute is a sub-instance of ```list``` or ```tuple```
- A ```SafeNone``` type if the attribute is None or if the declared path does not point to any attribute

</br>
</br>


# Examples

```python
# Simple attribute access
value = SafeDict(**test_dict_base) >> 'foo' >= 'fizz' # -> []

# Attribute access with sequences
value = SafeDict(**test_dict) >> 'foo' >> [0] >= 'info' # -> {'category': 'FOO', 'description': 'This is FOO'}

# Attribute access with None objects
value = SafeDict(**test_dict) >> 'bar' >> [0] >= 'info' # None

# Attribute access with bad path
value = SafeDict(**test_dict) >> 'bad' >> 'path' >> 'to' >= 'attr' # None
```
</br>
</br>


# Cotributing
Have you find a bug, typo or just want to contribute? Feel free to open an issue!

</br>
</br>


# Acknowledgements

Thanks to [Airscript](https://github.com/airscripts) for the inspiration of this project!