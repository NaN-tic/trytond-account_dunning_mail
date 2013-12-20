#This file is part account_dunning_mail module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .dunning import *


def register():
    Pool.register(
        Dunning,
        module='account_dunning_mail', type_='model')
    Pool.register(
        AccountDunningGenerateTemplateEmail,
        module='account_dunning_mail', type_='wizard')
