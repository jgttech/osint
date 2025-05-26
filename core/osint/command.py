from click import Group
from functools import wraps
from click import pass_context, Context

def command(group: Group, name: str):
    """
    Custom decorator that creates a Click command for OSINT tools.

    Args:
        name: The name of the command
    """

    def decorator(func):
        @group.command(name, context_settings=dict(
            ignore_unknown_options=True,
            allow_extra_args=True,
        ))
        @pass_context
        @wraps(func)
        def wrapper(ctx: Context):
            return func(ctx)

        return wrapper

    return decorator
