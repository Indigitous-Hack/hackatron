import logging
import random
import pkg_resources
from Legobot.Lego import Lego

logger = logging.getLogger(__name__)

class Encourage(Lego):
    def __init__(self,baseplate,lock,encouragement,*args,**kwargs):
        super().__init__(baseplate,lock)

        self.e = encouragement
        return

    def listening_for(self, message):
         if 'encourage me' in message['text']:
             logger.info('Lego %s activated' % self.get_name())
             return True

    def handle(self, message):
        opts = None
        logger.info(message)
        try:
            target = message['metadata']['source_channel']
            opts = {'target':target}
        except IndexError:
            logger.error('Could not identify message source in message: %s' % str(message))
        txt = self.get_single_quote(self.get_all_quotes(self.e))
        self.reply(message, txt, opts)

    def get_name(self):
        return 'encourage'

    def get_help(self):
        help_text = "Helpful motivational quotes " \
                    "from influential figures such as Shia LeBouf, "\
                    "Courage Wolf, and your drill sergeant."
        return help_text

    def get_single_quote(self,quotes):
        quote = random.choice(quotes)
        quote = quote.strip()
        logger.info(quote)
        return quote

    def get_all_quotes(self,infile):
        with open(infile,'r') as f:
            content = f.readlines()
        logger.info(content)
        return content
