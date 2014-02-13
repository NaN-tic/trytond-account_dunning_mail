#This file is part account_dunning_mail module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView
from trytond.pool import PoolMeta
from trytond.pyson import Eval
from trytond.modules.electronic_mail_wizard import GenerateTemplateEmail

__all__ = ['Dunning', 'AccountDunningGenerateTemplateEmail']
__metaclass__ = PoolMeta


class Dunning:
    __name__ = 'account.dunning'

    @classmethod
    def __setup__(cls):
        super(Dunning, cls).__setup__()
        cls._buttons.update({
                'wizard_email_account_dunning': {
                    'invisible': Eval('state') != 'done'
                    },
                'done': {
                    'invisible': Eval('state') == 'done',
                    },
                })

    @classmethod
    @ModelView.button
    def done(cls, dunnings):
        cls.process(dunnings)

    @classmethod
    @ModelView.button_action('account_dunning_mail.wizard_email_account_dunning')
    def wizard_email_account_dunning(cls, dunnings):
        pass


class AccountDunningGenerateTemplateEmail(GenerateTemplateEmail):
    "Account Dunning Wizard to Generate Email from template"
    __name__ = "electronic_mail_wizard.account_dunning"
