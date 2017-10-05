# from dsl_parser.functions import Function


class Func1(object):
    def __init__(self, args, scope=None, context=None, path=None, raw=None):
        self.scope = scope
        self.context = context
        self.path = path
        self.raw = raw
        self.parse_args(args)

    def parse_args(self, args):
        print 'args', args
        return 58

    def validate(self, plan):
        raise RuntimeError('validate')

    def evaluate(self, plan):
        raise RuntimeError('evaluate')

    def evaluate_runtime(self, storage):
        raise RuntimeError('evaluate_runtime')
