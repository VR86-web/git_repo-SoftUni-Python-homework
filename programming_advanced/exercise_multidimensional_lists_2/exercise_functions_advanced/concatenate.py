def concatenate(*args, **kwargs):
    concatenated_args = "".join(args)
    for key, value in kwargs.items():
        concatenated_args = concatenated_args.replace(key, value)

    return concatenated_args

