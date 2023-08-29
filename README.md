# **py-safe-dict**
### Version: 0.2.0

*py-safe-dict* is a python project created with the intention of helping developers to easily and securely access dictionary attributes without having to deal with checks and errors.

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


Generally, if you want to get nested attributes you should probably use:
```python
my_dict['foo'][0]['info']['category'] # -> FOO
```

... but if you try to get *'extra'* key, which is not in the ```dict```:

```python
my_dict['foo'][0]['info']['extra'] # -> KeyError: 'extra'
```

With ```py-safe-dict```, you can easily access attributes with a cool syntax!

</br>
</br>


# Usage

How to use it:

1. wrap your ```dict``` with ```safe```:
```python
my_safe_dict = safe(my_dict)
```

2. Map the path with the ```>>``` operator, using the key as ```string``` or index as ```list``` of ```int```:
```python
my_safe_dict >> 'foo' >> [0] >> ... 
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
value = safe(my_dict) >> 'foo' >= 'fizz' # -> []

# Attribute access with sequences
value = safe(my_dict) >> 'foo' >> [0] >= 'info' # -> {'category': 'FOO', 'description': 'This is FOO'}

# Attribute access with None objects
value = safe(my_dict) >> 'bar' >> [0] >= 'info' # -> None

# Attribute access with bad path
value = safe(my_dict) >> 'bad' >> 'path' >> 'to' >= 'attr' # -> None

```

</br>

You can also deal with ```sequences``` of ```dict```:

</br>

```python
my_list = [
            {'info': {'name': 'FOO'}}, 
            {'info': {'name': 'BAR'}}, 
            {'info': {'name': 'FIZZ'}}
          ]

value = safe(my_list) >> [2] >> 'info' >= 'name' # -> 'FIZZ'

```

**NEW in 0.2.0**

Now, you can deal with multiple index:

```python
value = safe(test_dict) >> 'foo' >> [0, 1] >= 'info'

```


</br>
</br>


# Contributing
Have you find a bug, typo or just want to contribute? Feel free to open an [issue](https://github.com/mat-bro/py-safe-dict/issues) or start a [discussion](https://github.com/mat-bro/py-safe-dict/discussions)!

</br>
</br>


# Acknowledgements

Thanks to [Airscript](https://github.com/airscripts) for the inspiration of this project!