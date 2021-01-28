def age_assignment(*args, **kwargs):
    return {name: kwargs[name[0]] for name in args}
