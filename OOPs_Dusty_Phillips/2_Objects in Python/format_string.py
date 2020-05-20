def format_string(string, formatter=None):
    class DefaultFormatter:
        def format(self, string):
            return str(string).title()

    if not formatter:
        formatter = DefaultFormatter()
        return formatter.format(string)


print(format_string("hello rajeev"))
