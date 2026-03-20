"""Turns any object into a CLI tool using Fire in the xonsh shell."""

@aliases.register
def _fire(args, stdout, stderr):
    """Turns any object into a CLI tool using Fire in the xonsh shell."""
    if len(args) == 0:
        print('Usage: fire <object name> [args|--help]', file=stderr)
        print('Example: fire @ --help', file=stderr)
        return 1
    def fixed_fire():
        """Fix https://github.com/google/python-fire/issues/188"""
        import fire
        fire.core.Display = lambda lines, out: stdout.write("\n".join(lines) + "\n")
        return fire
    with __xonsh__.env.swap(UPDATE_OS_ENVIRON=True, PAGER='-'):
        fixed_fire().Fire(evalx(args[0]), command=args[1:], name=args[0])
