from . import PDNSCommand
class STATISTICS(PDNSCommand):
    NAME = 'statistics'
    DESCRIPTION = 'statistics related API actions'
    COMMANDS = ['statistics']

    @classmethod
    def init_parser(cls, subparsers, zone_parser):
        # statistics

        subparsers.add_parser('statistics', help='show internal statistics')

    def run(self):
        getattr(self, (self.args.action).replace('-', '_'))()
